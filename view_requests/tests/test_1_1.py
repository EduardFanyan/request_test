from utilit.checking import ChekingTools
from utilit.api import GoogleMapeApi
import allure

import json

@allure.epic("Создание новой локации, команды post/get/put/delete")
class TestCreatePlace():

    @allure.description("Запуск тестов")
    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapeApi.create_new_place()  # Создание локации
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        ChekingTools.chek_status_code(result_post, 200)
        ChekingTools.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        print('----', '----', sep='\n')

        print("Метод get post")
        result_get = GoogleMapeApi.get_new_place(place_id)  # Создалась ли локация
        ChekingTools.chek_status_code(result_get, 200)
        ChekingTools.check_json_fields(result_get,
                                       ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                        'language'])
        print('----', '----', sep='\n')

        print("Метод put")
        result_put = GoogleMapeApi.put_new_place(place_id)
        ChekingTools.chek_status_code(result_put, 200)
        ChekingTools.check_json_fields(result_put, ["msg"])
        check_msg = result_put.json()["msg"]
        assert check_msg == 'Address successfully updated', 'Ошибка, текс в msg не совпадает'  # Доп проверка текста сообщения
        print(f'Верный текст в msg {check_msg}')
        print('----', '----', sep='\n')

        print("Метод get put")
        result_get = GoogleMapeApi.get_new_place(place_id)  # отправка метода Get
        ChekingTools.chek_status_code(result_get, 200)
        ChekingTools.check_json_fields(result_get,
                                       ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                        'language'])
        print('----', '----', sep='\n')

        print("Метод delete")
        result_delete = GoogleMapeApi.delete_new_place(place_id)
        ChekingTools.chek_status_code(result_delete, 200)
        ChekingTools.check_json_fields(result_delete, ["status"])
        print('----', '----', sep='\n')

        print('Метод GET delete')
        result_get = GoogleMapeApi.get_new_place(place_id)  # отправка метода Get
        ChekingTools.chek_status_code(result_get, 404)
        ChekingTools.check_json_fields(result_get, ['msg'])
