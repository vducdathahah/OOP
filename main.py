# main.py
from datetime import datetime
from app.models.person import Patient, Doctor, Nurse, Technician
from app.models.room_supply import OperatingRoom
from app.models.surgery import Surgery
from app.services.scheduler import Scheduler

if __name__ == "__main__":
    # 1. Khởi tạo dịch vụ điều phối bệnh viện
    hospital_core = Scheduler()
    
    # Thiết lập cơ sở vật chất phòng mổ (Use Case 2)
    hospital_core.add_room(OperatingRoom("OR_01", "Phòng mổ Tim Mạch Đặc Biệt", ["Tim mạch"]))
    hospital_core.add_room(OperatingRoom("OR_02", "Phòng mổ Ngoại Chấn Thương", ["Chấn thương"]))
    
    # Nhập kho vật tư y tế (Use Case 1)
    hospital_core.update_inventory("Dao mổ siêu âm", 5)
    hospital_core.update_inventory("Khung nẹp cố định xương đùi", 1) # Chỉ có 1 bộ nẹp

    # 2. Khởi tạo hồ sơ nhân sự (Use Case 3)
    patient_a = Patient("BN01", "Nguyễn Văn A", "Hở van tim nặng")
    patient_b = Patient("BN02", "Lê Văn B", "Gãy xương đùi")
    patient_c = Patient("BN03", "Phạm Văn C", "Chấn thương phức tạp")
    
    doctor_nam = Doctor("DR01", "Dr. Nguyễn Hoài Nam", "Tim mạch")
    nurse_lan = Nurse("NS01", "Điều dưỡng Hoàng Lan")
    tech_duc = Technician("TECH01", "KTV Minh Đức", "Máy tuần hoàn ngoài cơ thể")

    # 3. Tạo các ca mổ yêu cầu xử lý
    s1 = Surgery("MỔ_TIM_01", patient_a, "Tim mạch", "Khẩn cấp", {"Dao mổ siêu âm": 1})
    s2 = Surgery("MỔ_XƯƠNG_01", patient_b, "Chấn thương", "Thường", {"Khung nẹp cố định xương đùi": 1})
    s3 = Surgery("MỔ_XƯƠNG_02", patient_c, "Chấn thương", "Khẩn cấp", {"Khung nẹp cố định xương đùi": 1}) # Sẽ lỗi thiếu vật tư

    # Thực thi kiểm tra kho và tiếp nhận (Use Case 1)
    hospital_core.check_and_receive_record(s1)
    hospital_core.check_and_receive_record(s2)
    hospital_core.check_and_receive_record(s3) # Trả về lỗi thất bại do hết khung nẹp đùi

    # 4. Chạy tiến trình xếp lịch tự động (Use Case 2)
    sim_date = datetime(2026, 6, 1, 8, 0)
    hospital_core.auto_schedule(sim_date)

    # 5. Phân công đội ngũ y tế vào ca mổ Tim (Use Case 3)
    print("\n--- Tiến hành điều động nhân sự ---")
    s1.assign_staff(doctor_nam)
    s1.assign_staff(nurse_lan)
    s1.assign_staff(tech_duc)

    # 6. Mô phỏng ca mổ diễn ra thông qua chuyển đổi trạng thái (Use Case 4)
    print("\n--- Nhật ký diễn biến ca mổ thực tế ---")
    s1.advance_stage()  # Scheduled -> InProgress
    s1.advance_stage()  # InProgress -> Recovery
    
    # Bác sĩ ghi y lệnh hậu phẫu & Y tá chăm sóc (Use Case 5 & 6)
    s1.add_order("Theo dõi điện tâm đồ liên tục, tiêm kháng sinh liều cao lúc 20h.")
    nurse_lan.record_care(s1.id, "Bệnh nhân đã tỉnh, các chỉ số sinh tồn ổn định, đã thực hiện y lệnh tiêm.")
    
    s1.advance_stage()  # Recovery -> Discharged

    # 7. Xuất báo cáo hoạt động tuần (Use Case 7)
    hospital_core.generate_report()
