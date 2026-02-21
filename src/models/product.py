from dataclasses import dataclass , field
import uuid
from datetime import datetime

@dataclass
class Product:
    name : str
    price : float
    stock : int
    id : str = field(default_factory= lambda : str(uuid.uuid4()))
    timestamp : str = field(default_factory= lambda : datetime.now().isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls , data : dict):
        return cls(
            id = data["id"],
            name = data["name"],
            price= data["price"],
            stock = data["stock"],
            timestamp= data["timestamp"]
        )