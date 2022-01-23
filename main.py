from telethon import TelegramClient, events, Button, errors, functions

from os import getenv

API_KEY = getenv("API_KEY")
API_HASH = getenv("API_HASH")
TOKEN = getenv("TOKEN")
CHANNEL_ID = getenv("CHANNEL_ID")
OWNER_ID = getenv("OWNER_ID")
if CHANNEL_ID:
    CHANNEL_ID = int(CHANNEL_ID)
if OWNER_ID:
    OWNER_ID = int(OWNER_ID)

bot = TelegramClient(None, API_KEY, API_HASH)

bot.start(bot_token=TOKEN)

msg = """
You are not participant of <b>{}</b>.
In order to use this bot your should join the channel <b><a href='t.me/{}'>{}</a></b>

.
"""

USERS = []

@bot.on(events.NewMessage(func=lambda e: e.is_private, pattern="/start"))
async def channel_check(e):
 if e.sender_id != OWNER_ID:
     try:
        chat = await bot.get_entity(CHANNEL_ID)
        p = await bot(functions.channels.GetParticipantRequest(CHANNEL_ID, e.sender_id))
     except errors.UserNotParticipantError:
        return await e.respond(msg.format(chat.title, chat.id, chat.title), buttons=Button.Url("Join Channel", "t.me/{}".format(chat.username)))
     except Exception as err:
        print(err)
 if e.sender_id not in USERS:
    print("New User: ", e.sender_id)
    USERS.append(e.sender_id)
 else:
    pass
 
bot.run_until_disconnected()

# RoseLoverX
