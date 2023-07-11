from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from lexicon import lexicon
from services.phrases import get_random_phrase


router: Router = Router()


@router.message(CommandStart())
async def process_start(message: Message) -> None:
    await message.answer(lexicon.ANSWERS['greet'])


@router.message()
async def process_any_message(message: Message) -> None:
    await message.answer(get_random_phrase())
