import telebot
from telebot import types

# Replace '5344714622:AAFc3YXKuivbCeBmj6baG8S8OyybBYZePz0' with your actual bot token
bot = telebot.TeleBot('5344714622:AAFc3YXKuivbCeBmj6baG8S8OyybBYZePz0')

# Replace 'GROUP_CHAT_ID' with the actual ID of the group where you want to add the usee
group_chat_id = '-4031955217'

@bot.inline_handler(lambda query: True)
def inline_query(query):
    # Create an inline keyboard with a button to trigger the process
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Add Me to Group", switch_inline_query="addme")
    keyboard.add(button)

    # Create an InlineQueryResultArticle to display the button
    results = [types.InlineQueryResultArticle(id='1', title='Add Me to Group', input_message_content=types.InputTextMessageContent(message_text="Click the button to add me to the group."), reply_markup=keyboard)]

    # Answer the inline query with the button
    bot.answer_inline_query(query.id, results)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Check if the message is from the group where you want to add the user
    if message.chat.id == group_chat_id and message.text == "/addme":
        # Extract the user ID from the incoming message
        user_id_to_add = message.from_user.id

        try:
            # Use the add_chat_member_to_chat method to add the user to the group
            bot.add_chat_member_to_chat(chat_id=group_chat_id, user_id=user_id_to_add)
            bot.reply_to(message, "User added to the group successfully!")
        except telebot.apihelper.ApiException as e:
            # Check if the exception is due to the user already being a member
            if "User is already a member of the group" in str(e):
                bot.reply_to(message, "User is already a member of the group.")
            else:
                # Handle other exceptions if needed
                bot.reply_to(message, "An error occurred while adding the user to the group.")

# Run the bot
bot.polling()
