from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router
from db import users

router = Router()


@router.message(CommandStart())
async def process_start(message:Message):
    if message.from_user.id not in users: # type: ignore
        users[message.from_user.id ] = { # type: ignore
            'celsiusOrFahrenheit':True, #when True bot shows in celsius if False in Fahrenheit
            'kilolometersOrMiles':True  #when True bot shows in kilometers if Fasle in Miles
        }
        print(users)

    await message.answer(f"🌤️ Welcome to WeatherWise Bot! 🌤️\nHi {message.from_user.first_name} I'm your personal weather assistant, ready to help you stay informed about the weather anywhere in the world.\n Press /help to see how work with bot") # type: ignore

@router.message(Command(commands='help'))
async def  process_help(message:Message):
    await message.answer(text='Write me a place location  and i will show you current weather there\n\n/change_temperature_units to switch celsius and fahrenheit\n/change_measure_units to switch between kilometers and miles\nother features in developing process')


@router.message(Command(commands='change_temperature_units'))
async def change_temperatue_units(message:Message):
    users[message.from_user.id]['celsiusOrFahrenheit'] =  not  users[message.from_user.id]['celsiusOrFahrenheit'] # type: ignore

    if users[message.from_user.id]['celsiusOrFahrenheit']: # type: ignore
        await message.answer('now temperature units is celsius')
    else:
        await message.answer('now temperature units is fahrenheit')

@router.message(Command(commands='change_measure_units'))
async def change_measure_units(message:Message):
    users[message.from_user.id]['kilolometersOrMiles'] =  not  users[message.from_user.id]['kilolometersOrMiles'] # type: ignore

    if users[message.from_user.id]['kilolometersOrMiles']: # type: ignore
        await message.answer('now measure units are kilometers')
    else:
        await message.answer('now measure units are miles')