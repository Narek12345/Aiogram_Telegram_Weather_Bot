"""Telegram bot calculator."""

import asyncio
import logging
import requests

from config_reader import config
from aiogram.dispatcher.filters import CommandObject
from aiogram import (
	Dispatcher,
	Bot,
	types,
	html,
)


# Enabling logging so as not to miss important messages.
logging.basicConfig(level=logging.INFO)

# Bot object and data about the city.
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")

# Dispatcher.
dp = Dispatcher()


# Handler on /start command.
@dp.message(commands=['start'])
async def start_command(message: types.Message):
	await message.answer("Hello. I'm a simple bot, which can tell the weather in the city you wrote. To do this, you will need to write the /w command and enter the name of the city. Example: /w Moscow. If you have any questions. then write the command /help.")


# Handler on /help command.
@dp.message(commands=['help'])
async def help_command(message: types.Message):
	await message.answer("Here is our help.")


@dp.message(commands=["w"])
async def cmd_name(message: types.Message, command: CommandObject):
	if command.args:
		name_city = command.args

		# Getting all the data from the server (about the weather) in the city that the user entered.
		getting_all_data_about_city = requests.get("http://api.openweathermap.org/data/2.5/find", params={
			'q': name_city,
			'units': 'metric',
			'APPID': config.weather_token.get_secret_value()
		})

		# Transformation of the received data about the city into json format.
		city_data_in_json_format = getting_all_data_about_city.json()['list']

		# Data analysis and temperature output.
		for city_temperatures in city_data_in_json_format:
			temp_now_city = city_temperatures['main']['temp']
			temp_max_city = city_temperatures['main']['temp_max']
			temp_min_city = city_temperatures['main']['temp_min']

		await message.reply(f"Температура на данный момент: {temp_now_city}\
							\nМаксимальная температура: {temp_max_city}\
							\nМинимальная температура: {temp_min_city}")


	else:
		await message.answer("To do this, you will need to write the /w command and enter the name of the city. Example: /w Moscow.")



# Starting processes polling new updates.
async def main():
	await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())