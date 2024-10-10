#packages
import time
from telebot import TeleBot

#python files:
from keyboards import *
from repository.edits_db import *
from repository.new_edits_db import *
from localization.bot_lang import *
from localization.key_lang import *
from configs.config import Bot_config

#token:
cfg_token = Bot_config().token
token = cfg_token
bot = TeleBot(token)

#dict for lang
user_langs = {}

#-------------------------------------------------------
#start:
#--------------------------------------------------------
@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    chose_lang(message)

#-------------------------------------------------------
#chose lang:
#--------------------------------------------------------
def chose_lang(message):
    chat_id = message.chat.id
    chat_first_name = message.from_user.first_name
    bot.send_message(chat_id, f"𝑯𝒆𝒚 {chat_first_name}👋")
    bot.send_message(chat_id, f"𝑺𝒆𝒍𝒆𝒄𝒕 𝒍𝒂𝒏𝒈𝒖𝒂𝒈𝒆:", reply_markup=generate_localization())
    bot.register_next_step_handler(message, explain)


#-------------------------------------------------------
#explain to catalogs:
#--------------------------------------------------------
def explain(message):
    chat_id = message.chat.id

    lang = user_langs.get(chat_id, 'uz')

    if message.text == "🇺🇿𝑼𝒁𝑩":
        lang = "uz"

    if message.text == "🇺🇸𝑬𝑵𝑮":
        lang = "en"

    if message.text == "🇷🇺𝑹𝑼𝑺":
        lang = "ru"

    bot.send_photo(chat_id, "https://www.google.com/imgres?q=griffith%20eye&imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FM%2FMV5BNDIwZDQ5NzgtOTJmMS00NjA1LWJmMTAtZWQ3NjMzNDI4YjQ2XkEyXkFqcGc%40._V1_.jpg&imgrefurl=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt1259427%2F&docid=Z--ZkgKQvRJA_M&tbnid=3ZcfLMmNgIaKsM&vet=12ahUKEwj4ycGSjb6IAxV7IBAIHeDKF9sQM3oECH0QAA..i&w=2880&h=2160&hcb=2&ved=2ahUKEwj4ycGSjb6IAxV7IBAIHeDKF9sQM3oECH0QAA",
                   caption=lang_explain[lang])
    bot.send_message(chat_id, lang_select_catalog[lang], reply_markup=generate_catalogs(lang))

    user_langs[chat_id] = lang

    bot.register_next_step_handler(message, main_catalogs)




#-------------------------------------------------------
#main catalogs:
#--------------------------------------------------------
def main_catalogs(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, 'uz')

    if message.text == lang_edit_xml_key[lang]:
        bot.send_message(chat_id, lang_edit_style[lang], reply_markup=generate_edit(lang))
        bot.register_next_step_handler(message, edits_pagination)


    if message.text == lang_frezze_key[lang]:
        bot.send_message(chat_id, lang_channels_owner[lang], reply_markup=generate_channel(lang))
        bot.register_next_step_handler(message, channels)


    if message.text == lang_social_key[lang]:
        bot.send_message(chat_id, lang_social_bot[lang], reply_markup=generate_social_media(lang))
        bot.register_next_step_handler(message, social_media)


    if message.text == lang_settings_key[lang]:
        bot.send_message(chat_id, lang_setting[lang], reply_markup=generate_setting(lang))
        bot.register_next_step_handler(message, setting)


    if message.text == lang_back_start_key[lang]:
        return start(message)





#-------------------------------------------------------
#edits and xml:
#--------------------------------------------------------
def edits_pagination(message, edit_id=0, edits=None):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, 'uz')


    if message.text == lang_catalog_pagination_key[lang]:
        return explain(message)

    if message.text == lang_new_edit_key[lang]:
        edits = PostgreSql_new_edit().select_data()

    if message.text == lang_old_edit_key[lang]:
        edits = PostgreSql_edit().select_data()

    if message.text == lang_next_pagination_key[lang] and len(edits) - (edit_id + 1) == 0:
        time.sleep(3)
        bot.send_message(chat_id, lang_kechirasiz[lang])
        return explain(message)




    if message.text == lang_next_pagination_key[lang] and edit_id < len(edits):
        edit_id += 1

    if message.text == lang_back_pagination_key[lang] and edit_id > 0:
        edit_id -= 1

    edit = edits[edit_id]

    edit_title = edit[0]
    edit_url = edit[1]
    edit_xml = edit[2]
    bot.send_video(chat_id, edit_url, caption=edit_title)
    if message.text == "𝘅𝗺𝗹":
        bot.send_message(chat_id, edit_xml)
        bot.delete_message(chat_id, message.id + 1)

    user_message = bot.send_message(chat_id, f"𝗲𝗱𝗶𝘁_𝗶𝗱 : {len(edits) - (edit_id + 1)}", reply_markup=generate_edits_control(lang))

    if message.text == lang_next_pagination_key[lang] and len(edits) - (edit_id + 1) == 0:
        bot.delete_message(chat_id,message.id + 2)
        bot.send_message(chat_id,lang_no_edit[lang], reply_markup=generate_edits_control(lang))
        edit_id = edit_id - len(edits)
    bot.register_next_step_handler(user_message, edits_pagination, edit_id, edits)






# --------------------------------------------------------
# owner channels:
# --------------------------------------------------------
def channels(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, 'uz')


    if message.text == lang_main_chanel_key[lang]:
        bot.send_message(chat_id, 'https://t.me/frezze_edits', reply_markup=generate_channel_back(lang))
        bot.register_next_step_handler(message, channel_back)


    if message.text == lang_material_chanel_key[lang]:
        bot.send_message(chat_id, 'https://t.me/frezzematerials', reply_markup=generate_channel_back(lang))
        bot.register_next_step_handler(message, channel_back)

    if message.text == lang_back_key[lang]:
        bot.send_message(chat_id, lang_select_catalog[lang], reply_markup=generate_catalogs(lang))
        bot.register_next_step_handler(message, main_catalogs)



def channel_back(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, 'uz')

    if message.text == lang_catalog_key[lang]:
        bot.send_message(chat_id, lang_select_catalog[lang], reply_markup=generate_catalogs(lang))
        bot.register_next_step_handler(message, main_catalogs)




#-------------------------------------------------------
#social media:
#--------------------------------------------------------
def social_media(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, 'uz')

    if message.text == '𝗧𝗶𝗸𝘁𝗼𝗸':
        bot.send_message(chat_id, f"{lang_tiktok_bot[lang]} https://www.tiktok.com/@frezzexpp?_t=8qOWvgzLj4q&_r=1")
        bot.send_message(chat_id, lang_social_bot[lang], reply_markup=generate_social_media(lang))
        bot.register_next_step_handler(message, social_media)

    if message.text == '𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺':
        bot.send_message(chat_id, f"{lang_instagram_bot[lang]} https://www.instagram.com/frezze.xpp/profilecard/?igsh=MWhwcWx5ZTJnbmptZA==")
        bot.send_message(chat_id, lang_social_bot[lang], reply_markup=generate_social_media(lang))
        bot.register_next_step_handler(message, social_media)

    if message.text == '𝗬𝗼𝘂𝘁𝘂𝗯𝗲':
        bot.send_message(chat_id, f"{lang_youtube_bot[lang]} https://youtube.com/@frezze_xpp?si=9Ij3Aw89qX5KQj4B")
        bot.send_message(chat_id, lang_social_bot[lang], reply_markup=generate_social_media(lang))
        bot.register_next_step_handler(message, social_media)

    if message.text == lang_back_key[lang]:
        bot.send_message(chat_id, lang_select_catalog[lang], reply_markup=generate_catalogs(lang))
        bot.register_next_step_handler(message, main_catalogs)




#-------------------------------------------------------
#setting:
#--------------------------------------------------------
def setting(message):
    chat_id = message.chat.id
    lang = user_langs.get(chat_id, 'uz')


    if message.text == lang_change_lang_key[lang]:
        bot.send_message(chat_id, f"𝑺𝒆𝒍𝒆𝒄𝒕 𝒍𝒂𝒏𝒈𝒖𝒂𝒈𝒆:", reply_markup=generate_localization())
        bot.register_next_step_handler(message, explain)

    if message.text == lang_bot_reset_key[lang]:
        return start(message)

    if message.text == lang_back_key[lang]:
        bot.send_message(chat_id, lang_select_catalog[lang], reply_markup=generate_catalogs(lang))
        bot.register_next_step_handler(message, main_catalogs)



bot.polling(non_stop=True)