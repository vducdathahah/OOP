# 🏥 BTL.10 - HỆ THỐNG QUẢN LÝ LỊCH PHẪU THUẬT BỆNH VIỆN
> **Bài tập lớn môn:** Lập trình Hướng đối tượng (OOP)  
> **Ngôn ngữ & Framework:** Python 3.x, Flask, SQLite (SQLAlchemy), Bootstrap 5

---

## 📖 I. MÔ TẢ BÀI TOÁN (Problem Description)
Hệ thống giải quyết bài toán luân chuyển và điều phối quy trình phẫu thuật tại bệnh viện một cách khép kín:
1. **Tiếp nhận & Chuẩn bị:** Khi có bệnh án cần phẫu thuật, hồ sơ được đưa vào hệ thống. Phòng vật tư tiến hành kiểm tra kho – nếu đáp ứng đủ điều kiện vật tư thì mới tiến hành xếp lịch.
2. **Logic xếp lịch:** Lịch mổ được hệ thống tính toán dựa trên 3 yếu tố: sự sẵn sàng của phòng mổ, độ ưu tiên (Ca khẩn cấp > Ca thường), và loại bệnh lý phải phù hợp với tiêu chuẩn của phòng mổ đó.
3. **Thực hiện phẫu thuật:** Mỗi ca mổ được phân công một kíp trực tiêu chuẩn bao gồm: 1 Bác sĩ chính, Y tá và Kỹ thuật viên.
4. **Hậu phẫu:** Sau phẫu thuật, bệnh nhân tuần tự được chuyển sang phòng Hồi tỉnh $\rightarrow$ Hồi sức $\rightarrow$ Chuyển khoa. Bác sĩ và y tá tiến hành ghi y lệnh và theo dõi chăm sóc liên tục trên hệ thống.

---

## ⚙️ II. TÍNH NĂNG CHÍNH (Core Use Cases)
Hệ thống được thiết kế để đáp ứng tối thiểu 7 Use Case nghiệp vụ chính:
1. **Tiếp nhận bệnh án & Duyệt vật tư:** Xử lý hồ sơ đầu vào và xác nhận điều kiện y tế.
2. **Xếp lịch tự động:** Phân bổ thời gian dựa theo phòng và mức độ ưu tiên của bệnh nhân.
3. **Phân công đội ngũ y tế:** Chỉ định Bác sĩ, Y tá, Kỹ thuật viên cho từng ca mổ cụ thể.
4. **Cập nhật trạng thái ca mổ:** Quản lý vòng đời ca mổ (Chờ mổ $\rightarrow$ Đang mổ $\rightarrow$ Hồi tỉnh $\rightarrow$ Hồi sức $\rightarrow$ Chuyển khoa).
5. **Ghi y lệnh hậu phẫu:** Hỗ trợ bác sĩ kê đơn và chỉ định sau mổ.
6. **Ghi nhận chăm sóc bệnh nhân:** Y tá cập nhật tình trạng sinh tồn và quá trình chăm sóc.
7. **Báo cáo & Thống kê:** Xuất báo cáo danh sách ca mổ trong tuần và tính toán KPI hiệu suất của từng phòng mổ.

---

## 🛠️ III. KIẾN TRÚC & ÁP DỤNG OOP
Dự án áp dụng chặt chẽ các nguyên lý Lập trình Hướng đối tượng (OOP) và Design Pattern:

### 1. Kiến trúc Lớp (Classes & Inheritance)
- `Person` *(Abstract Class)*: Lớp cơ sở chứa thông tin định danh (`id`, `name`).
  - **Kế thừa:** Các lớp `Patient` (Bệnh nhân), `Doctor` (Bác sĩ), `Nurse` (Y tá), `Technician` (KTV) đều kế thừa từ `Person`.
- `Surgery` (Ca phẫu thuật): Lớp trung tâm quản lý dữ liệu ca mổ với các thuộc tính: `id`, `patient`, `type`, `priority`, `room`, `start_time`, `status`, `team[]`.
- `OperatingRoom` (Phòng mổ): Thuộc tính `id`, `name`, `allowed_types[]` (loại phẫu thuật được phép).
- `MedicalSupply` (Vật tư y tế): Thuộc tính `name`, `quantity`.

### 2. Design Pattern (State Pattern)
Sử dụng State Pattern để quản lý trạng thái luân chuyển phức tạp của một ca phẫu thuật, tránh sử dụng if/else lồng nhau:
- Abstract Class: `SurgeryState`
- Các Concrete States kế thừa: `Pending` (Chờ) $\rightarrow$ `Scheduled` (Đã xếp lịch) $\rightarrow$ `InProgress` (Đang mổ) $\rightarrow$ `Recovery` (Hồi sức) $\rightarrow$ `Discharged` (Xuất viện/Chuyển khoa).

### 3. Lớp Dịch vụ (Services)
- `Scheduler`: Lớp xử lý nghiệp vụ xếp lịch với logic kiểm tra ràng buộc khắt khe thông qua phương thức `assign(
