import sys
from datetime import datetime

from loguru import logger
from telethon import functions, types
from telethon.sync import TelegramClient

import config

# from messages_config import ad_1, ad_2, ad_kazan
# from telethon.tl import types
logger.remove()
logger.add(sys.stderr, level="DEBUG")

client1 = TelegramClient('count1', config.api_id, config.api_hash)
client2 = TelegramClient('count2', config.api_id2, config.api_hash2)
client3 = TelegramClient('count3', config.api_id2, config.api_hash2)
clients = [client1, client2, client3]


def show_client(client):
    if client == client1:
        return 'client1'
    elif client == client2:
        return 'client2'
    else:
        return 'client3'


@logger.catch
async def start():
    logger.warning(f'Counting in {show_client(client)}')
    # request = await client(functions.messages.GetDialogFiltersRequest())
    # await count_date()
    await count_users()
    if client != clients[-1]:
        logger.debug(f'Current count: {count}')
    # print()


# async def count_date(request):

#     _data = []
#     for dialog_filter in request:
#         result = dialog_filter.to_dict()
#         for key, value in result.items():
#
#             if key == 'title':
#                 if value == 'Входящие':
#                     _data += result['exclude_peers']
#                 else:
#                     _data += result['include_peers']
#
#                 _data = _data + result['pinned_peers']
#
#     await count_users_in_dir(_data)
#
#     logger.success(count)


async def exclude_users():
    dialogs = await client.get_dialogs(archived=False)
    users = filter(lambda x: isinstance(x.entity, types.User), dialogs)
    return users


async def count_users():
    users = await exclude_users()
    messages_data = []
    for bebra in users:
        client_messages = await client.get_messages(
            entity=bebra,
            reverse=True,
            limit=1,
            from_user=bebra
        )
        if client_messages and client_messages.total < 30:
            messages_data.append(client_messages)
            logger.trace(client_messages.total)
    # messages_data = filter(lambda x: x.total < 30, messages_data)
    for date in todate:
        input_date = datetime.strptime(date, '%d.%m.%y').date()
        count[date] += len(
            list(filter(lambda x: x[0].date.date()
                 == input_date, messages_data))
        )


#     exclude_user_list = await exclude_users(_data)
#     logger.debug(len(exclude_user_list))
#     dialogs = await client.get_dialogs()
#     data = [x.entity for x in dialogs if x.entity not in exclude_user_list]
#
#     for bebra in data:
#
#         if not isinstance(bebra, types.User) or bebra.bot:
#             continue
#
#
#
#         for message in client_messages:
#             logger.debug(f'{bebra.first_name} {bebra.last_name}')
#             for date in todate:
#                 # logger.success(date, todate)
#                 input_date = datetime.strptime(date, '%d.%m.%y').date()
#                 message_date = message.date.date()
#                 # logger.debug(f'{input_date} - {message_date}')
#                 if input_date == message_date:
#
#                     global count
#
#                     logger.debug(f'{input_date} - {message_date}')
#                     # date = date.strftime('%d.%m.%y')
#
#                     count[date] = count[date]+1
#                     logger.debug(count)


def choose_date():
    input_date = sys.argv[1:]
    today = [datetime.today().strftime('%d.%m.%y')]
    if not input_date:
        return today
    return list(x for x in input_date)


if __name__ == '__main__':
    global todate, count
    todate = choose_date()
    count = dict.fromkeys(todate, 0)
    logger.trace(count)

    for current_client in clients:
        with current_client as client:
            client.session.save_entities = False
            client.loop.run_until_complete(start())

    for key, value in count.items():
        print(f'{key} {value}')
