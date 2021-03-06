from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import *
import random
import os
import re

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

    TOKEN = os.environ['TOKEN']
    APPNAME = os.environ['APPNAME']
    PORT = int(os.environ.get('PORT', '8443'))

    updater = Updater(TOKEN, arbitrary_callback_data=True)

    updater.dispatcher.add_handler (
        ConversationHandler (
            entry_points = [CommandHandler('start', start)],
            states = {1 : [MessageHandler((Filters.regex(re.compile(r'ооо', re.IGNORECASE)) ^ Filters.regex(re.compile(r'ooo', re.IGNORECASE))), generate)]},
            fallbacks = [CommandHandler('info', info)]
        )
    )

    updater.start_webhook (
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url="https://{appname}.herokuapp.com/{token}".format(appname=APPNAME, token=TOKEN)
    )


if __name__ == '__main__':
    main()
