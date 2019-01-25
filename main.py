import datetime

now = datetime.datetime.now()


def decorator_maker(path):
    def my_decorator(function_to_decorate):
        def cover_function(*args, **kwargs):
            log_string = ''
            with open(path, 'a', encoding='utf8') as log:
                log_string += f'{now.strftime("%d-%m-%Y %H:%M:%S")} | Имя функции: {function_to_decorate.__name__} | ' \
                          f'Переданные аргументы: {args} {kwargs} | Результат: \n'
                result_string = function_to_decorate(*args, **kwargs)
                log_string += result_string + '\n'
                log.write(log_string)
        return cover_function

    return my_decorator


@decorator_maker('log.txt')
def adv_print(*args, start='', max_line=0, in_file=False):
    result = str(start)
    result_sep = ''
    for value in args:
        result += str(value)

    if max_line > 0 and len(result) > max_line:
        for symbol in range(0, len(result), max_line):
            result_sep += result[symbol:symbol + max_line] + '\n'
        result = result_sep

    if in_file:
        with open('result.txt', 'w', encoding='utf8') as file:
            file.write(result)
        return result
    else:
        return result


adv_print(31153, '1111111111', start='*', max_line=5, in_file=True)





