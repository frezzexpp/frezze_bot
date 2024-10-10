from telebot import types
from localization.key_lang import *
def generate_localization():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_uzb = types.KeyboardButton(text="🇺🇿𝑼𝒁𝑩")
    key_eng = types.KeyboardButton(text="🇺🇸𝑬𝑵𝑮")
    key_rus = types.KeyboardButton(text="🇷🇺𝑹𝑼𝑺")
    keyboard.row(key_uzb, key_eng, key_rus)
    return keyboard



def generate_catalogs(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    edits = types.KeyboardButton(text=lang_edit_xml_key[lang])
    owner_channels = types.KeyboardButton(text=lang_frezze_key[lang])
    social_media = types.KeyboardButton(text=lang_social_key[lang])
    settings = types.KeyboardButton(text=lang_settings_key[lang])
    back_main = types.KeyboardButton(text=lang_back_start_key[lang])


    keyboard.row(edits,owner_channels)
    keyboard.row(social_media,settings)
    keyboard.row(back_main)
    return keyboard



def generate_edits_control(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_xml = types.KeyboardButton(text="𝘅𝗺𝗹")
    btn_back = types.KeyboardButton(text=lang_back_pagination_key[lang])
    btn_next = types.KeyboardButton(text=lang_next_pagination_key[lang])
    btn_main = types.KeyboardButton(text=lang_catalog_pagination_key[lang])
    keyboard.row(btn_xml)
    keyboard.row(btn_back, btn_next)
    keyboard.row(btn_main)
    return keyboard




def generate_channel(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_main_channel = types.KeyboardButton(text=lang_main_chanel_key[lang])
    btn_material_channel = types.KeyboardButton(text=lang_material_chanel_key[lang])
    btn_back = types.KeyboardButton(text=lang_back_key[lang])
    keyboard.row(btn_main_channel, btn_material_channel)
    keyboard.row(btn_back)
    return keyboard

def generate_channel_back(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton(text=lang_catalog_key[lang])
    keyboard.row(btn_back)
    return keyboard

def generate_edit(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_old = types.KeyboardButton(text=lang_old_edit_key[lang])
    btn_new = types.KeyboardButton(text=lang_new_edit_key[lang])
    keyboard.row(btn_old, btn_new)
    return keyboard

def generate_social_media(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_tiktok = types.KeyboardButton(text='𝗧𝗶𝗸𝘁𝗼𝗸')
    btn_instagram = types.KeyboardButton(text='𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺')
    btn_youtube = types.KeyboardButton(text='𝗬𝗼𝘂𝘁𝘂𝗯𝗲')
    btn_back = types.KeyboardButton(text=lang_back_key[lang])
    keyboard.row(btn_tiktok, btn_instagram, btn_youtube)
    keyboard.row(btn_back)
    return keyboard

def generate_setting(lang):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_language = types.KeyboardButton(text=lang_change_lang_key[lang])
    btn_reset = types.KeyboardButton(text=lang_bot_reset_key[lang])
    btn_back = types.KeyboardButton(text=lang_back_key[lang])
    keyboard.row(btn_language,btn_reset)
    keyboard.row(btn_back)
    return keyboard