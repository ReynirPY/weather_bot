from dataclasses import dataclass
from environs import Env



@dataclass
class TgBot:
    token:str

@dataclass
class WeatherApi:
    key:str

@dataclass
class Config:
    bot:TgBot
    weatherApi:WeatherApi



def load_config() -> Config:
    env:Env = Env()
    env.read_env()

    return Config(
        bot=TgBot(
            token=env('BOT_TOKEN')
        ),
        weatherApi = WeatherApi(
            key=env('WEATHER_API_KEY')
        )
    ) # type: ignore