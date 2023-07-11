from dotenv import load_dotenv
from dataclasses import dataclass
import os


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    bot: TgBot


def load_config() -> Config:
    if os.path.exists('.env'):
        load_dotenv()
    token = os.environ['BOT_TOKEN']
    return Config(bot=TgBot(token=token))