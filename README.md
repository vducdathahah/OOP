# BTL.10 - HỆ THỐNG QUẢN LÝ LỊCH PHẪU THUẬT BỆNH VIỆN
> **Bài tập lớn môn:** Lập trình Hướng đối tượng (OOP)  
> **Hệ thống nộp bài:** sv12.bcse-vju.com  
> **Ngôn ngữ & Framework:** Python 3.x, Flask, SQLite (SQLAlchemy), Bootstrap 5

---

## 📌 1. Giới thiệu Đề tài
Dự án tập trung giải quyết bài toán tối ưu hóa quy trình lập lịch, điều phối và quản lý vòng đời các ca phẫu thuật trong bệnh viện. Đối tượng người dùng trung tâm là **Điều dưỡng trưởng phòng mổ** – người chịu trách nhiệm điều phối toàn diện từ khâu tiếp nhận bệnh nhân, kiểm tra vật tư, phân phòng mổ cho đến khi bệnh nhân xuất viện hoặc chuyển khoa hậu phẫu.

## ⚙️ 2. Các Tính năng Hệ thống (Core Use Cases)
Hệ thống đáp ứng toàn bộ các nghiệp vụ khắt khe theo yêu cầu đề bài:
* **Tiếp nhận & Duyệt vật tư:** Tiếp nhận hồ sơ bệnh án từ các khoa lâm sàng, tự động đối chiếu số lượng vật tư y tế trong kho tiêu hao trước khi phê duyệt ca mổ.
* **Xếp lịch phẫu thuật tự động & Bán tự động:** Tự động đề xuất khung giờ dựa trên các ràng buộc: Phòng mổ trống, tính tương thích của thiết bị phòng mổ với loại phẫu thuật, và thứ tự ưu tiên cấp cứu (Ca khẩn cấp > Ca thường).
* **Phân công kíp mổ (Đội ngũ y tế):** Chỉ định chi tiết nhân sự phối hợp gồm: Bác sĩ phẫu thuật chính, Bác sĩ gây mê, Điều dưỡng hỗ trợ và Kỹ thuật viên thiết bị.
* **Theo dõi vòng đời ca mổ (State Tracking):** Giám sát trạng thái thời gian thực của ca mổ qua các giai đoạn nghiêm ngặt.
* **Y lệnh & Nhật ký hậu phẫu:** Hỗ trợ bác sĩ cập nhật y lệnh thuốc, điều dưỡng cập nhật chỉ số sinh tồn và ghi nhận nhật ký chăm sóc tại phòng hồi sức.
* **Báo cáo & Thống kê hiệu suất:** Tổng hợp số liệu ca mổ theo tuần/tháng, tính toán chỉ số hiệu suất sử dụng (KPI) của từng phòng mổ để tối ưu hóa nguồn lực.

## 🛠️ 3. Kiến trúc Hướng đối tượng (OOP Architecture)
Đồ án áp dụng triệt để các nguyên lý thiết kế hướng đối tượng cốt lõi để đảm bảo hệ thống có tính module hóa cao, dễ bảo trì và mở rộng:

* **Tính Kế thừa (Inheritance):**
  * Lớp trừu tượng nền tảng `Person` (định nghĩa thuộc tính cơ bản như `id`, `name`, `gender`, `role`).
  * Các lớp con `Patient`, `Doctor`, `Nurse`, `Technician` kế thừa trực tiếp từ `Person` và mở rộng các thuộc tính/phương thức đặc trưng nghiệp vụ.
* **Mô hình hóa Quan hệ (Association & Composition):**
  * Lớp `Surgery` đóng vai trò trung tâm, chứa quan hệ sở hữu chặt chẽ (Composition) với `Patient` và `OperatingRoom`, kết hợp (Association) với danh sách các đối tượng thuộc kíp mổ (`MedicalStaff`).
  * Lớp quản lý `Scheduler` đóng gói toàn bộ logic kiểm tra xung đột lịch trình thông qua phương thức kiểm tra chéo `check_conflict()`.
* **Áp dụng State Pattern (Quản lý Trạng thái):**
  * Thay vì sử dụng chuỗi câu lệnh `if-else` phức tạp để kiểm tra điều kiện chuyển đổi trạng thái của ca mổ, dự án định nghĩa interface `SurgeryState` cùng các lớp trạng thái cụ thể: `PendingState`, `ScheduledState`, `InProgressState`, `RecoveryState`, `DischargedState`. 
  * Mỗi trạng thái tự đóng gói hành vi logic hợp lệ của riêng nó (Ví dụ: Không thể chuyển từ *Chờ mổ* thẳng sang *Xuất viện* mà bắt buộc phải qua trạng thái *Đang mổ*).

---

## 🗺️ 4. Sơ đồ Thiết kế Hệ thống (UML Diagrams)

### A. Sơ đồ Use Case (Phân quyền & Chức năng)
Dưới đây là sơ đồ luồng tính năng tương tác của Điều dưỡng trưởng và các tác nhân vào hệ thống:

![Sơ đồ Use Case](use_case_diagram.png)

---

## 📂 5. Cấu trúc Thư mục Dự án (Project Structure)
```text
OOP/
│
├── app/
│   ├── __init__.py          # Khởi tạo ứng dụng Flask & Cấu hình Database
│   ├── models.py            # Chứa định nghĩa các lớp OOP (Person, Patient, Surgery, State Pattern...)
│   ├── routes.py            # Điều hướng API và xử lý Logic điều khiển (Controllers)
│   ├── static/              # Lưu trữ file CSS, JS tùy chỉnh
│   └── templates/           # Giao diện hiển thị Frontend (Bootstrap 5)
│
├── images/
│   └── use_case_diagram.png # File ảnh sơ đồ thiết kế hệ thống
│
├── requirements.txt         # Danh sách thư viện phụ thuộc cần cài đặt
├── run.py                   # Điểm khởi chạy hệ thống (Entry Point)
└── README.md                # Tài liệu hướng dẫn dự án
