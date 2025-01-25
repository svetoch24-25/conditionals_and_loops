import unittest
import subprocess

class TestProblem1(unittest.TestCase):
    test_cases = [
        ("admin\n1234", "Доступ разрешён"),
        ("odmin\nqwerty", "Доступ запрещён"),
        ("admin\nwrongpass", "Доступ запрещён"),
        ("admin\n123", "Доступ запрещён")
    ]

    def run_test_case(self, input_data, expected_output):
        # Запускаем problem_1.py с input_data
        process = subprocess.run(
            ["python", "problem_1.py"],  # Файл решения студента
            input=input_data,            # Передача данных через stdin
            text=True,                   # Обработка ввода/вывода как текста
            capture_output=True          # Перехват stdout и stderr
        )

        # Проверяем, что выполнение прошло без ошибок
        self.assertEqual(process.returncode, 0, f"Ошибка выполнения: {process.stderr}")

        # Сравниваем результат выполнения с ожидаемым
        self.assertEqual(process.stdout, expected_output, "Неверный результат!")

    def test_all_cases(self):
        """Запуск всех тест-кейсов"""
        for input_data, expected_output in self.test_cases:
            with self.subTest(input=input_data, output=expected_output):  # Подтест для каждого кейса
                self.run_test_case(input_data, expected_output)

if __name__ == '__main__':
    unittest.main()
