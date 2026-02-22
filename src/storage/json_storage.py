import json
from pathlib import Path
from src.models.machine_state import MachineState


class JSONStorage:

    def __init__(self, file_path: str = "data/machine.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def create_default_file(self) -> MachineState:
        state = MachineState(
            products=[],
            transactions=[],
            cash_reserve={
                200: 10,
                100: 10,
                50: 10,
                20: 10,
                10: 10
            }
        )

        self.save_machine(state)
        return state

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
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            return MachineState.from_dict(data)

        except json.JSONDecodeError:
            print("Machine data corrupted. Creating backup and resetting.")
            self.backup_corrupted_file()
            return self.create_default_file()

        except Exception as e:
            raise RuntimeError(f"Failed to load machine state: {e}")

    def save_machine(self, state: MachineState) -> None:

        temp_file = self.file_path.with_suffix(".tmp")

        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(state.to_dict(), f, indent=4, ensure_ascii=False)

            temp_file.replace(self.file_path)

        except Exception as e:
            raise RuntimeError(f"Failed to save machine state: {e}")
