# Функция обработки строки
def process_string(numbers):
    incorrect_data = 0
    # Обрабатываем строку, просто выводим символы
    for char in numbers:
        print(f'Некорректный тип данных для подсчёта суммы - {char}')
        incorrect_data += 1  # Увеличиваем счетчик некорректных данных
    return 0, incorrect_data  # Возвращаем сумму (0) и количество некорректных данных

def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    # Если передана строка, обрабатываем её отдельно
    if isinstance(numbers, str):
        return process_string(numbers)

    # Обработка остальных типов данных
    for item in numbers:
        try:
            result += float(item)  # Пробуем привести к числу
        except (TypeError, ValueError):
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        # Проверяем, что это коллекция (список или кортеж)
        if not isinstance(numbers, (list, tuple, str)):
            raise TypeError  # Если это не коллекция, выдаем ошибку

        total_sum, incorrect_data = personal_sum(numbers)

        # Вычисляем среднее арифметическое
        valid_count = len(numbers) - incorrect_data
        if valid_count == 0:  # Если все данные некорректные
            return 0
        return total_sum / valid_count

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Смешанные типы
print(f'Результат 3: {calculate_average(567)}')  # Не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректные данные