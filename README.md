<div align="center">

# 🏥 Hospital Surgery Scheduler (HSS)

### ⚡ Advanced Surgery Scheduling & Post-Op Management Web App with Python OOP Core

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/SQLite-ORM_SQLAlchemy-003B57?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap" />
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge" />
</p>

<p>
  <b>Hệ thống quản lý, tự động xếp lịch phòng mổ thông minh, tối ưu hóa điều phối kíp trực y tế và số hóa toàn bộ hồ sơ y lệnh chăm sóc hậu phẫu chuẩn OOP.</b>
</p>

<p>
  <a href="https://github.com/vdat2511/Hospital-Surgery-Scheduler/releases/latest">📦 Download Latest Release</a>
  ·
  <a href="https://vdat2511.github.io/Hospital-Surgery-Scheduler-docs/">📖 Web Documentation</a>
  ·
  <a href="https://github.com/vdat2511/Hospital-Surgery-Scheduler/issues">📂 Report Bug</a>
</p>

</div>

---

## ⚡ Các Tính năng Cốt lõi (Use Cases Implemented)

Hệ thống được thiết kế tối ưu cho nghiệp vụ của Điều dưỡng trưởng phòng mổ và các bác sĩ chuyên khoa với đầy đủ các phân hệ chức năng:

* **📋 Tiếp nhận Bệnh án & Duyệt Vật tư:** Hỗ trợ khởi tạo hồ sơ ca mổ từ bệnh án của bệnh nhân. Bộ phận vật tư y tế tiến hành kiểm tra kho tiêu hao (đồ bảo hộ, dao mổ, thuốc gây mê) trước khi hệ thống phê duyệt đưa vào hàng đợi xếp lịch.
* **📅 Thuật toán Xếp lịch Tự động (Smart Scheduler):** Tự động rà soát khung giờ trống của hệ thống phòng mổ chuyên dụng. Ưu tiên tuyệt đối các ca phẫu thuật thuộc diện **Khẩn cấp (Emergency)** lên đầu danh sách và phân bổ khung giờ tối ưu cho các ca thường (Routine).
* **👨‍⚕️ Quản lý Đội ngũ & Tránh Xung đột lịch trực:** Phân bổ kíp mổ hoàn chỉnh (Bác sĩ chính, Y tá phụ mổ, Kỹ thuật viên thiết bị). Hệ thống tích hợp bộ lọc kiểm tra chéo thời gian thực (Real-time Conflict Checker), ngăn chặn tình trạng một nhân sự bị trùng lịch ở hai phòng mổ cùng lúc.
* **🔄 Điều phối Vòng đời Ca mổ (State Machine Workflow):** Cho phép Điều dưỡng trưởng quản lý cập nhật tiến trình di chuyển của bệnh nhân qua các trạng thái: *Chờ duyệt vật tư ➔ Đã lên lịch ➔ Đang phẫu thuật ➔ Phòng hồi tỉnh ➔ Xuất viện/Chuyển khoa*.
* **📝 Ghi Y lệnh Hậu phẫu:** Bác sĩ chính thao tác cập nhật báo cáo diễn biến ca mổ ngay sau khi hoàn thành, kèm theo các chỉ định dùng thuốc, chế độ dinh dưỡng và theo dõi đặc biệt.
* **💉 Nhật ký Chăm sóc của Y tá:** Hỗ trợ y tá trực phòng hồi sức cập nhật biểu đồ sinh tồn (huyết áp, nhịp tim, nhiệt độ) của bệnh nhân theo mốc giờ chỉ định, tự động cảnh báo nếu các chỉ số vượt ngưỡng an toàn.
* **📊 Thống kê Hiệu suất & Đo lường KPI:** Xuất báo cáo tổng quan về tần suất sử dụng các phòng mổ, tỷ lệ ca mổ thành công và thống kê số giờ túc trực của từng y bác sĩ để tính toán KPI cống hiến.

---

## 🧠 Kiến trúc Thiết kế & Ứng dụng Nguyên lý OOP Nâng cao

Mã nguồn dự án được xây dựng dựa trên mô hình thiết kế hướng đối tượng thuần khiết, áp dụng chặt chẽ các nguyên lý thiết kế bền vững (SOLID Design Principles):

### 1. Tính Đóng gói (Encapsulation) & Mô hình Domain Entities
Mọi thực thể trong hệ thống như `Patient`, `Surgery`, `OperatingRoom`, `MedicalSupply` đều đóng gói toàn bộ thuộc tính dữ liệu và chỉ lộ ra các phương thức tương tác thông qua các getter/setter hoặc validator kiểm hợp lệ. Trạng thái ca mổ không thể thay đổi tùy tiện mà phải thông qua phương thức kiểm duyệt logic của lớp.

### 2. Lớp Trừu tượng (Abstract Class) & Tính Kế thừa (Inheritance)
* Thiết lập lớp cơ sở trừu tượng `Person` chứa các thông tin định danh nền tảng (`id`, `name`, `phone`, `email`).
* Các phân lớp chuyên biệt `Doctor`, `Nurse`, `Technician` kế thừa từ `Person`, đồng thời mở rộng thêm các thuộc tính nghiệp vụ riêng biệt như chứng chỉ hành nghề, chuyên khoa sâu, danh sách ca trực.

### 3. Tính Đa hình (Polymorphism) & Mẫu Thiết kế Trạng thái (State Design Pattern)
Hệ thống áp dụng **State Pattern** để quản lý vòng đời ca mổ phức tạp thay vì dùng các câu lệnh `if-else` lồng nhau. Lớp abstract `SurgeryState` định nghĩa các hành vi chuyển trạng thái, các lớp con cụ thể (`PendingState`, `ScheduledState`, `InProgressState`, `RecoveryState`, `DischargedState`) sẽ ghi đè (override) phương thức hành vi này. Hệ thống tự động từ chối nếu người dùng cố tình chuyển trạng thái sai quy trình (ví dụ: nhảy từ *Chờ duyệt* thẳng sang *Phòng hồi tỉnh*).

---

## 📂 Cấu trúc Thư mục Mã nguồn (Project Directory Structure)

```text
hospital-surgery-scheduler/
├── app/
│   ├── __init__.py           # Khởi tạo Flask App, cấu hình SQLAlchemy ORM & bảo mật
│   ├── models/               # Tầng dữ liệu chứa định nghĩa các lớp đối tượng chuyên sâu
│   │   ├── person.py         # Lớp trừu tượng Person, lớp con Doctor, Nurse, Technician
│   │   ├── patient.py        # Quản lý thông tin hồ sơ bệnh án, tiền sử dị ứng thuốc
│   │   ├── room.py           # Mô hình hóa danh mục Phòng mổ (OperatingRoom)
│   │   ├── supply.py         # Quản lý kho Vật tư tiêu hao phục vụ ca mổ
│   │   ├── surgery.py        # Thực thể trung tâm Ca phẫu thuật (Surgery Aggregate)
│   │   └── state.py          # Tập hợp các lớp trạng thái áp dụng State Design Pattern
│   ├── services/             # Tầng xử lý logic nghiệp vụ cốt lõi (Business Layer)
│   │   ├── scheduler.py      # Bộ máy chạy thuật toán xếp lịch, kiểm tra xung đột tài nguyên
│   │   └── kpi_service.py    # Module xử lý số liệu thống kê hiệu suất, xuất báo cáo tuần
│   ├── routes/               # Bộ điều hướng phân tuyến xử lý HTTP Requests (Controllers)
│   │   ├── auth.py           # Kiểm soát quyền truy cập dựa trên vai trò trực (Role-based Auth)
│   │   ├── surgery.py        # Điều hướng xử lý vòng đời, cập nhật tiến độ ca mổ
│   │   └── staff.py          # Quản lý phân công kíp mổ và nhật ký y lệnh chăm sóc
│   ├── templates/            # Giao diện ứng dụng phía người dùng (Jinja2 HTML5 Templates)
│   │   ├── base.html         # Bố cục giao diện khung nền chuẩn hệ thống
│   │   ├── dashboard.html    # Bảng điều khiển thời gian thực của Điều dưỡng trưởng
│   │   ├── schedule.html     # Biểu đồ dòng thời gian trực quan lịch trực các phòng mổ
│   │   └── post_op.html      # Biểu mẫu cập nhật y lệnh sau mổ và theo dõi sinh tồn
│   └── static/               # File tài nguyên tĩnh phục vụ hiển thị Front-end
│       ├── css/              # Tệp tin định dạng giao diện tùy chỉnh
│       └── js/               # Tập lệnh xử lý tương tác UI linh hoạt
├── tests/                    # Kịch bản kiểm thử tự động, đảm bảo độ ổn định hệ thống
│   ├── test_models.py        # Kiểm thử tính đúng đắn của cấu trúc OOP và Kế thừa
│   └── test_scheduler.py     # Kiểm thử thuật toán xếp lịch và chặn trùng ca trực
├── config.py                 # File lưu trữ cấu hình môi trường chạy ứng dụng toàn cục
├── requirements.txt          # Danh sách thư viện Python bắt buộc phục vụ cài đặt nhanh
├── init_db.py                # Tập lệnh tạo cấu trúc cơ sở dữ liệu và nạp dữ liệu mẫu
└── run.py                    # Điểm khởi chạy (Entry Point) ứng dụng máy chủ chính
