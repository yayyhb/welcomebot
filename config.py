import os

BOTNAME = "DoorBitchBot"
TOKEN = os.environ['DOORBITCHBOT_TOKEN']
BOT_ADMIN_USER_IDS = eval('[' + os.environ['WELCOMEBOT_ADMIN_USER_IDS'].replace(':', ', ') + ']')
