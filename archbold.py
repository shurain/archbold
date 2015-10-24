import logging
import httplib

import telegram

from settings import TOKEN
from router import EventHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger('archbold_basic')
logger.setLevel(logging.DEBUG)


def mainloop():

    bot = telegram.Bot(TOKEN)

    handler = EventHandler()

    if len(bot.getUpdates()) == 0:
        LAST_UPDATE_ID = -1
    else:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
            text = update.message.text
            chat_id = update.message.chat.id
            update_id = update.update_id

            if text:
                logger.info(str(update))
                answer = handler.route(update)

                logger.info('Answer length: {}'.format(len(answer)))
                if len(answer) > 4096:
                    answer = answer[:4000]
                    answer += '[...]'

                try:
                    bot.sendMessage(chat_id=chat_id, text=answer)
                except httplib.IncompleteRead as e:
                    logger.error(e)

                LAST_UPDATE_ID = update_id + 1


if __name__ == '__main__':
    mainloop()
