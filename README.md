# Telegram bot.
A simple telegram bot that can tell the weather by the entered city.

## How it works.
The program receives data from the OpenWeatherMap server, processes it and displays the result on the screen.

## How to launch a bot.
To run this bot, you will first need to copy the repository. This is done using the following code:

```
git clone https://github.com/Narek12345/Aiogram_Telegram_Weather_Bot.git
```

Next, you will need to create a .env file and enter your bot token there:

```
BOT_TOKEN = '123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

Then you will need to register on the OpenWeatherMap website and get a token there, which you also need to enter in the .env file. Example:

```
WEATHER_TOKEN = "123456789abcdefgfmweoferfrffr"
```

After all these actions, you will need to install dependencies. They are stored in requirements.txt:

```
pip install -r requirements.txt
```

Finally, everything is ready to launch the project. The main file is bot.py






















