from aiogram.types import  Message
import aiohttp
from aiogram import Router
from aiogram.filters import Command
from db import users, emojiConditions
import datetime

router:Router = Router()

@router.message(Command(commands='forecast'))
async def procees_forecast(message:Message, weather_api_key:str):
    city:str = message.text.replace('/forecast', '').strip() # type: ignore
    print(city)
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={city}&days=5&aqi=no&alerts=no') as response:
            if response.status == 200:
                data = await response.json()
                answer_string:str = f'📅**5-Day Forecast for {data['location']['name']}, {data['location']['country']}**\n\n'


                for index, day in enumerate(data['forecast']['forecastday']):
                    epoch_time = day['date_epoch']
                    dt = datetime.datetime.fromtimestamp(epoch_time)

                    number = dt.day
                    month = dt.strftime("%b")

                    condition_code:int  = day['day']['condition']['code']
                    print(epoch_time)
                    if index == 0:
                        answer_string += f'**Today** ({month} {number})\n'
                    elif index == 1:
                        answer_string += f'**Tommorow** ({month} {number})\n'
                    else:
                        day_of_week = dt.strftime("%A")
                        answer_string += f'**{day_of_week}** ({month} {number})\n'


                    if users[message.from_user.id]['celsiusOrFahrenheit']:
                        answer_string +=f'{emojiConditions[condition_code]['day']} {day['day']['maxtemp_c']}°C / {day['day']['mintemp_c']}°C - {day['day']['condition']['text']}\n\n'
                    else:
                        answer_string +=f'{emojiConditions[condition_code]['day']} {day['day']['maxtemp_f']}°F / {day['day']['mintemp_f']}°F - {day['day']['condition']['text']}\n\n'

                await message.answer(text=answer_string)
