from aiogram.filters import Command
from aiogram.types import Message
from aiohttp import ClientSession
from db import users, emojiConditions
from aiogram import Router

router = Router()

@router.message()
async def process_current(message:Message, weather_api_key:str):

    if len(message.text) > 50: # type: ignore
        await message.answer(text='your message is out of length range')
        return
    elif message.text.isdigit(): # type: ignore
        await message.answer(text='location name cant be a number')
        return

    async with ClientSession() as session:
        async with session.get(f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={message.text}&aqi=no') as response:
            print('Status', response.status)
            print(message.text)
            if response.status == 200:
                data = await response.json()
                #print(data)
                condition_code:int = data['current']['condition']['code']
                answer_sting:str =f'🌤️**Current Weather in {data['location']['name']}, {data['location']['country']}**\n\n'

                if users[message.from_user.id]['celsiusOrFahrenheit']: # type: ignore
                    answer_sting+=f'🌡️**{data['current']['temp_c']}°C** (feels like {data['current']['feelslike_c']}°C)\n\n '
                else:
                    answer_sting+=f'🌡️**{data['current']['temp_f']}°F** (feels like {data['current']['feelslike_f']}°F)\n\n'

                if data['current']['is_day']:
                    answer_sting+=f'{emojiConditions[condition_code]['day']}'
                else:
                    answer_sting+=f'{emojiConditions[condition_code]['night']}'

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