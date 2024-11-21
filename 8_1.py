def add_everything_up(a, b):
    try:
        if isinstance(a, str) and isinstance(b, str):
            return a + b  # Сложение строк
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b  # Сложение чисел
            # Округление до трех знаков после запятой, если необходимо
            if isinstance(result, float) and len(str(result).split('.')[-1]) > 3:
                return round(result, 3)
            return result  # Возвращаем результат сложения
        else:
            # Если a и b разных типов, возвращаем их строковое представление
            return str(a) + str(b)
    except TypeError:
        return str(a) + str(b)  # На всякий случай, если возникнет TypeError

# Примеры использования
print(add_everything_up(123.456789, 'строка'))  # Вывод: 123.456789строка
print(add_everything_up('яблоко', 4215))         # Вывод: яблоко4215
print(add_everything_up(123.456, 7))              # Вывод: 130.456
print(add_everything_up(1.12345, 2.98765))        # Вывод: 4.111