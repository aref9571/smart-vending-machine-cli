import json
from pathlib import Path
from typing import Optional
from models import MachineState

class JSONStorage:
    def __init__(self , file_path = "data/machine.json") :
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True , exist_ok= True)

    def create_default_file(self) -> MachineState:
        default_state = MachineState(
            products=[],
            transactions= [],
            cash_reserve={
                2.0: 10, 1.0: 10, 0.5: 10, 0.2: 10, 0.1: 10
            }
        )

    def backup_corrupted_file(self) -> None:
        backup_path = self.file_path.with_suffix(".backup")

        try:
            if self.file_path.exists():
                self.file_path.replace(backup_path)
        except Exception:
            pass

    def load_machine(self) -> MachineState:
        if not self.file_path.exists():
            return self.create_default_file()

        try:
            with open(self.file_path , 'r' , encoding="utf-8") as f:
                data = json.load(f)

            return MachineState.from_dict(data)
        except json.JSONDecodeError:
            print("Machine data corrupted. creating backup and resetting.")
            self.backup_corrupted_file()
            return self.create_default_file()
        except Exception as e:
            raise RuntimeError(f"Failed to load machine state: {e}")

