import os
import time
import os
import time
import re
import os
from os import environ
from dotenv import load_dotenv
from pyrogram import Client
import string
import random
import re
import os
from os import environ
from dotenv import load_dotenv
import time, requests

from helper_func.dbhelper import Database as Db
db = Db().setup()

import pyrogram
from pyrogram import Client
import logging
import logging.config

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

LOGGER = logging

botStartTime2 = time.time()
if os.path.exists('config.env'):
    load_dotenv('config.env')

id_pattern = re.compile(r'^.\d+$') 

def is_enabled(value:str):
    return bool(str(value).lower() in ["true", "1", "e", "d"])

def get_config_from_url():
    CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', None)
    try:
        if len(CONFIG_FILE_URL) == 0: raise TypeError
        try:
            res = requests.get(CONFIG_FILE_URL)
            if res.status_code == 200:
                LOGGER.info("Config uzaktan alındı. Status 200.")
                with open('config.env', 'wb+') as f:
                    f.write(res.content)
                    f.close()
            else:
                LOGGER.error(f"Failed to download config.env {res.status_code}")
        except Exception as e:
            LOGGER.error(f"CONFIG_FILE_URL: {e}")
    except TypeError:
        pass

get_config_from_url()
if os.path.exists('config.env'): load_dotenv('config.env')

id_pattern = re.compile(r'^.\d+$')

LOGGER.info("--- CONFIGS STARTS HERE ---")


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")


    # Get from my.telegram.org (or @UseTGXBot)
    API_ID = int(os.environ.get("API_ID", 12345))


    # Get from my.telegram.org (or @UseTGXBot)
    API_HASH = os.environ.get("API_HASH", "")
    
    
    # Database URL from https://cloud.mongodb.com/
    DATABASE_URI = os.environ.get("DATABASE_URI", "")


    # Your database name from mongoDB
    DATABASE_NAME = str(os.environ.get("DATABASE_NAME", "Cluster0"))


    # ID of users that can use the bot commands
    AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())


    # To save user details (Usefull for getting userinfo and total user counts)
    # May reduce filter capacity :(
    # Give yes or no
    SAVE_USER = os.environ.get("SAVE_USER", "no").lower()


    # Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
    # To check dyno status
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")


    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


    # To record start time of bot
    BOT_START_TIME = time.time()
