from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "76d284b1f3f335b7b68214c87e25a3f7")
      API_ID = int(getenv("API_ID", "33096354"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6564513574:AAGDqUaEmeu0m4DjLDetNc4nooVTWYT7Fzo")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001998534311:-1003193921476").replace("\n", " ").split(' '))



