import unittest
from Serializeble.loader import load_data


class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        # Создаем файл points.txt с данными для тестирования
        with open('points.txt', 'w') as f:
            f.write("user1 10\n")
            f.write("user2 20\n")
            f.write("user3 15\n")
            f.write("user1 30\n")

        # Вызываем функцию load_data() и проверяем результат
        expected_result = [('user1', 30), ('user2', 20), ('user3', 15)]
        self.assertEqual(load_data(), expected_result)

        # Удаляем файл points.txt после выполнения теста
        import os
        os.remove('points.txt')
