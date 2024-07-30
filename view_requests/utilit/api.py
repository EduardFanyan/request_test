from utilit.Http_methods import Http_method

"""Метод для тестирования api"""

base_url = 'https://rahulshettyacademy.com'  # Базавая url
key = '?key=qaclick123'  # Параметр для всех запросов


class GoogleMapeApi:
    """Result по основным методам post get put delete"""

    @staticmethod
    def create_new_place():
        """Добавление новой локации"""

        resource_post = '/maps/api/place/add/json'
        body_post = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_url = base_url + resource_post + key  # Url для post метода
        print(f"Url используется-post: {post_url}")

        result_post = Http_method.post(post_url, body_post)  # post запрос
        return result_post

    @staticmethod
    def get_new_place(place_id):  # place_id маячек нашей локаци
        """Проверка result методов по place_id"""

        resource_get = '/maps/api/place/get/json'

        get_url = base_url + resource_get + key + '&place_id=' + place_id  # Url для get метода
        print(f"Url используется-get: {get_url}")

        result_get = Http_method.get(get_url)  # get запрос
        return result_get

    @staticmethod
    def put_new_place(place_id):
        """Изменение result методов по place_id"""

        resource_put = '/maps/api/place/update/json'
        body_put = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_url = base_url + resource_put + key  # Url для put метода
        print(f"Url используется-put: {put_url}")

        result_put = Http_method.put(put_url, body_put)  # put запрос
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Проверка result методов по place_id"""

        resource_delete = '/maps/api/place/delete/json'
        body_delete = {
            "place_id": place_id
        }

        delete_url = base_url + resource_delete + key  # Url для delete метода
        print(f"Url используется-delete: {delete_url}")

        result_delete = Http_method.delete(delete_url, body_delete)  # delete запрос
        return result_delete


