from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "76d284b1f3f335b7b68214c")
      API_ID = int(getenv("API_ID", "33096354"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6564513574:AAGDqUaEmeu0m4DjLDetNc4nooVTWYT7Fzo")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001998534311:-1003067255959").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
