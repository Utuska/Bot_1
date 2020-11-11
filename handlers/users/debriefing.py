from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp

from states import Form


@dp.message_handler(Command('form'))
async def start_debriefing(message: types.Message, state: FSMContext):
    await message.answer("Answer a few questions.\n"
                         "Enter your name:")

    await state.set_state('name_step')


@dp.message_handler(state='name_step')
async def set_name(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data({"name": answer})
    await message.answer("Enter your email:")
    await state.set_state('email_step')


@dp.message_handler(state='email_step')
async def set_name(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data({"email": answer})
    await message.answer("Enter your phone:")
    await state.set_state('phone_step')


@dp.message_handler(state='phone_step')
async def set_name(message: types.Message, state: FSMContext):
    answer = message.text
    data = await state.get_data()

    await message.answer(f"Hellow! You entered the following data:\n"
                         f"Name - {data.get('name')}\n"
                         f"Email - {data.get('email')}\n"
                         f"Phone: - {answer}\n")

    await state.finish()

# @dp.message_handler(Command('form'))
# async def start_debriefing(message: types.Message):
#     await message.answer("Answer a few questions.\n"
#                          "Enter your name:"
#                          )
#
#     await Form.name_step.set()
#
#
# @dp.message_handler(state=Form.name_step)
# async def set_name(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     await state.update_data({"name": answer})
#     await message.answer("Enter your email:")
#     await Form.next()
#
#
# @dp.message_handler(state=Form.email_step)
# async def set_email(message: types.Message, state: FSMContext):
#     answer = message.text
#
#     await state.update_data({"email": answer})
#     await message.answer("Enter your phone:")
#     await Form.next()
#
#
# @dp.message_handler(state=Form.phone_step)
# async def set_phone(message: types.Message, state: FSMContext):
#     answer = message.text
#     data = await state.get_data()
#
#     await message.answer(f"Hellow! You entered the following data:\n"
# #                          f"Name - {data.get('name')}\n"
# #                          f"Email - {data.get('email')}\n"
# #                          f"Phone: - {answer}\n")
#     await state.finish()
