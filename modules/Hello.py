from math import sin


class Hello:
    def sayhello(app, message):
        app.bot.send_message(
            message.chat.id, "Hello!")

    def sin(app, message):
        corner = message.text.split(" ")[1]
        try:
            app.bot.send_message(
                message.chat.id, sin(int(corner)))
        except ValueError:
            app.logging.error('ValueError')
            app.bot.send_message(
                message.chat.id, "Wrong argument, try one more time")
