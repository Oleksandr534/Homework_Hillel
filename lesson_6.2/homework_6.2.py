while True:
    word = input("Введіть слово з літерою 'h': ")
    if 'h' in word.lower():
        print("Слово підходить")
        break
    else:
        print("У слові немає літери 'h'. Спробуйте ще раз.")