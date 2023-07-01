import datetime
import os
import logging

from aiogram import Bot, Dispatcher, executor, types
from task_2.sheet_api import append_message_info_to_sheet
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('TOKEN')
sheet_id = os.environ.get('SHEET_ID')
CREDENTIALS_FILE = os.environ.get('CREDENTIALS_FILE')

bot = Bot(token=token)
dp = Dispatcher(bot=bot)

logging.basicConfig(level=logging.ERROR, filename='log.log',
                    format='%(asctime)s %(message)s')


@dp.message_handler()
async def write_message_info_to_google_sheet(message: types.Message):
    author = message.from_user.full_name
    text = message.text
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    append_message_info_to_sheet(sheet_id=sheet_id, message_info=[author, text, time],
                                 cred_file=CREDENTIALS_FILE)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
