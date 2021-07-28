from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import *
import random

import config

def start(update: Update, context: CallbackContext) -> None:

    update.message.reply_text("Для взаимодействия напишите \"ooo\"")

    return 1


def info(update: Update, context: CallbackContext) -> None:

    update.message.reply_text(
        "Бот, который изменит мир \n\n"
        "абоба абоба абоба \n"
        "абоба \n\n"
        "Made with ❤️ by Butukay, Stre1f"
    )

    return 1


def generate(update: Update, context: CallbackContext) -> None:

    l1 = ['солнечный', 'траурный', 'плюшевый', 'бешеный', 'памятный', 'трепетный', 'базовый', 'скошенный', 'преданный', 'ласковый', 'пойманный', 'радужный', 'огненный', 'радостный', 'тензорный', 'шёлковый', 'пепельный', 'ламповый', 'жареный', 'загнанный']
    l2 = ['зайчик', 'Верник', 'глобус', 'ветер', 'щавель', 'пёсик', 'копчик', 'ландыш', 'стольник', 'мальчик', 'дольщик', 'Игорь', 'невод', 'егерь', 'пончик', 'лобстер', 'жемчуг', 'кольщик', 'йогурт', 'овод']
    l3 = ['стеклянного', 'ванильного', 'резонного', 'широкого', 'дешёвого', 'горбатого', 'собачьего', 'исконного', 'волшебного', 'картонного', 'лохматого', 'арбузного', 'огромного', 'запойного', 'великого', 'бараньего', 'вандального', 'едрёного', 'парадного', 'укромного']
    l4 = ['глаза', 'плова', 'пельша', 'мира', 'деда', 'жира', 'мема', 'ада', 'бура', 'жала', 'нёба', 'гунна', 'хлама', 'шума', 'воза', 'сала', 'фена', 'зала', 'рака']

    text = "Моя оборона "

    text += l1[random.randint(0, len(l1) - 1)] + " "
    text += l2[random.randint(0, len(l2) - 1)] + " "
    text += l3[random.randint(0, len(l3) - 1)] + " "
    text += l4[random.randint(0, len(l4) - 1)] + " "

    update.message.reply_text(text.upper())

    return 1


def main() -> None:

    updater = Updater(config.TOKEN, arbitrary_callback_data=True)

    updater.dispatcher.add_handler(
        ConversationHandler(
            entry_points = [CommandHandler('start', start)],
            states = {1 : [MessageHandler((Filters.regex('ooo') ^ Filters.regex('ооо')), generate)]},
            fallbacks = [CommandHandler('info', info)]
        )
    )

    updater.start_polling()


if __name__ == '__main__':
    main()
