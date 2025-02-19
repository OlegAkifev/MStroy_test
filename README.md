ЗАДАНИЕ

Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:
    - getAll() 
        Должен возвращать изначальный массив элементов.
    - getItem(id) 
        Принимает id элемента и возвращает сам объект элемента;
    - getChildren(id) 
        Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента, чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
    - getAllParents(id) 
        Принимает id элемента и возвращает массив из цепочки родительских элементов, начиная от самого элемента, чей id был передан в аргументе и до корневого элемента, т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

Требования: 

    Максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
    в идеале, прямой доступ к элементам без поиска их в массиве.

РЕШЕНИЕ

    - Быстрый доступ по id: Используется словарь id_map, где ключ — это id, а значение — объект. Это позволяет за O(1) получать элемент по id.
    - Группировка по parent: Используется словарь parent_map, где ключ — это parent, а значение — список всех дочерних элементов. Это позволяет быстро находить детей.
    - Метод getAllParents: Для поиска цепочки родителей начинаем с элемента, идем вверх, используя поле parent, и добавляем элементы в список, пока не достигнем корня.

Для корректной работы требуется Python версии 3.11.2

## Установка

1. Клонируйте репозиторий:

    ```
    https://github.com/OlegAkifev/MStroy_test.git
    cd MStroy_test
    ```
2. Создайте виртуальное окружение:

    ```
    virtualenv venv 
    ```
3. Активируйте виртуальное окружение:

    ```
    source venv/bin/activate
    ```
4. Установите зависимостей:

    ```
    pip install -r requirements.txt
    ```

## Запуск

Чтобы запустить скрипт, из корневой папки введите команду:

    ```
    python -m src.tree_store
    ```

## Тестирование 

Чтобы запустить тесты, из корневой папки введите команду:
    ```
    python -m unittest tests.test_tree_store
    ```

