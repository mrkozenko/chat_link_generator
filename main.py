import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ChatInviteLink

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /link
@dp.message(Command("link"))
async def link_create(message: types.Message):
    result = await message.bot.create_chat_invite_link(chat_id=message.chat.id, name="PrivacyInviteLink",
                                                                       creates_join_request=True)

    await message.reply(f"{result.invite_link}")


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())