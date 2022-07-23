def get_filename():
    """Запрашивает имя текстового файла."""

    print("\nEnter 'q' to end the program.")
    file_name = input('Enter the text file name: ')
    if file_name == 'q':  # Если, пользователь ввел 'q', то программа завершается;
        quit()
    else:  # Получив имя файла, функция возвращает его и вызывает другую функцию;
        return file_name
        checking_file()


def get_word():  
    """Запрашивает у пользователя слово."""

    word = input('Enter the word: ')
    if word == 'q':  # Если, пользователь ввел 'q', то программа завершается;
        quit()
    else:  # Получив слово, функция возвращает его и вызывает другую функцию;
        return word
        count_words()


def checking_file(): 
    """Проверяет наличие файла в директории."""

    file_name = get_filename()  # Сохраняет возвращенное значение в переменной;
    try:  # Проверка наличия файла
        file_name = file_name + '.txt'  # Добавляет расширение .txt к имени файла;
        with open(file_name) as f:  # Открывает файл;
            f.read()
    except FileNotFoundError:  # Если файла нет в деректории, то выводится сообщение об отсутствии файла;
        print(f"File named '{file_name}' is not found.")
    else:  # Если, файл существует и присутствует в директории, то функция возвращает имя файла;
        return file_name


def count_words():
    """Считает, сколько раз слово встречается в тексте."""

    file_name = checking_file()
    if file_name:  # Проверяет наличие имени файла в переменной;
        word = get_word()
        with open(file_name) as f:  # Открывает файл;
            content = f.read()  # Читает файл и сохраняет его содержимое в переменной;
        word_count = content.lower().count(word)  # Финальный подсчет;
        print(f"\tThe word '{word}' appears {word_count} times in the text.")
    else:
        count_words()


while True:  # Запускает цикл
    count_words()
# Конец
