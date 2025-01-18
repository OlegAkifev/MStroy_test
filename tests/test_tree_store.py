import unittest
from src.tree_store import TreeStore


class TestTreeStore(unittest.TestCase):
    def setUp(self):
        """
        Подготавливаем тестовые данные, представляющие собой элементы дерева
        """
        self.items = [
            {"id": 1, "parent": "root"},
            {"id": 2, "parent": 1, "type": "test"},
            {"id": 3, "parent": 1, "type": "test"},
            {"id": 4, "parent": 2, "type": "test"},
            {"id": 5, "parent": 2, "type": "test"},
            {"id": 6, "parent": 2, "type": "test"},
            {"id": 7, "parent": 4, "type": None},
            {"id": 8, "parent": 4, "type": None}
        ]
        """
        Создаем объект TreeStore с данными
        """
        self.tree_store = TreeStore(self.items)

    def test_get_all(self):
        """
        Проверяем, что метод getAll возвращает все элементы
        """
        self.assertEqual(self.tree_store.getAll(), self.items)

    def test_get_item_existing(self):
        """
        Проверяем получение элемента по существующему id
        """
        self.assertEqual(self.tree_store.getItem(7), {"id": 7, "parent": 4, "type": None})

    def test_get_item_non_existing(self):
        """
        Проверяем получение элемента по несуществующему id
        """
        self.assertIsNone(self.tree_store.getItem(999))

    def test_get_children_existing(self):
        """
        Проверяем получение дочерних элементов для существующего элемента
        """
        self.assertEqual(
            self.tree_store.getChildren(4),
            [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}]
        )

    def test_get_children_non_existing(self):
        """
        Проверяем получение дочерних элементов для несуществующего элемента
        """
        self.assertEqual(self.tree_store.getChildren(999), [])

    def test_get_children_no_children(self):
        """
        Проверяем, что для элемента без дочерних элементов метод вернет пустой список
        """
        self.assertEqual(self.tree_store.getChildren(5), [])

    def test_get_all_parents_existing(self):
        """
        Проверяем получение всех родителей для существующего элемента
        """
        self.assertEqual(
            self.tree_store.getAllParents(7),
            [
                {"id": 4, "parent": 2, "type": "test"},
                {"id": 2, "parent": 1, "type": "test"},
                {"id": 1, "parent": "root"}
            ]
        )

    def test_get_all_parents_non_existing(self):
        """
        Проверяем получение родителей для несуществующего элемента
        """
        self.assertEqual(self.tree_store.getAllParents(999), [])

    def test_get_all_parents_root(self):
        """
        Проверяем, что для корня (id == 1) родителей нет
        """
        self.assertEqual(self.tree_store.getAllParents(1), [])

    def test_empty_tree(self):
        """
        Проверяем поведение пустого дерева
        """
        empty_tree_store = TreeStore([])
        self.assertEqual(empty_tree_store.getAll(), [])  # Нет элементов
        self.assertIsNone(empty_tree_store.getItem(1))  # Элемент с id 1 не существует
        self.assertEqual(empty_tree_store.getChildren(1), [])  # У элемента с id 1 нет детей
        self.assertEqual(empty_tree_store.getAllParents(1), [])  # У элемента с id 1 нет родителей

    def test_missing_parent_field(self):
        """
        Проверяем, что происходит при отсутствии поля 'parent' в элементе
        """
        invalid_items = [
            {"id": 1, "parent": "root"},
            {"id": 2, "type": "test"}  # Отсутствует 'parent'
        ]
        with self.assertRaises(KeyError):  # Ожидаем ошибку KeyError
            TreeStore(invalid_items)

    def test_missing_id_field(self):
        """
        Проверяем, что происходит при отсутствии поля 'id' в элементе
        """
        invalid_items = [
            {"id": 1, "parent": "root"},
            {"parent": 1, "type": "test"}  # Отсутствует 'id'
        ]
        with self.assertRaises(KeyError):  # Ожидаем ошибку KeyError
            TreeStore(invalid_items)


if __name__ == "__main__":
    unittest.main()
