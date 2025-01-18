from typing import Any, Dict, List, Optional, Union

class TreeStore:
    def __init__(self, items: List[Dict[str, Any]]):
        self.items: List[Dict[str, Any]] = items
        # Словарь для быстрого доступа к элементам по id
        self.id_map: Dict[int, Dict[str, Any]] = {item["id"]: item for item in items}
        # Словарь для группировки элементов по parent
        self.parent_map: Dict[Union[int, str], List[Dict[str, Any]]] = {}
        for item in items:
            parent = item["parent"]
            if parent not in self.parent_map:
                self.parent_map[parent] = []
            self.parent_map[parent].append(item)

    def getAll(self) -> List[Dict[str, Any]]:
        """Возвращает изначальный массив элементов."""
        return self.items

    def getItem(self, id: int) -> Optional[Dict[str, Any]]:
        """Возвращает объект элемента по его id."""
        return self.id_map.get(id)

    def getChildren(self, id: int) -> List[Dict[str, Any]]:
        """Возвращает массив дочерних элементов для заданного id."""
        return self.parent_map.get(id, [])

    def getAllParents(self, id: int) -> List[Dict[str, Any]]:
        """Возвращает цепочку родительских элементов от заданного id до корневого элемента."""
        parents: List[Dict[str, Any]] = []
        current_item = self.getItem(id)
        while current_item and current_item["parent"] != "root":
            parent_id = current_item["parent"]
            current_item = self.getItem(parent_id)
            if current_item:
                parents.append(current_item)
        return parents

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)
print(ts.getAll())
print(ts.getItem(7))
print(ts.getChildren(4))
print(ts.getChildren(5))
print(ts.getAllParents(7))