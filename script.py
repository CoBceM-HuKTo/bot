#  -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random



tok = '7a88cb60ea583abe541ddbebec7ffcabdbf243cb5718e63c0f89c8d7df6d08409f9f1d90b77a6cbe1894e'



def main():
    vk_session = vk_api.VkApi(token=tok)
    longpoll = VkBotLongPoll(vk_session, 213722560)
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.obj.message['text']
            vk = vk_session.get_api()
            try:
                if 'прив' in message.lower() or 'нача' in message.lower():
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Приветствуем вас в сообществе "Отцы и дети. Мотивационыые встречи." г. Тюмени.'
                                             f'\n\nМеста в зрительном зале ограниченны, поэтому для записи на мероприятие, '
                                             f'просим ввести корректно свои данные в формате: \n"ФИО - телефон - количество'
                                             f' человек которые придут с вами (включая вас)", \n\nНапример:\n\n'
                                             f'Иванов Иван Иванович - 89991234567 - 4\n\n'
                                             f'!!!(Использование тире - обязательно)!!!',
                                    random_id=random.randint(0, 2 ** 64))
                elif len(message.lower().split()) == 7 and ' - ' in message.lower() and '8' in message.lower():
                    f = open('test.txt', 'a', encoding='utf-8')
                    f.write(f'\n{message}')
                    f.close()
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Вот и все, спасибо Вам.\nЗа 1-2 дня мы напомним Вам о мероприятии.\n\n'
                                             f'Поближе ознакомиться с информацией по сообществу "Совет надежных отцов"'
                                             f' по направлению воспитания детей можно перейдя по ссылке:\n'
                                             f'https://vk.com/club213722560'
                                             f'\n\nНапоминаем, что при каждой последущей регистрации на будущее мероприятие Вам нужно будет ввести слово "начать".',
                                     random_id=random.randint(0, 2 ** 64))
                else:
                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message=f'Не понимаю Вас, напишите "начать" или позвоните по т. 89220062243',
                                     random_id=random.randint(0, 2 ** 64))
            except ValueError or KeyError or EOFError or EnvironmentError as error:
                f = open('test.txt', 'a', encoding='utf-8')
                f.write(f'\n{error}')
                f.close()
                vk.messages.send(user_id=event.obj.message['from_id'],
                                 message=f'Не понимаю Вас, напишите "начать" или позвоните по т. 89220062243',
                                 random_id=random.randint(0, 2 ** 64))

if __name__ == '__main__':
    main()


