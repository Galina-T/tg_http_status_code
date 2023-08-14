from telebot import types

def create_welcome_msg(username):
    return (
        f"Привет, <b>{username}</b>!\n\n"
        f"<i>Напиши свой статус код.</i>\n"
        f"<u>Например: 418</u>\n\n"
        f"<i>Или выбери команду</i> 👇🏻"
    )

def create_main_response_msg(code, data):
    return (
        f"<b>Статус код: {code}</b>\n\n"
        f"<b>Класс:</b> <i>{data.get('type')}</i>\n"
        f"<b>Название:</b> <i>{data.get('name')}</i>\n"
        f"<b>Версия:</b> <i>{data.get('version')}</i>\n\n"
        f"<b>Описание:</b> {data.get('description')}"
    )

def is_click_button_main_menu(message, array):
    for item in array:
        if item.get("title") in message.text:
            return True
    return False

def create_keyboard_main_menu(row, array):
    key_board = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row)
    button_list = [
        types.KeyboardButton(
            f"{status_type.get('note')} "
            f"{status_type.get('title')} "
            f"{status_type.get('icon')}"
        )
        for status_type in array
    ]
    return key_board.add(*button_list)

def create_keyboard_current_menu(row, dictionary, current_menu, btn_back_text):
    current_codes = {key: val for key, val in dictionary.items() if val.get("type") == current_menu}
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row)
    button_list = [types.KeyboardButton(code) for code in current_codes]
    keyboard.add(*button_list)
    keyboard.add(types.KeyboardButton(btn_back_text))
    return keyboard

#доп кнопки для ответа о статус коде
def create_keyboard_status_code(row, links, buttons_text):
    key_board = types.InlineKeyboardMarkup(row_width=row)
    button_list = [
        types.InlineKeyboardButton(
          text = f"{buttons_text.get(key)}",
          url=f"{val}"
        )
        for key, val in links.items()
    ]
    return key_board.add(*button_list)

def get_status_type(text, array):
    for type in array:
        if type.get("title") in text:
            return type