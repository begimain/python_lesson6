array = [1, 2, 4, 5, 6, 'string', [1, 2], 1.3]




if __name__ == '__main__':
    array.append('Hello')  # Метод добавляет элемент в конце списка
    array.extend([[8, 9, 10]])  # Метод добавляет все элементы итератора в конце списка
    array.insert(3, 'World')  # Метод вставляет элемент в список по указанному индексу.
    array.remove(6)  # Метод удаляет первый соответствующий элемент из списка
    array.pop(5)  # Метод удаляет элемент с заданным индексом из списка
    array.index(2)  # Метод возвращает индекс указанного элемента в списке.
    array.count(1.3)  # Метод возвращает указанного элемента в списке
    array.reverse()
    array.copy()  # Метод возвращает неполную копию списка.
    array.clear()  # Метод очищает список
    print(array.clear)
    print('copied list:', array)
    print(reversed, array)  # Метод Разварачивает список
    print(sorted, array)  # Метод Сортирует список
    # print(array.index(2))
    print(array.count(1.3))



