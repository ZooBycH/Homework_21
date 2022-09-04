from classes.base_storage import BaseStorage
from exceptions import TooManyDifferentProduct


class Shop(BaseStorage):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self,  name: str, amount: int):
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProduct

        super().add(name, amount)



