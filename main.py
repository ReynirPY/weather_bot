from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiohttp import ClientSession

BOT_TOKEN = ''

WEATHER_API_KEY = ''

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def process_start(message:Message):
    await message.answer(f"🌤️ Welcome to WeatherWise Bot! 🌤️\nHi {message.from_user.first_name} I'm your personal weather assistant, ready to help you stay informed about the weather anywhere in the world.") # type: ignore

@dp.message()
async def process_current(message:Message):
    async with ClientSession() as session:
        async with session.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={message.text}&aqi=no') as response:
            print('Status', response.status)
            print(message.text)
            if response.status == 200:
                data = await response.json()
                #print(data)
                await message.answer(f"🌤️**Current Weather in {data['location']['name']}, {data['location']['country']}**\n\n🌡️**{data['current']['temp_c']}°C** (feels like {data['current']['feelslike_c']}°C)\n\n {data['current']['condition']['text']}\n\n💧 Humidity: {data['current']['humidity']}%\n🌬️ Wind: {data['current']['wind_kph']} km/h {data['current']['wind_dir']}\n👁️ Visibility: {data['current']['vis_km']} km")


dp.run_polling(bot)