# BÀI TẬP LỚN LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP)
## ĐỀ TÀI 10: HỆ THỐNG QUẢN LÝ LỊCH PHẪU THUẬT BỆNH VIỆN

[cite_start]Hệ thống quản lý và tối ưu hóa lịch phẫu thuật tại bệnh viện, hỗ trợ đắc lực cho điều dưỡng trưởng phòng mổ trong công tác quản lý vật tư, điều phối nhân lực và theo dõi sát sao tình trạng bệnh nhân.

---

## 1. Giới thiệu thành viên nhóm

Dưới đây là danh sách thành viên thực hiện dự án (Vui lòng cập nhật đúng thông tin cá nhân):

| STT | Họ và tên | Mã số sinh viên (MSSV) | Vai trò / Nhiệm vụ đảm nhiệm |
|---|---|---|---|
| 1 | [Sinh viên mẫu A] | [MSSV_01] | *Nhóm trưởng* - Thiết kế kiến trúc, Dịch vụ xếp lịch Core (Scheduler) |
| 2 | [Sinh viên mẫu B] | [MSSV_02] | [cite_start]Phát triển phân hệ Nhân sự (Person, Doctor, Nurse,...) [cite: 570] |
| 3 | [Sinh viên mẫu C] | [MSSV_03] | [cite_start]Quản lý vòng đời ca mổ (Surgery, State Pattern) [cite: 571, 572] |
| 4 | [Sinh viên mẫu D] | [MSSV_04] | [cite_start]Thiết kế quản lý vật tư (OperatingRoom, Inventory) & Xuất báo cáo [cite: 569, 571] |

---

## 2. Cấu trúc thư mục nguồn (Project Structure)

[cite_start]Project được phân tách module rõ ràng theo nguyên lý thiết kế hướng đối tượng, giúp dễ dàng bảo trì và mở rộng[cite: 570, 571]:

```text
 hospital_scheduler/
 │
 ├── main.py                  # Điểm chạy chính của chương trình (Kịch bản mô phỏng)
 └── app/
     ├── _init_.py
     │
     ├── models/              # Chứa các lớp định nghĩa thực thể dữ liệu
     │   ├── _init_.py
     │   ├── person.py        # Quản lý lớp trừu tượng Person, Patient, Doctor, Nurse, Tech [cite: 570]
     │   ├── room_supply.py   # Định nghĩa Phòng mổ (OperatingRoom) và Vật tư y tế [cite: 571]
     │   └── surgery.py       # Quản lý thông tin ca mổ và trạng thái ca mổ (State Pattern) [cite: 571, 572]
     │
     └── services/            # Chứa các lớp xử lý logic nghiệp vụ
         ├── _init_.py
         └── scheduler.py     # Bộ điều phối tự động kiểm tra kho vật tư & xếp lịch mổ [cite: 569, 572]
