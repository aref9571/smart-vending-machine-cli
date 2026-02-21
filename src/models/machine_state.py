from dataclasses import dataclass, field
from itertools import product

from models import Product
from models import Transaction
from typing import List , Dict
@dataclass
class MachineState:
    products : List[Product] = field(default_factory = list)
    transactions : List[Transaction] = field(default_factory=list)
    cash_reserve : Dict[float , int] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "products" : [p.to_dict() for p in self.products],
            "transactions": [t.to_dict() for t in self.transactions],
            "cash_reserve": self.cash_reserve
        }

    @classmethod
    def from_dict(cls , data : dict):
        products = [Product.from_dict(p) for p in data.get("products",[])]
        transactions = [Transaction.from_dict(t) for t in data.get("transactions" , [])]
        cash = data.get("cash_reserve" , {})

        return cls(
            products=products,
            transactions=transactions,
            cash_reserve=cash

        )