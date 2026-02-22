Smart Vending Machine CLI
A robust, production-style Command Line Interface (CLI) vending machine simulator. This project demonstrates modern software engineering principles, including service-oriented architecture, data persistence, and algorithmic safety.


🌟 Features

Interactive CLI: User-friendly menus for both customers and administrators.
Persistent State: Automatic JSON-based storage ensures machine data survives restarts.
Smart Change Logic: A greedy algorithm-based change calculator that respects the machine's physical coin reserve.
Transaction Logging: Every sale is uniquely identified (UUID) and timestamped for reporting.
Robust Validation: Prevents sales if stock is empty or if the machine cannot provide exact change.
Inventory Management: Admin tools to add, restock, or remove products on the fly.

🏗️ Architecture

The project follows a Clean Architecture approach to ensure a strict separation of concerns:
Models: Data entities (Product, Transaction, MachineState) using Python DataClasses.
Services: The core "brain" (VendingService) containing business rules.
Storage: A persistence layer (JSONStorage) that manages file I/O safely.
Utils: Specialized helper algorithms, such as the change_calculator.

📂 Project Structure

smart-vending-machine-cli/
├── src/
│   ├── cli/                # CLI interface logic
│   ├── models/             # Data structures (Product, Transaction)
│   ├── services/           # Business logic (VendingService)
│   ├── storage/            # Persistence logic (JSONStorage)
│   ├── utils/              # Algorithms (Change calculation)
│   └── main.py             # Internal entry point
├── tests/                  # Unit tests (Pytest)
├── data/                   # JSON database storage
├── run.py                  # Root entry point to launch application
├── requirements.txt        # Project dependencies
└── .gitignore              # Files excluded from version control

🚀 Installation & Setup

Clone the Repository:

git clone https://github.com/aref9571/smart-vending-machine-cli.git
cd smart-vending-machine-cli

