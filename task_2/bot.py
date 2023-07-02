import os
import logging
import datetime

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from sheet_api import append_message_info_to_sheet

load_dotenv()
TOKEN = os.getenv('TOKEN')
SHEET_ID = os.getenv('SHEET_ID')
CREDENTIALS_FILE = os.getenv('CREDENTIALS_FILE')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


def setup_for_logging():
    logging.basicConfig(level=logging.ERROR, filename='log.log',
                        format='%(asctime)s %(message)s')


setup_for_logging()


@dp.message_handler()
async def write_message_info_to_google_sheet(message: types.Message):
    login = message.from_user.username
    text = message.text
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    append_message_info_to_sheet(sheet_id=SHEET_ID,
                                 message_info=[login, text, time],
                                 cred_file=CREDENTIALS_FILE)


def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
