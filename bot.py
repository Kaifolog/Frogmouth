"""
        Application main file  
"""

import logging
import telebot
import config
import path

from modules.module import ModuleManager as Manager


class App:
    """Programm main class that callable from everywhere"""

    def __init__(self, bot):
        self.bot = bot
        self.config = config
        self.manager = Manager(self)
        self.logging = logging


if __name__ == "__main__":

    # start logging
    logging.basicConfig(format='<%(levelname)s> [%(asctime)s %(name)s] %(message)s',
                        level=logging.INFO,
                        filename='bot.log')
    # bot object creation
    bot = telebot.TeleBot(config.BOT_TOKEN)
    logging.info('bot initialization complete')
    # app object creation
    app = App(bot)
    for module in app.manager.modules:
        logging.info("\t %s module found\n", module)

    # starting mainloop
    path.pollingInit(app)
    logging.info('polling initialization complete')

    logging.info("Starting polling")
    path.pollingStart(app)
