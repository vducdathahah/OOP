<h1 align="center">BÀI TẬP LỚN LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG</h1>
<h2 align="center">Đề tài 10: Quản lý lịch phẫu thuật bệnh viện</h2>

**Giảng viên hướng dẫn:** [Điền tên Giảng Viên vào đây]

**Nhóm sinh viên thực hiện:**
1. **Vương Đức Dạt** - 25112239 (Nhóm trưởng)
2. **Nguyễn Bùi Tú** - 25112119
3. **Lê Duy Anh** - 251120043
4. **Nguyễn Khắc Trung Dũng** - 25112030

---

### 1. Giới thiệu đề tài
Hệ thống **Quản lý lịch phẫu thuật bệnh viện** được xây dựng nhằm mục đích tin học hóa quy trình điều phối và quản lý ca mổ. Phần mềm giúp các bệnh viện giải quyết bài toán sắp xếp lịch mổ phức tạp, tránh trùng lặp phòng, theo dõi sát sao tình trạng của bệnh nhân và quản lý hiệu quả vật tư y tế cũng như đội ngũ y bác sĩ tham gia ca mổ.

### 2. Các chức năng chính
Hệ thống bao gồm các nghiệp vụ cốt lõi sau:
- **Tiếp nhận bệnh án & Duyệt vật tư:** Nhận yêu cầu mổ và tự động kiểm tra kho vật tư (nếu đủ vật tư mới cho phép xếp lịch).
- **Xếp lịch tự động:** Phân bổ lịch mổ dựa trên phòng mổ khả dụng, loại bệnh lý phù hợp với phòng, và mức độ ưu tiên (Ca khẩn cấp > Ca thường).
- **Phân công đội ngũ y tế:** Quản lý và chỉ định kíp mổ cho từng ca (bao gồm 1 Bác sĩ chính, Y tá, Kỹ thuật viên).
- **Cập nhật trạng thái ca mổ:** Theo dõi thời gian thực lộ trình của bệnh nhân (Chờ mổ -> Đang mổ -> Hồi tỉnh -> Hồi sức -> Chuyển khoa).
- **Chăm sóc hậu phẫu:** Hỗ trợ bác sĩ ghi y lệnh hậu phẫu và y tá ghi nhận tình trạng chăm sóc bệnh nhân hàng ngày.
- **Báo cáo & Thống kê:** Xuất dữ liệu các ca mổ trong tuần và tính toán chỉ số hiệu suất (KPI) của từng phòng mổ.

### 3. Áp dụng hướng đối tượng (OOP)
Dự án áp dụng chặt chẽ 4 tính chất cơ bản của lập trình hướng đối tượng thông qua ngôn ngữ Python:
- **Tính Trừu tượng (Abstraction):** Khởi tạo lớp trừu tượng `Person` (chứa các thuộc tính chung như `id`, `name`) và lớp `SurgeryState` đại diện cho các trạng thái của ca mổ.
- **Tính Kế thừa (Inheritance):** Các lớp `Patient`, `Doctor`, `Nurse`, `Technician` được kế thừa từ lớp cha `Person`. Các trạng thái cụ thể như `Pending`, `Scheduled`, `InProgress`, `Recovery`, `Discharged` kế thừa từ `SurgeryState` (State Pattern).
- **Tính Đa hình (Polymorphism):** Thể hiện qua các phương thức chuyển đổi trạng thái trong Design Pattern. Cùng một phương thức hành động nhưng mỗi trạng thái (`SurgeryState`) sẽ có cách xử lý logic khác nhau.
- **Tính Đóng gói (Encapsulation):** Các thuộc tính nhạy cảm của bệnh nhân và ca mổ (như `status`, danh sách `team`) được bảo vệ bằng các Access modifiers trong Python (ví dụ: `_status`), chỉ cho phép truy cập và cập nhật thông qua các phương thức kiểm tra ràng buộc logic của lớp `Scheduler`.

### 4. Sơ đồ Use Case
Dưới đây là sơ đồ Use Case thể hiện các tác nhân và chức năng của hệ thống:

![Sơ đồ Use Case](use_case_diagram.png)

### 5. Cài đặt và Hướng dẫn sử dụng
Yêu cầu hệ thống: Cài đặt sẵn Python 3.x trên máy tính.

**Bước 1: Clone mã nguồn về máy**
```bash
git clone [https://github.com/vducdatahah/OOP.git](https://github.com/vducdatahah/OOP.git)
cd OOP
Bước 2: Tạo và kích hoạt môi trường ảo (Virtual Environment)
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt (Trên Windows)
venv\Scripts\activate

# Kích hoạt (Trên macOS/Linux)
source venv/bin/activate
Bước 3: Cài đặt thư viện
pip install -r requirements.txt
Bước 4: Chạy chương trình
python run.py
