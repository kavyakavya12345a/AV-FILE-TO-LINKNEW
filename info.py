import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# Bot information
SESSION = environ.get('SESSION', 'Webavbot')
API_ID = int(environ.get('API_ID', '22807751'))
API_HASH = environ.get('API_HASH', 'adbbccf8eed67602e3c13f2524272ae6')
BOT_TOKEN = environ.get('BOT_TOKEN', "")
BOT_USERNAME = environ.get("BOT_USERNAME", 'Rnfnejejebot') # without @ 

# Admins, Channels & Users
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", '-1002317605736')) # admin your channel in stream 
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", '-1002298463307')) # admin your channel in users log 
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5694158462').split()] # 3567788, 678899, 5889467
OWNER_USERNAME = environ.get("OWNER_USERNAME", 'mox_by_mox') # without @ 

# pics information
PICS = environ.get('PICS', 'https://envs.sh/dFO.jpg')

# channel link information
CHANNEL = environ.get('CHANNEL', 'https://t.me/es_update')
SUPPORT = environ.get('SUPPORT', 'http://t.me/es_update')

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# ban information
BANNED_CHANNELS = [int(banned_channels) if id_pattern.search(banned_channels) else banned_channels for banned_channels in environ.get('BANNED_CHANNELS', '').split()]   
BAN_CHNL = [int(ban_chal) if id_pattern.search(ban_chal) else ban_chal for ban_chal in environ.get('BAN_CHNL', '').split()]
BAN_ALERT = environ.get('BAN_ALERT' , '<b>ʏᴏᴜʀ ᴀʀᴇ ʙᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.ᴄᴏɴᴛᴀᴄᴛ [ᴀᴠ ᴄʜᴀᴛ ᴏᴡɴᴇʀ](https://telegram.me/AV_OWNER_BOT) ᴛᴏ ʀᴇsᴏʟᴠᴇ ᴛʜᴇ ɪssᴜᴇ!!</b>')

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://godsuraj564:Rb9HKktUHIN5qAnD@cluster0.p5pp1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "godsuraj564")

# fsub  information
AUTH_PICS = environ.get('AUTH_PICS', 'https://envs.sh/0RN.jpg')              
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002329626725"))
FSUB = environ.get("FSUB", False)

# port information
PORT = int(getenv('PORT', '2626'))
NO_PORT = bool(getenv('NO_PORT', False))

#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP

# time information
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))

# Online Stream and Download
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
WORKERS = int(getenv('WORKERS', '4'))
MULTI_CLIENT = False
name = str(environ.get('name', 'avbotz'))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME')) #dont need to fill anything here
else:
    ON_HEROKU = False
FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://environmental-goldia-kavhenfwnfbw-a924b22b.koyeb.app/".format(FQDN)
else:
    URL = "https://environmental-goldia-kavhenfwnfbw-a924b22b.koyeb.app/".format(FQDN)
      
#Dont Remove My Credit @AV_BOTz_UPDATE 
#This Repo Is By @BOT_OWNER26 
# For Any Kind Of Error Ask Us In Support Group @AV_SUPPORT_GROUP
