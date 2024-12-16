def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() #Функция не возвращает вывод текста

inner_function() #Функция выдает ошибку, NameError: name 'inner_function' is not defined

test_function() #Функция работает
