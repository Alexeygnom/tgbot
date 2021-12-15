from telethon import TelegramClient, sync, events
import unittest
import time
from DB import db

# Use your own values from my.telegram.org
api_id =
api_hash = ''
client = TelegramClient('qwerty', api_id, api_hash)

client.start()


class tgbot_test(unittest.TestCase):

    def testA(self):
        try:
            # client.send_message('@Mind_gnom_bot', '/start')
            client.send_message('@Mind_gnom_bot', '/start')
            messages = client.get_messages('@Mind_gnom_bot')
            for message in client.get_messages('@Mind_gnom_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Ещё один... \nНу привет, Tumanchik184 \nЯ проверяю твои знания вопросами по следующим темам: география, история, биология, астрономия\nДля того, чтобы начать, напиши\n/victorina'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def testB(self):
        try:
            time.sleep(2)
            client.send_message('@Mind_gnom_bot', '/victorina')
            messages = client.get_messages('@Mind_gnom_bot')
            for message in client.get_messages('@Mind_gnom_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Выбери тему, на вопросы которой хочешь отвечать:'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def testC(self):
        try:
            client.send_message('@Mind_gnom_bot', 'География')
            messages = client.get_messages('@Mind_gnom_bot')
            for message in client.get_messages('@Mind_gnom_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вы выбрали географию'
            self.assertRegex(m, text)

        except:
            self.assertFalse(True)

    def testD(self):
        try:
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Либревиль')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Молдова')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Тихого')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Остров')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Гольфстрим')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '/start')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '/victorina')
            time.sleep(1)

            client.send_message('@Mind_gnom_bot', 'История')
            messages = client.get_messages('@Mind_gnom_bot')
            for message in client.get_messages('@Mind_gnom_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вы выбрали историю, и вот ваш первый в'
            self.assertRegex(m, text)

        except:
            self.assertFalse(True)

    def testE(self):
        try:
            client.send_message('@Mind_gnom_bot', '988')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '1337')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '1939')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '1096')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '476')
            client.send_message('@Mind_gnom_bot', '/start')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '/victorina')
            time.sleep(1)

            client.send_message('@Mind_gnom_bot', 'Биология')
            messages = client.get_messages('@Mind_gnom_bot')
            for message in client.get_messages('@Mind_gnom_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вы выбрали биологию, и вот ваш первый вопрос:'
            self.assertRegex(m, text)

        except:
            self.assertFalse(True)

    def testF(self):
        try:
            client.send_message('@Mind_gnom_bot', 'Не имеют дифференцированных тканей')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Более 30см')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Стрекозы')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Четвертичная')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Глаз')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '/start')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '/victorina')
            time.sleep(1)

            client.send_message('@Mind_gnom_bot', 'Астрономия')
            messages = client.get_messages('@Mind_gnom_bot')
            for message in client.get_messages('@Mind_gnom_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = f'Вы выбрали астрономию, и вот ваш первый вопрос'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def testG(self):
        try:
            client.send_message('@Mind_gnom_bot', 'Гидра')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Венера')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Перигелий')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', 'Новолуние')
            time.sleep(1)
            client.send_message('@Mind_gnom_bot', '2')
            time.sleep(1)
        except:
            self.assertFalse(True)