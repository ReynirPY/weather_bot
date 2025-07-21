from aiogram import Bot, Dispatcher

from handlers import user, current

from config import Config, load_config
import asyncio
#import dotenv
async def main():
    config: Config = load_config()
    BOT_TOKEN = config.bot.token
    WEATHER_API_KEY = config.weatherApi.key



    bot = Bot(token=BOT_TOKEN) # type: ignore
    dp = Dispatcher()

    dp['weather_api_key'] = WEATHER_API_KEY

    dp.include_router(user.router)
    dp.include_router(current.router)





    await dp.start_polling(bot)

asyncio.run(main())