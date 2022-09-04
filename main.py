from classes.courier import Courier
from classes.request import Request
from classes.shop import Shop
from classes.store import Store
from exceptions import InvalidRequest, BaseError, InvalidStorageName

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "коробка": 25
})

shop = Shop(items={
    "печенька": 2,
    "собачка": 2,
    "коробка": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print("\nДобрый день\n")

    while True:

        """Вывести все товары во всех хранилищах"""
        for storage_name in storages:
            print(f"Сейчас в {storage_name}:\n {storages[storage_name].get_items()}")

        user_input = input(
            "Введите запрос в формате: 'Доставить 3 печеньки из склад в магазин'\n"
            "Введите 'стоп' или 'stop', если хотите закончить:\n"
        )
        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request=user_input, storages=storages)

        except BaseError as e:
            print(e.message)
            continue

        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as e:
            print(e.message)
            courier.cancel()


if __name__ == "__main__":
    main()
