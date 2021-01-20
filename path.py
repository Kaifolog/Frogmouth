# -*- coding: utf8 -*-
from pathlib import Path
import importlib
import threading
# you have to initialize all threads in "pollingStart" function


def pollingStart(App):
    """
    |   This is place for your handlers and threads.
    |
    |   app -+
    |         | - config
    |         | - bot
    |         | - manager
    """

    @bot.message_handler(commands=['start'])
    def start_message(message):
        app.logging.info('"/start" by' + str(message.chat.id) +
                         " as " + message.chat.username)
        Hello.sayhello(app, message)

    @bot.message_handler(commands=['sin'])
    def start_message(message):
        app.logging.info('"/sin" by' + str(message.chat.id) +
                         " as " + message.chat.username + "with message \n\t" + message.text)
        Hello.sin(app, message)

    app.logging.info("Polling started.")
    bot.polling()

    """
    |
    """


"""  _______________________________________________________________________________________________________________________________________________  """


def pollingInit(App):
    """
        Getting app object into module
        Importing user modules
    """
    global app
    global bot
    global config
    app = App

    for file in app.manager.modules:
        path = Path(file)

        globals().update(importlib.import_module(
            app.config.MODULE_PATH[:-1] + "." + path.stem).__dict__)
        app.logging.info('\t\"%s\" module imported successfully\n', path.stem)

    bot = app.bot
    config = app.config


if __name__ == "__main__":
    pass
