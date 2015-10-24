Archbold
========

Telegram-based server controller inspired by [KarimJedda/whatsappcli](https://github.com/KarimJedda/whatsappcli).

Intended to be a toy PoC. Use at your own risk.

Modification
------------


Usage
-----

```pip install -r requirements.txt```

You need Telegram token for this to work. To generate an Access Token you have to talk to [BotFather](https://telegram.me/botfather) and follow a few simple steps (described [here](https://core.telegram.org/bots#botfather)).

Modify `settings.py` file appropriately.

Run server with,

```python archbold.py```

Authenticated user list resides in `settings.py` file as well. Ask the bot for user id by `/start`.

To implement new commands, look into `events.py`. Some relevant resources are as follows.

- [leandrotoledo/python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot)
- [Welcome to Python Telegram Bot’s documentation! — Python Telegram Bot 2.8.7 documentation](http://python-telegram-bot.readthedocs.org/en/latest/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [All Methods](https://core.telegram.org/methods)
