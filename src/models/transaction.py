from dataclasses import dataclass , field
from datetime import datetime
import uuid
from itertools import product


@dataclass
class Transaction:
    product_id: str
    product_name : str
    price : float
    paid : float
    change : float
    id : str = field(default_factory= lambda: str(uuid.uuid4()))
    timestamp : str = field(default_factory= lambda : datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "product_id": self.product_id,
            "product_name": self.product_name,
            "price": self.price,
            "paid": self.paid,
            "change": self.change,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            product_id=data["product_id"],
            product_name=data["product_name"],
            price=data["price"],
            paid=data["paid"],
            change=data["change"],
            timestamp=data["timestamp"]
        )