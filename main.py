# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(update.message.text)


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater('1658734136:AAFzFOylGxk7296zs12EKT4dLMEgg8ey2Is', use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    def start(update, context):
        update.message.reply_text(
            "Ну ё-моё, Лёха! 500 рублей с зп удержим")

    def help(update, context):
        update.message.reply_text(
            "Я пока не умею помогать... Я только ваше эхо.")

    # Зарегистрируем их в диспетчере рядом
    # с регистрацией обработчиков текстовых сообщений.
    # Первым параметром конструктора CommandHandler я
    # вляется название команды.
    dp.add_handler(CommandHandler("leha_nascal", start))
    dp.add_handler(CommandHandler("help", help))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()