from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater,CommandHandler, CallbackQueryHandler, CallbackContext, InvalidCallbackData

import random

import config

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Для взаимодействия напишите /ooo")


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "абоба абоба абоба \n"
        "абоба"
    )


def generate(update: Update, context: CallbackContext) -> None:

    l1 = ['солнечный', 'траурный', 'плюшевый', 'бешеный', 'памятный', 'трепетный', 'базовый', 'скошенный', 'преданный', 'ласковый', 'пойманный', 'радужный', 'огненный', 'радостный', 'тензорный', 'шёлковый', 'пепельный', 'ламповый', 'жареный']
    l2 = ['зайчик', 'Верник', 'глобус', 'ветер', 'щавель', 'пёсик', 'копчик', 'ландыш', 'стольник', 'мальчик', 'дольщик', 'Игорь', 'невод', 'егерь', 'пончик', 'лобстер', 'жемчуг', 'кольцик', 'йогурт']
    l3 = ['стеклянного', 'ванильного', 'резонного', 'широкого', 'дешёвого', 'горбатого', 'собачьего', 'исконного', 'волшебного', 'картонного', 'лохматого', 'арбузного', 'огромного', 'запойного', 'великого', 'бараньего', 'вандального', 'едрёного', 'парадного']
    l4 = ['глаза', 'плова', 'пельша', 'мира', 'деда', 'жира', 'мема', 'ада', 'бура', 'жала', 'нёба', 'гунна', 'хлама', 'шума', 'воза', 'сала', 'фена', 'зала', 'рака']

    text = "Моя оборона "

    text += l1[random.randint(0, len(l1) - 1)] + " "
    text += l2[random.randint(0, len(l2) - 1)] + " "
    text += l3[random.randint(0, len(l3) - 1)] + " "
    text += l4[random.randint(0, len(l4) - 1)] + " "

    update.message.reply_text(text.upper())


def main() -> None:
    updater = Updater(config.TOKEN, arbitrary_callback_data=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('ooo', generate))

    updater.start_polling()


if __name__ == '__main__':
    main()
