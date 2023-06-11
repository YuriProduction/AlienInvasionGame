import unittest
import os
from Serializeble.saver import save_data

class TestSaveData(unittest.TestCase):
    def test_save_data(self):
        # Вызываем функцию save_data() и проверяем, что файл points.txt создан и содержит правильные данные
        save_data(10, 'user1')
        save_data(20, 'user2')
        save_data(15, 'user3')
        expected_result = "user1 10\nuser2 20\nuser3 15\n"
        with open('points.txt', 'r') as f:
            self.assertEqual(f.read(), expected_result)

        # Удаляем файл points.txt после выполнения теста
        os.remove('points.txt')


