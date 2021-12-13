from telethon import TelegramClient, sync, events
import time
#from DB import db
# Use your own values from my.telegram.org
api_id = '18305040'
api_hash = 'e360f892de1940d08ff938b5819dffe8'
client = TelegramClient('qwerty', api_id, api_hash)

client.start()

client.send_message('@Mind_gnom_bot', '/start')
time.sleep(1)
client.send_message('@Mind_gnom_bot', '/victorina')
time.sleep(1)
client.send_message('@Mind_gnom_bot', 'География')
time.sleep(1)
client.send_message('@Mind_gnom_bot', 'Либревиль')
time.sleep(1)
client.send_message('@Mind_gnom_bot', 'Молдова')
time.sleep(1)
client.send_message('@Mind_gnom_bot', 'Южного')
time.sleep(1)
client.send_message('@Mind_gnom_bot', 'Г')
time.sleep(1)
client.send_message('@Mind_gnom_bot', 'Антильское')
time.sleep(1)
