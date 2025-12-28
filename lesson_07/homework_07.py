# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_number (a, b):
    return a+b

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average(numbers):
    return sum(numbers) / len(numbers)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse(text):
    return text[::-1]

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    return max(words, key=len)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
     return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def find_second_occurrence(text: str, word: str) -> int:
    """
    Повертає індекс другого входження слова у тексті.
    Якщо слово зустрічається менше двох разів — повертає -1.
    """
    words = text.split()

    if words.count(word) < 2:
        return -1

    first_index = words.index(word)
    second_index = words.index(word, first_index + 1)
    return second_index

# task 8
def split_into_sentences(text: str) -> list:
    """
    Розбиває текст на список речень за крапкою.
    """
    return text.split(".")

# task 9
def get_fourth_sentence_lower(sentences: list) -> str | None:
    """
    Повертає четверте речення у нижньому регістрі.
    Якщо речень менше чотирьох — повертає None.
    """
    if len(sentences) < 4:
        return None

    return sentences[3].lower()

# task 10
def contains_sentence_starting_with(text: str, phrase: str) -> bool:
    """
    Перевіряє, чи містить текст речення, що починається з заданої фрази.
    """
    sentences = text.split(".")

    for sentence in sentences:
        if sentence.strip().startswith(phrase):
            return True

    return False

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""