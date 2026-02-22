from dataclasses import dataclass, field
from datetime import datetime , UTC
import uuid


@dataclass
class Transaction:
    product_id: str
    product_name: str
    price: float
    paid: float
    change: float
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Invalid price")

        if self.paid < 0:
            raise ValueError("Invalid payment")

        if self.change < 0:
            raise ValueError("Invalid change")

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
            price=float(data["price"]),
            paid=float(data["paid"]),
            change=float(data["change"]),
            timestamp=data["timestamp"]
        )
