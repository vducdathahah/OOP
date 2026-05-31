
from typing import List
from datetime import datetime, timedelta

class OperatingRoom:

    def __init__(self, room_id: str, name: str, allowed_types: List[str]):
        self.id = room_id
        self.name = name
        self.allowed_types = allowed_types  # Các loại phẫu thuật phòng đáp ứng được [cite: 273]
        self.booked_slots: List[datetime] = []

    def is_available(self, time_slot: datetime) -> bool:
        """Kiểm tra xem phòng có bị trùng lịch trong khoảng 2 tiếng không."""
        for slot in self.booked_slots:
            if abs(slot - time_slot) < timedelta(hours=2):
                return False
        return True

class MedicalSupply:

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity
