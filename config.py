import os 

TOKEN = os.getenv('TOKEN', '')
WHITELIST = os.getenv('WHITELIST', '').split(',')