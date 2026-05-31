# app/states/surgery_state.py
from abc import ABC, abstractmethod

class SurgeryState(ABC):
    """Lớp trừu tượng định nghĩa giao diện chung cho mọi trạng thái ca mổ."""
    @abstractmethod
    def next(self, surgery: "Surgery") -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class PendingState(SurgeryState):
    def next(self, surgery: "Surgery") -> None:
        if surgery.room and surgery.start_time:
            from app.states.surgery_state import ScheduledState
            surgery.set_state(ScheduledState())
        else:
            raise ValueError("Không thể xếp lịch: Thiếu thông tin phòng mổ hoặc thời gian!")
            
    def __str__(self) -> str: 
        return "Pending (Chờ duyệt vật tư & xếp lịch)"

class ScheduledState(SurgeryState):
    def next(self, surgery: "Surgery") -> None:
        if len(surgery.team) >= 3:  # Tối thiểu phải có Bác sĩ, Y tá và Kỹ thuật viên [cite: 274]
            from app.states.surgery_state import InProgressState
            surgery.set_state(InProgressState())
        else:
            raise ValueError("Không thể tiến hành: Đội ngũ y tế chưa được phân công đầy đủ!")
            
    def __str__(self) -> str: 
        return "Scheduled (Đã xếp lịch & sẵn sàng)"

class InProgressState(SurgeryState):
    def next(self, surgery: "Surgery") -> None:
        from app.states.surgery_state import RecoveryState
        surgery.set_state(RecoveryState())
        
    def __str__(self) -> str: 
        return "InProgress (Đang trong phòng phẫu thuật)"

class RecoveryState(SurgeryState):
    def next(self, surgery: "Surgery") -> None:
        from app.states.surgery_state import DischargedState
        surgery.set_state(DischargedState())
        
    def __str__(self) -> str: 
        return "Recovery (Đang hồi tỉnh / Hồi sức hậu phẫu)"

class DischargedState(SurgeryState):
    def next(self, surgery: "Surgery") -> None:
        print(f"[Thông báo] Ca mổ {surgery.id} đã hoàn tất hoàn toàn. Bệnh nhân đã chuyển khoa dưỡng bệnh.")
        
    def __str__(self) -> str: 
        return "Discharged (Đã xuất viện / Chuyển khoa)"
