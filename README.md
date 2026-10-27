# Smart Vending Machine CLI

A vending machine simulator for the command line, written in Python. Customers insert money and buy products; an administrator adds and restocks products. The machine keeps a reserve of coins, gives change from it, and saves its state to a JSON file between runs.

## Features

- View products with price and stock
- Insert money, buy a product and get change, or return the inserted money
- Change is calculated from the coins the machine actually has (greedy algorithm); if exact change is impossible, the sale is refused and stock and balance stay unchanged
- Each sale is stored as a transaction with a UUID and a timestamp
- Admin menu to add products and restock them
- Validation for out-of-stock products, insufficient balance, non-positive amounts and empty IDs
- State saved to `data/machine.json` with an atomic write (temporary file, then replace); a damaged file is moved to `machine.backup` and the machine starts fresh
- Unit tests for the service layer with pytest

## Tech stack

- Python 3.13 with data classes
- pytest
- JSON file storage

## Project structure

```text
smart-vending-machine-cli/
├── run.py                       Entry point
├── src/
│   ├── cli/main.py              Menus and input handling
│   ├── models/                  Product, Transaction and MachineState
│   ├── services/vending_service.py   Business rules
│   ├── storage/json_storage.py  Loading and saving the machine state
│   └── utils/change_calculator.py    Change calculation from the coin reserve
├── tests/
│   └── test_vending_machine.py
├── conftest.py                  Lets pytest import the src package from the project root
└── requirements.txt
```

The CLI only handles input and output, `VendingService` holds the rules, and `JSONStorage` is the only part that touches the file system.

## Getting started

```bash
git clone https://github.com/aref9571/smart-vending-machine-cli.git
cd smart-vending-machine-cli
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

The machine starts with an empty product list and ten coins each of 2.00, 1.00, 0.50, 0.20 and 0.10. Products are selected by the first characters of their ID, shown in the product list.

## Running tests

```bash
pytest
```

The tests cover adding, restocking and removing products, inserting money, buying with change, out-of-stock and insufficient-balance errors, a refused sale when change cannot be given, and sales statistics. GitHub Actions runs them on every push to `main`.

## Limitations

- Money is handled as floating-point numbers and rounded to cents; coin values in the reserve are stored in cents.
- Any positive amount can be inserted, not only real coin values.
- Removing products and the sales statistics (`total_sales`, `most_popular_product`) exist in the service layer but are not in the menu yet.
