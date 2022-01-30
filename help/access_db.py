# (c) @AbirHasan2005

from config import Config
from help.database import Database

db = Database(Config.DATABASE_URI, Config.BOT_USERNAME)
