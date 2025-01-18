class TreeStore:
    def __init__(self, items):
        self.items = items
        # Словарь для быстрого доступа к элементам по id
        self.id_map = {item["id"]: item for item in items}
        # Словарь для группировки элементов по parent
        self.parent_map = {}
        for item in items:
            parent = item["parent"]
            if parent not in self.parent_map:
                self.parent_map[parent] = []
            self.parent_map[parent].append(item)

    def getAll(self):
        """Возвращает изначальный массив элементов."""
        return self.items

    def getItem(self, id):
        """Возвращает объект элемента по его id."""
        return self.id_map.get(id)

    def getChildren(self, id):
        """Возвращает массив дочерних элементов для заданного id."""
        return self.parent_map.get(id, [])

    def getAllParents(self, id):
        """Возвращает цепочку родительских элементов от заданного id до корневого элемента."""
        parents = []
        current_item = self.getItem(id)
        while current_item and current_item["parent"] != "root":
            parent_id = current_item["parent"]
            current_item = self.getItem(parent_id)
            if current_item:
                parents.append(current_item)
        return parents
    
