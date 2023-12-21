import asyncio
import datetime as dt
from datetime import date

from config.messages import Deviation, Keywords, Assistant
from loguru import logger
# from telethon.sync import TelegramClient
from telethon.types import Message, User
from tools.editor import make_plain
from tools.checker import is_user

from .clients import choose_clients, show_client
from .tags import UserStatus


class ExitLoop(Exception):
    pass


today: date = dt.date.today()

logger.add(
    "process.log",
    format="{time:DD-MM-YYYY at HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="10 MB",
    retention="2 days",
    compression="zip",
)


@logger.catch
async def sent_reply_start(bebra: User) -> None:
    log_name: str = bebra.first_name
    first_name = bebra.first_name.split(" ")[0]

    await asyncio.sleep(1)
    #############
    await client.send_read_acknowledge(bebra)
    async with client.action(bebra, "typing"):
        await asyncio.sleep(4)
        await client.send_message(bebra, Assistant.say_hi(first_name))

    async with client.action(bebra, "typing"):
        await asyncio.sleep(5)
        await client.send_message(bebra, Assistant.FORM)
        logger.debug(f"{show_client(client)}: message sent to {log_name}")


@logger.catch
async def sent_reply(
    bebra_user: User, message: Message
) -> None:
    log_name = bebra_user.first_name
    sender = bebra_user
    logger.info(f"{show_client(client)}: got message from {log_name}")
    await asyncio.sleep(1)
    await client.send_read_acknowledge(sender)

    with client.action(bebra_user, "typing"):
        await asyncio.sleep(4)
        await client.send_message(sender, message)
        logger.debug(f"{show_client(client)}: message sent to {log_name}")


async def match_sent_message(user: User, from_user: User, message: Message):
    read_message = make_plain(message.message).split(" ")
    r_message = set(read_message)
    if user != from_user:
        form_set: set = set(make_plain(Assistant.FORM).split(" "))
        finish_set: set = set(make_plain(Assistant.FINISH).split(" "))
        # TODO: change state
        if len(form_set & r_message) / len(form_set) >= Deviation.FORM:
            raise ExitLoop(f"{user.username} = {UserStatus.WAIT_FORM_REPLY}")
        if len(finish_set & r_message) / len(finish_set) >= Deviation.FINISH:
            raise ExitLoop(f"{user.username} = {UserStatus.DONE}")
        return

    logger.opt(colors=True).debug(
        f"<white>{read_message}</white> : {user.username}")
    upprove = Keywords.FIRST_MESSAGE
    ignore = Keywords.IGNORE
    if r_message & upprove and not (r_message & ignore):
        current_state = None
        match current_state:
            case None:
                await sent_reply_start(client, user)
                raise ExitLoop(f"First message sent to {user.username}")
                # TODO: send start_message to user
        # await sent_reply_start(client, user)


async def match_messages_from(user: User, from_user: User) -> None:
    user_messages_list = await client.get_messages(
        entity=user,
        from_user=from_user,
        limit=3,
    )
    if user_messages_list.total > 5:
        return
    user_messages = filter(
        lambda x: (today - x.date.date()).days <= Deviation.MESSAGE_AGE,
        user_messages_list,
    )

    for message in user_messages:
        if not message.message:
            continue
        await match_sent_message(user, from_user, message)


@logger.catch
async def check_new_messages() -> None:
    await client.start()
    global myself
    myself = await client.get_me()
    dialogs = client.iter_dialogs()

    async for dialog in dialogs:
        try:
            bebra = dialog.entity
            if not is_user(bebra):
                continue
            # logger.debug(bebra.username)
            # Проверяем статус по нашим полследним сообщениям из формы
            await match_messages_from(bebra, myself)

            # Далее определяем тип по последним сообщениям пользователя
            await match_messages_from(bebra, bebra)

        except ValueError as e:
            logger.critical(e.__class__.__name__)
        except ExitLoop as e:
            logger.success(repr(e))
            # print(dialog.name)
    logger.debug(show_client(client))


@logger.catch
def run_message_checker() -> None:
    logger.info("Begin check")
    clients = choose_clients()
    for current_client in clients:
        global client
        with current_client as client:
            client.session.save_entities = False
            client.loop.run_until_complete(check_new_messages())
    logger.success("")


if __name__ == "__main__":
    try:
        run_message_checker()
        # start_event_handler()
    except KeyboardInterrupt:
        pass
