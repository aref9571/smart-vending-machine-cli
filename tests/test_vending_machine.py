import tempfile
import shutil

from src.services.vending_service import VendingService
from src.storage.json_storage import JSONStorage


def create_test_service():

    temp_dir = tempfile.mkdtemp()

    storage = JSONStorage(file_path=f"{temp_dir}/machine.json")

    service = VendingService()
    service.storage = storage
    service.machine = storage.create_default_file()

    return service, temp_dir


def cleanup(temp_dir):
    shutil.rmtree(temp_dir)


def test_add_product():

    service, temp = create_test_service()

    p = service.add_product("Cola", 2.5, 10)

    assert p.name == "Cola"
    assert p.price == 2.5
    assert p.stock == 10

    cleanup(temp)


def test_insert_money():

    service, temp = create_test_service()

    balance = service.insert_money(2)

    assert balance == 2

    cleanup(temp)


def test_buy_product():

    service, temp = create_test_service()

    p = service.add_product("Water", 1.5, 5)

    service.insert_money(2)

    t = service.buy_product(p.id)

    assert t.product_name == "Water"
    assert t.change == 0.5

    cleanup(temp)


def test_out_of_stock():

    service, temp = create_test_service()

    p = service.add_product("Juice", 2, 0)

    service.insert_money(2)

    try:
        service.buy_product(p.id)
        assert False
    except ValueError:
        assert True

    cleanup(temp)


def test_insufficient_balance():

    service, temp = create_test_service()

    p = service.add_product("Snack", 3, 10)

    service.insert_money(1)

    try:
        service.buy_product(p.id)
        assert False
    except ValueError:
        assert True

    cleanup(temp)


def test_restock():

    service, temp = create_test_service()

    p = service.add_product("Tea", 2, 1)

    service.restock_product(p.id, 5)

    assert service.get_product(p.id).stock == 6

    cleanup(temp)


def test_remove_product():

    service, temp = create_test_service()

    p = service.add_product("Cookie", 1, 5)

    removed = service.remove_product(p.id)

    assert removed
    assert service.get_product(p.id) is None

    cleanup(temp)


def test_total_sales():

    service, temp = create_test_service()

    p = service.add_product("Coffee", 2, 10)

    service.insert_money(2)
    service.buy_product(p.id)

    assert service.total_sales() == 2

    cleanup(temp)


def test_transaction_count():

    service, temp = create_test_service()

    p = service.add_product("Latte", 3, 10)

    service.insert_money(3)
    service.buy_product(p.id)

    assert service.total_transactions() == 1

    cleanup(temp)
