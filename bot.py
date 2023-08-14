import variables as variables
import functions as functions
from telebot import TeleBot, types

bot = TeleBot(token=variables.token, parse_mode='html')

# кнопки для главного меню
keyboard_main_menu = functions.create_keyboard_main_menu(
    row=1,
    array=variables.status_code_types
)

#обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=functions.create_welcome_msg(message.from_user.username),
        parse_mode='html',
        reply_markup=keyboard_main_menu
    )

#обработчик кнопок главного меню
@bot.message_handler(func=lambda message: functions.is_click_button_main_menu(message, variables.status_code_types))
def click_main_menu(message: types.Message):
    #формируем объект с данными о выбранной группе из объекта STATUS_CODE_TYPES
    status_type = functions.get_status_type(
        text=message.text,
        array=variables.status_code_types
    )

    #формируем строку с текстом ответа, картинку + кнопки для текущего меню на основе объекта status_type
    response = status_type.get("description")
    img = open(status_type.get("img"), 'rb')
    keyboard = functions.create_keyboard_current_menu(
        row=5,
        dictionary=variables.status_codes,
        current_menu=status_type.get("title"),
        btn_back_text=variables.btn_back_to_main_menu_text
    )

    #отправляем результат:
    bot.send_photo(
        chat_id=message.chat.id,
        photo=img,
        caption=response,
        parse_mode='html',
        reply_markup= keyboard
    )
    bot.send_message(
        chat_id=message.chat.id,
        text=variables.current_menu_msg,
        parse_mode='html'
    )

#обработчик кнопки Вернуться в главное меню
@bot.message_handler(func= lambda message: (message.text == variables.btn_back_to_main_menu_text))
def click_btn_back(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=variables.back_to_menu_msg,
        parse_mode='html',
        reply_markup=keyboard_main_menu
    )

#обработчик иных текстовых сообщений
@bot.message_handler(content_types=['text'])
def get_data_status_code(message: types.Message):

    #формируем объект с данными запрашиваемого статус кода из объекта STATUS_CODES
    status_code = variables.status_codes.get(message.text.lower())

    if status_code == None:
        bot.send_message(
            chat_id=message.chat.id,
            text=variables.status_code_is_none_msg
        )
    else:
        #формируем строку с текстом ответа, картинку и кнопки на основе объекта status_code
        response = functions.create_main_response_msg(
            code=message.text,
            data=status_code
        )
        img = open(status_code.get('img'), 'rb')
        key_board = functions.create_keyboard_status_code(
            row=1,
            links=status_code.get('links'),
            buttons_text=variables.btns_for_status_code_response
        )

        #отправляем результат:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption=response,
            parse_mode='html',
            reply_markup= key_board
        )

@bot.message_handler(content_types=['audio', 'document', 'photo', 'sticker', 'video', 'location', 'contact',])
def get_incorrect_format_msg(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=variables.incorrect_format_msg,
        parse_mode='html'
    )

# главная функция программы
def main():
    bot.infinity_polling()

if __name__ == '__main__':
    main()