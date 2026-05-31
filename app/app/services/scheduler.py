# app/services/scheduler.py
from datetime import datetime, timedelta
from typing import List, Dict
from app.models.surgery import Surgery
from app.models.room_supply import OperatingRoom

class Scheduler:
    """Dịch vụ lõi xử lý thuật toán phân phòng và kiểm tra kho vật tư[cite: 272, 273, 279]."""
    def __init__(self):
        self.rooms: List[OperatingRoom] = []
        self.inventory: Dict[str, int] = {}
        self.surgeries: List[Surgery] = []

    def add_room(self, room: OperatingRoom) -> None:
        self.rooms.append(room)

    def update_inventory(self, supply_name: str, qty: int) -> None:
        self.inventory[supply_name] = self.inventory.get(supply_name, 0) + qty

    def check_and_receive_record(self, surgery: Surgery) -> bool:
        """Use Case 1: Tiếp nhận bệnh án và duyệt vật tư kho[cite: 272, 276]."""
        print(f"\n[Hệ thống] Đang thẩm định vật tư ca mổ {surgery.id}...")
        for item, needed_qty in surgery.required_supplies.items():
            if self.inventory.get(item, 0) < needed_qty:
                print(f"[-] DUYỆT THẤT BẠI: Kho không đủ '{item}' (Cần: {needed_qty}, Có: {self.inventory.get(item, 0)})")
                return False
        
        # Đủ vật tư -> Trừ kho vật tư tạm ứng
        for item, needed_qty in surgery.required_supplies.items():
            self.inventory[item] -= needed_qty
            
        self.surgeries.append(surgery)
        print(f"[+] DUYỆT THÀNH CÔNG: Đã niêm phong đủ vật tư y tế.")
        return True

    def auto_schedule(self, start_date: datetime) -> None:
        """Use Case 2: Xếp lịch tự động theo phòng và độ ưu tiên (Khẩn cấp > Thường)[cite: 273, 276]."""
        print(f"\n[Thuật toán] Khởi động trình tự động tối ưu xếp lịch ngày {start_date.date()}...")
        
        # Lọc các ca mổ đang ở trạng thái Pending và sắp xếp: "Khẩn cấp" lên đầu [cite: 273]
        pending_surgeries = [s for s in self.surgeries if "Pending" in s.get_status()]
        pending_surgeries.sort(key=lambda s: 0 if s.priority == "Khẩn cấp" else 1)

        current_slot = start_date

        for surgery in pending_surgeries:
            is_scheduled = False
            for room in self.rooms:
                # Kiểm tra ràng buộc loại phẫu thuật phù hợp và phòng trống [cite: 273]
                if surgery.type in room.allowed_types and room.is_available(current_slot):
                    surgery.room = room
                    surgery.start_time = current_slot
                    room.booked_slots.append(current_slot)
                    
                    surgery.advance_stage()  # Chuyển trạng thái sang Scheduled 
                    print(f"[🗲] Đã xếp ca {surgery.id} vào phòng [{room.name}] lúc {current_slot.strftime('%H:%M')}")
                    
                    current_slot += timedelta(hours=2)  # Mỗi ca mổ cách nhau 2 tiếng để dọn dẹp phòng
                    is_scheduled = True
                    break
            
            if not is_scheduled:
                print(f"[-] Cảnh báo: Không thể xếp lịch ca mổ {surgery.id} do hết phòng phù hợp!")

    def generate_report(self) -> None:
        """Use Case 7: Báo cáo ca mổ trong tuần và KPI phòng mổ[cite: 276]."""
        print("\n" + "="*60)
        print("          BÁO CÁO HIỆU SUẤT PHÒNG MỔ BỆNH VIỆN TRONG TUẦN")
        print("="*60)
        print(f"Tổng số ca mổ tiếp nhận: {len(self.surgeries)}")
        
        for room in self.rooms:
            hours = len(room.booked_slots) * 2
            print(f" • {room.name}: Tổng giờ phẫu thuật đã vận hành = {hours} giờ (KPI)")
        print("="*60 + "\n")
