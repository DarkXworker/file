✘ This Specially For Who Want To Store FIles.

✘ Just Send Me Your File/Text/Media And Get Your Shareable Link.""",reply_markup=markupJ,parse_mode='HTML')
    else:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("✘ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url='http://t.me/Aizamods')
        item2 = types.InlineKeyboardButton("✅ Jᴏɪɴᴇᴅ",callback_data='join')
        markup.add(item1, item2)
        bot.send_photo(user_id,photo='https://t.me/Bots_Pay_Alert/941',caption=f"""<b>👋 Hey !!!

👉 You Need To Join Our Channel To Use This Bot. </b>️""", reply_markup=markup,parse_mode='HTML')
        return 
@bot.message_handler(commands=['broadcast'])
def handle_broadcast_command(message):
    if message.chat.id != 5417870023:
        return
    else:
        msg = bot.send_message(message.chat.id, f"""<b>Pʟᴇᴀsᴇ Eɴᴛᴇʀ Tʜᴇ Mᴇssᴀɢᴇ Yᴏᴜ Wᴀɴᴛ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ:- 👇👇👇</b>""",parse_mode='HTML')
        bot.register_next_step_handler(msg, handle_broadcast_message)
def handle_broadcast_message(message):
    chat_id = message.chat.id
    broadcast_message = message.text
    user_list = get_data(f"{bot_id}-user_id.json")
    if user_list is None:
        bot.send_message(chat_id, "Error: User list not found.")
        return
    total_users = len(user_list)
    total_success = 0
    total_fail = 0
    for user_id in user_list:
        try:
            bot.copy_message(chat_id=user_id, from_chat_id=chat_id, message_id=message.message_id)
            total_success += 1
        except Exception as e:
            total_fail += 1
    success_emoji = u'\U0001F60E'
    fail_emoji = u'\U0001F622'
    response_message = f"Bʀᴏᴀᴅᴄᴀsᴛ Sᴜᴍᴍᴀʀʏ 👇👇👇\n\n"
    response_message += f"Tᴏᴛᴀʟ Usᴇʀs: {total_users}\n"
    response_message += f"Tᴏᴛᴀʟ Sᴜᴄᴄᴇss: {total_success} {success_emoji}\n"
    response_message += f"Tᴏᴛᴀʟ Fᴀɪʟᴇᴅ: {total_fail} {fail_emoji}\n"
    bot.send_message(chat_id, response_message)              
bot.infinity_polling()
