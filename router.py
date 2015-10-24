import re

from events import events
from settings import DEFAULT_RESPONSE


class EventHandler(object):
    def __init__(self):
        self.events = [(re.compile(pattern), callback) for pattern, callback in events]

    def route(self, update):
        msg = update.message.text
        for event, callback in self.events:
            match = event.match(msg)
            if match:
                answer = callback(update, match)
                if answer:
                    return answer
            return DEFAULT_RESPONSE
