import logging
import subprocess
from functools import wraps

from settings import ALLOWED_USERS, DEFAULT_RESPONSE, NOT_ALLOWED_RESPONSE


logger = logging.getLogger('archbold_basic')


def auth_required(func):
    @wraps(func)
    def wrapper(update, match):
        user_id = update.message.from_user.id
        if user_id not in ALLOWED_USERS:
            return NOT_ALLOWED_RESPONSE
        return func(update, match)
    return wrapper


# List of events
def start(update, match):
    user_id = update.message.from_user.id
    answer = "You have to be included in the ALLOWED_USERS. Your ID is {}".format(user_id)

    return answer


@auth_required
def exec_command(update, match):
    commands = match.group('exec_command').split(' ')
    # if there is no command, it will return null
    command = commands[0]
    params = commands[1:]

    try:
        answer = subprocess.check_output([command, ' '.join(params)],
                                         stderr=subprocess.STDOUT,
                                         )
    except subprocess.CalledProcessError as e:
        answer = e.output

    logger.debug(answer)
    if not answer.strip():
        answer = DEFAULT_RESPONSE

    return answer


# (event pattern, callback)
events = [
    ("/start", start),
    ("^/exec\s(?P<exec_command>[^$]+)", exec_command),
]
