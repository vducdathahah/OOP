
from typing import List, Dict, Optional
from datetime import datetime
from app.models.person import Patient, Person
from app.models.room_supply import OperatingRoom
from app.states.surgery_state import SurgeryState, PendingState

class Surgery:

    def __init__(self, surgery_id: str, patient: Patient, surgery_type: str, priority: str, required_supplies: Dict[str, int]):
        self.id = surgery_id
        self.patient = patient               # 
        self.type = surgery_type             # Loại phẫu thuật (Ví dụ: Tim mạch, Chấn thương) [cite: 273]
        self.priority = priority             # Khẩn cấp hoặc Thường [cite: 273]
        self.required_supplies = required_supplies
        
        self.room: Optional[OperatingRoom] = None  # 
        self.start_time: Optional[datetime] = None # 
        self.team: List[Person] = []               # Đội ngũ y tế phối hợp [cite: 274, 278, 281]
        self.post_op_orders: List[str] = []        # Danh sách y lệnh [cite: 275, 276]
        self._state: SurgeryState = PendingState() # Trạng thái khởi tạo mặc định 

    def set_state(self, state: SurgeryState) -> None:
        print(f"[Ca mổ {self.id}] Đổi trạng thái: {self._state} -> {state}")
        self._state = state

    def get_status(self) -> str:
        return str(self._state)

    def advance_stage(self) -> None:
      
        self._state.next(self)

    def assign_staff(self, staff: Person) -> None:
   
        self.team.append(staff)
        print(f"[Điều phối] Đã thêm {staff.name} ({staff.__class__.__name__}) vào ca mổ {self.id}")

    def add_order(self, order_text: str) -> None:
     
        self.post_op_orders.append(order_text)
        print(f"[Y lệnh Bác sĩ] Thêm mới: {order_text}")
