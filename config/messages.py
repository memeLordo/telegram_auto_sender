class Ads:
    FREE_ASSIST = (
        "#вакансия \n"
        "\n"
        "В дружную команду международной компании Stonks требуется"
        "операционный менеджер! \n"
        "\n"
        "Stonks - эксперты в сегменте криптотестнетов, объединившиеся "
        "с uCrypto для создания фонда, позволяющего инвесторам зайти в "
        "нишу тестнетов с помощью опыта и команды из более чем 25 человек."
        " Компания активно развивается в области тестнетов и работает на "
        "англоязычную и СНГ-аудиторию. \n"
        "\n"
        "Зарплата: 35 000 ₽, есть доплаты за переработки во внеурочное время\n"
        "Место работы: офис в центре Казани\n"
        "\n"
        "Если у тебя есть:\n"
        "- Опыт работы не менее 1 года\n"
        "- Умение доводить дела до конца \n"
        "- Ответственность и усидчивость \n"
        "\n"
        "Задачи:\n"
        "- Ведение отчетности в конце дня и недели\n"
        "- Работа с большими объемами данных\n"
        "- Командная работа\n"
        "- Управление и контроль выполнения задач\n"
        "- Расстановка приоритетов\n"
        "\n"
        "Условия:\n"
        "- Гибкая занятость\n"
        "- сб и вс выходные\n"
        "- возможно совмещение с учебой\n"
        "- Карьерный рост до руководителя офиса\n"
        "- Возможность оформления по договору ГПХ или с ИП\n"
        "- Комфортный офис с чилл-зоной 300 кв. метров\n"
        "- Полноценное комплексное питание\n"
        "- Выдача персонального компьютера \n"
        "- Интересные задачи и постоянный профессиональный рост\n"
        "\n"
        'Заинтересовала вакансия, пиши "операционка" @behetly\n'
    )

    NEW_FA = (
        "#вакансия \n"
        "\n"
        "В дружную команду международной компании Stonks требуется"
        "операционный менеджер! \n"
        "\n"
        "Stonks - эксперты в сегменте криптотестнетов, объединившиеся "
        "с uCrypto для создания фонда, позволяющего инвесторам зайти в "
        "нишу тестнетов с помощью опыта и команды из более чем 25 человек."
        " Компания активно развивается в области тестнетов и работает на "
        "англоязычную и СНГ-аудиторию. \n"
        "\n"
        "Зарплата: 35 000 ₽, есть доплаты за переработки во внеурочное время\n"
        "Место работы: офис в центре Казани\n"
        "\n"
        "Если у тебя есть:\n"
        "- Опыт работы не менее 1 года\n"
        "- Умение доводить дела до конца \n"
        "- Ответственность и усидчивость \n"
        "\n"
        "Задачи:\n"
        "- Ведение отчетности в конце дня и недели\n"
        "- Работа с большими объемами данных\n"
        "- Командная работа\n"
        "- Управление и контроль выполнения задач\n"
        "- Расстановка приоритетов\n"
        "\n"
        "Условия:\n"
        "- Гибкая занятость\n"
        "- сб и вс выходные\n"
        "- возможно совмещение с учебой\n"
        "- Карьерный рост до руководителя офиса\n"
        "- Возможность оформления по договору ГПХ или с ИП\n"
        "- Комфортный офис с чилл-зоной 300 кв. метров\n"
        "- Полноценное комплексное питание\n"
        "- Выдача персонального компьютера \n"
        "- Интересные задачи и постоянный профессиональный рост\n"
        "\n"
        'Заинтересовала вакансия, пиши "операционка" в ЛС\n'
    )


class Keywords:
    FIRST_MESSAGE = ["работа"]
    FORM = [
        "заполнил",
        "заполнила",
        "отправил",
        "отправила",
        "прислал",
        "прислала",
        "+",
    ]
    SEARCHED_DIRS = ["Новые FA", "Free assist"]


class Reply:
    def say_hi(name=None):
        name = "" if name is None else f" {name}"
        return (
            f"Привет{name}, рад, что вы откликнулись на вакансию🔥\n"
            "Расскажите подробнее о вашем опыте работы,"
            " чтобы я смог узнать о вас побольше)"
        )

    FORM = (
        "Для того, чтобы принять вашу заявку, вам нужно будет заполнить форму,"
        " которая пойдёт непосредственно директору для ознакомления. "
        "Вот ссылка на неё:\n"
        "https://docs.google.com/forms/d/e/"
        "1FAIpQLScQ4MXsn-Qrl38tRwgB6O5LPXrGt2Wasv8H5hCvA-N5H4w2Hw/viewform\n"
        'После этого отпишитесь, например "+", и мы продолжим диалог.'
    )

    FINISH = (
        "Отлично. Теперь ваша заявка рассмотрена и отправлена на утверждение "
        "директору. Если вы нам подойдёте, то я свяжусь с вами. "
        "И если у вас остались вопросы, то смело задавайте их!"
    )