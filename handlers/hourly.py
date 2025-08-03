from aiogram.types import Message
import aiohttp
from aiogram import Router
from aiogram.filters import Command
import datetime
from db import emojiConditions
router = Router()


@router.message(Command(commands='hourly'))
async def process_hourly(message:Message,weather_api_key:str):
    location:str = message.text.replace('/hourly', '').strip() # type: ignore
    print(location)
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={location}&days=1&aqi=no&alerts=no") as response:
            if response.status == 200:
                data = await response.json()
                hourData = data['forecast']['forecastday'][0]['hour']
                print(hourData)
                answerStr = ''
                for i in hourData:
                    time = datetime.datetime.fromtimestamp(i['time_epoch'])
                    time = time.strftime("%H:%M")

                    answerStr += f'**{time}** {emojiConditions[i['condition']['code']]['day']} {i['temp_c']}°C ({i['chance_of_rain']}% rain)\n'
                print(data)
                await message.answer(answerStr)
            else:
                await message.answer("something went wrong")