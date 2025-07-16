from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiohttp import ClientSession
import os
#import dotenv

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

WEATHER_API_KEY = env('WEATHER_API_KEY')

users: dict[int, dict[str, bool]] = {}

bot = Bot(token=BOT_TOKEN) # type: ignore
dp = Dispatcher()

@dp.message(CommandStart())
async def process_start(message:Message):
    if message.from_user.id not in users: # type: ignore
        users[message.from_user.id ] = { # type: ignore
            'celsiusOrFahrenheit':True, #when True bot shows in celsius if False in Fahrenheit
            'kilolometersOrMiles':True  #when True bot shows in kilometers if Fasle in Miles
        }
        print(users)

    await message.answer(f"🌤️ Welcome to WeatherWise Bot! 🌤️\nHi {message.from_user.first_name} I'm your personal weather assistant, ready to help you stay informed about the weather anywhere in the world.\n Press /help to see how work with bot") # type: ignore

@dp.message(Command(commands='change_temperature_units'))
async def change_temperatue_units(message:Message):
    users[message.from_user.id]['celsiusOrFahrenheit'] =  not  users[message.from_user.id]['celsiusOrFahrenheit'] # type: ignore

    if users[message.from_user.id]['celsiusOrFahrenheit']: # type: ignore
        await message.answer('now temperature units is celsius')
    else:
        await message.answer('now temperature units is fahrenheit')

@dp.message(Command(commands='change_measure_units'))
async def change_measure_units(message:Message):
    users[message.from_user.id]['kilolometersOrMiles'] =  not  users[message.from_user.id]['kilolometersOrMiles'] # type: ignore

    if users[message.from_user.id]['kilolometersOrMiles']: # type: ignore
        await message.answer('now measure units are kilometers')
    else:
        await message.answer('now measure units are miles')

@dp.message()
async def process_current(message:Message):
    async with ClientSession() as session:
        async with session.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={message.text}&aqi=no') as response:
            print('Status', response.status)
            print(message.text)
            if response.status == 200:
                data = await response.json()
                #print(data)
                answer_sting:str =f'🌤️**Current Weather in {data['location']['name']}, {data['location']['country']}**\n\n'

                if users[message.from_user.id]['celsiusOrFahrenheit']: # type: ignore
                    answer_sting+=f'🌡️**{data['current']['temp_c']}°C** (feels like {data['current']['feelslike_c']}°C)\n\n '
                else:
                    answer_sting+=f'🌡️**{data['current']['temp_f']}°F** (feels like {data['current']['feelslike_f']}°F)\n\n'

                answer_sting += f'{data['current']['condition']['text']}\n\n💧 Humidity: {data['current']['humidity']}%\n'

                if users[message.from_user.id]['kilolometersOrMiles']: # type: ignore
                    answer_sting += f'🌬️ Wind: {data['current']['wind_kph']} km/h {data['current']['wind_dir']}\n👁️ Visibility: {data['current']['vis_km']} km'
                else:
                    answer_sting += f'🌬️ Wind: {data['current']['wind_mph']} m/h {data['current']['wind_dir']}\n👁️ Visibility: {data['current']['vis_miles']} m'

                await message.answer(answer_sting)
            elif response.status == 400:
                await message.answer('❌ City not found. Please check the spelling and try again.')
            elif response.status == 401:
                await message.answer('❌ Weather service temporarily unavailable.')
            else:
                await message.answer(f'❌ Error: {response.status}')


dp.run_polling(bot)