import datetime

now = datetime.datetime.now()


def my_decorator(function_to_decorate):
    def cover_function(*args):
        log_string = ''
        with open('log.txt', 'a', encoding='utf8') as log:
            log_string += f'{now.strftime("%d-%m-%Y %H:%M:%S")} | Имя функции: {function_to_decorate.__name__} | ' \
                      f'Переданные аргументы: {args} | Результат: '
            result_string = str(function_to_decorate(*args))
            log_string += result_string + '\n'
            log.write(log_string)

    return cover_function


@my_decorator
def test_function(*args):
    a = ''
    for i in args:
        a += i

    return a


test_function('Тестовый ввод', 'asdas')





