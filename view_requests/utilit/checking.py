import json


class ChekingTools:
    """Методы для проверки ответов наших запросов"""

    @staticmethod
    def chek_status_code(result, status_code):
        """Метод для проверки status _code"""
        assert status_code == result.status_code, 'ОШИБКА, Статус-код не совпадает'
        print(f'Успешно! Статус код = {result.status_code}')

    @staticmethod
    def check_json_fields(result, expected_value):
        """Метод для проверки полей"""
        fields = json.loads(result.text)
        assert list(fields) == expected_value, 'ОШИБКА, Список полей не совпадает'
        print(list(fields))
        print('Все поля присутствуют')
