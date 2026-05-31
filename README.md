# 🏥 Hospital Surgery Scheduling & Management System (HSSMS)

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask--v3.0-green.svg)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/database-SQLite%20%2F%20SQLAlchemy-orange.svg)](https://www.sqlite.org/)
[![Architecture](https://img.shields.io/badge/architecture-Pure%20OOP%20%7C%20State%20Pattern-red.svg)]()

> **Đồ án nhóm môn học:** Lập trình Hướng đối tượng (OOP)
> **Đề tài số 10:** Hệ thống quản lý và xếp lịch phẫu thuật bệnh viện
> **Hệ thống nộp bài:** sv12.bcse-vju.com

---

## 📝 Tổng quan Dự án

Hệ thống **HSSMS** được xây dựng nhằm số hóa và tối ưu hóa toàn bộ vòng đời điều phối một ca phẫu thuật tại bệnh viện. Phần mềm giúp Điều dưỡng trưởng phòng mổ quản lý danh sách bệnh án, tự động hóa quy trình xếp lịch dựa trên mức độ khẩn cấp, phân công đội ngũ y tế, kiểm tra tính sẵn sàng của vật tư y tế và theo dõi sát sao tiến độ điều trị hậu phẫu của bệnh nhân theo thời gian thực.

Dưới góc nhìn của các kỹ sư phần mềm, dự án này không chỉ giải quyết một bài toán quản lý thông thường mà tập trung tối đa vào việc hiện thực hóa các nguyên lý thiết kế hướng đối tượng nâng cao, áp dụng chặt chẽ các nguyên lý **SOLID** để tạo ra một codebase sạch, dễ mở rộng và có độ bền vững cao.

---

## ⚙️ Áp dụng Kiến trúc OOP & Design Patterns Nâng cao

Để loại bỏ các chuỗi câu lệnh rẽ nhánh `if-else` thô sơ dễ gây lỗi, toàn bộ hệ thống được mô hình hóa bằng các thực thể đối tượng thuần khiết:

### 1. Tính Kế thừa & Đa hình (Inheritance & Polymorphism)
* **Lớp trừu tượng `Person` (Abstract Class):** Định nghĩa khuôn mẫu nền tảng cho mọi thực thể con người trong hệ thống bao gồm `id`, `name`, `email`, và `phone`.
* **Các phân lớp kế thừa chuyên biệt:**
    * `Patient`: Quản lý thông tin tiền sử bệnh án và diễn biến sức khỏe đặc thù.
    * `Doctor` (Bác sĩ chính), `Nurse` (Y tá), `Technician` (Kỹ thuật viên): Kế thừa hành vi chung từ `Person` và mở rộng các thuộc tính chuyên môn riêng (như chứng chỉ phẫu thuật, lịch trực).
* **Tính Đa hình:** Phương thức tác vụ `get_role_permissions()` hoặc `get_health_summary()` được override động tại các lớp con, giúp hệ thống xử lý phân quyền và hiển thị thông tin linh hoạt mà không cần ép kiểu thủ công.

### 2. State Design Pattern (Quản lý Vòng đời Ca mổ)
Trạng thái ca mổ biến đổi liên tục qua nhiều giai đoạn và đòi hỏi các ràng buộc khắt khe. Chúng tôi áp dụng **State Pattern** bằng việc thiết kế lớp abstract `SurgeryState` cùng các lớp trạng thái cụ thể:
* `PendingState` (Chờ duyệt vật tư)
* `ScheduledState` (Đã xếp phòng & lịch mổ)
* `InProgressState` (Đang trong phòng phẫu thuật)
* `RecoveryState` (Bệnh nhân đang hồi tỉnh/hồi sức)
* `DischargedState` (Đã xuất viện hoặc chuyển khoa chuyên môn)

**Lợi ích:** Đối tượng `Surgery` sẽ ủy quyền (delegate) hành vi chuyển đổi cho đối tượng trạng thái hiện tại quản lý. Hệ thống tự động chặn đứng các hành vi chuyển đổi trạng thái không hợp lệ (ví dụ: một ca mổ không thể chuyển sang `InProgress` nếu chưa qua bước `Scheduled` phê duyệt tài nguyên).

### 3. Tầng Dịch vụ & Tính Đóng gói (Service Layer & Composition)
* **Composition:** Lớp `Surgery` đóng vai trò là một phức hợp chứa danh sách liên kết đến `Patient`, `OperatingRoom`, và danh sách mảng đối tượng đội ngũ y tế `team[]` (`Doctor`, `Nurse`, `Technician`).
* **SchedulerService:** Đóng gói toàn bộ logic thuật toán xếp lịch tự động. Khớp loại phẫu thuật với danh mục phòng mổ cho phép (`allowed_types`), tính toán mức độ ưu tiên (`Emergency > Routine`), đồng thời kiểm tra xung đột lịch trực của bác sĩ và định lượng kho vật tư tiêu hao (`MedicalSupply`).

---

## 🚀 Các Tính năng Cốt lõi (Use Cases Implemented)

Hệ thống đáp ứng trọn vẹn và vượt trội hơn 4 use case bắt buộc từ tài liệu đặc tả đồ án:

| STT | Tính năng / Use Case | Mô tả Chi tiết Nghiệp vụ |
| :--- | :--- | :--- |
| **1** | **Tiếp nhận Bệnh án & Duyệt Vật tư** | Số hóa hồ sơ bệnh án cần can thiệp ngoại khoa. Bộ phận vật tư kiểm tra tồn kho kho vật tư tiêu hao (`MedicalSupply`), nếu đủ số lượng sẽ phê duyệt chuyển trạng thái sang hàng đợi xếp lịch. |
| **2** | **Xếp Lịch Tự động Thông minh** | Quét tìm phòng mổ trống thích hợp, ưu tiên tuyệt đối ca mổ cấp cứu (`Emergency`), tự động đề xuất khung giờ `start_time` tối ưu nhằm nâng cao hiệu suất phòng mổ. |
| **3** | **Quản lý & Phân công Đội ngũ Y tế** | Thiết lập kíp mổ hoàn chỉnh bao gồm 1 Bác sĩ chính, Y tá hỗ trợ và Kỹ thuật viên thiết bị. Hệ thống tự động kiểm duyệt chéo, ngăn chặn tình trạng trùng ca trực của nhân viên. |
| **4** | **Điều phối Trạng thái Ca mổ** | Giao diện trực quan cho phép Điều dưỡng trưởng cập nhật tiến trình di chuyển của bệnh nhân theo đúng workflow chuẩn y khoa. |
| **5** | **Ghi Y lệnh Hậu phẫu** | Bác sĩ chính nhập ghi chú diễn biến ca phẫu thuật thành công kèm theo các chỉ định dùng thuốc, chế độ chăm sóc đặc biệt tại phòng hồi sức. |
| **6** | **Ghi nhận Chăm sóc của Y tá** | Cho phép y tá trực ghi nhật ký theo dõi chỉ số sinh tồn (mạch, huyết áp, nhiệt độ) hàng giờ của bệnh nhân trong giai đoạn hồi tỉnh. |
| **7** | **Báo cáo Thống kê & KPI Tuần** | Tổng hợp số liệu các ca mổ trong tuần, đo lường tần suất sử dụng các phòng phẫu thuật và tính toán chỉ số KPI cống hiến của từng nhân sự y tế. |

---

## 📂 Cấu trúc Thư mục Hệ thống (Project Structure)

Mã nguồn được tổ chức phân lớp rạch ròi theo mô hình kiến trúc chuẩn để phục vụ việc phát triển song song giữa các thành viên:

```text
hssms-project/
├── app/
│   ├── __init__.py           # Khởi tạo Flask Application & Cấu hình DB ORM
│   ├── models/               # Tầng dữ liệu chứa các thực thể đối tượng (Models)
│   │   ├── person.py         # Base class Person, Patient, Doctor, Nurse, Technician
│   │   ├── surgery.py        # Đối tượng Ca mổ (Surgery) và Vật tư (MedicalSupply)
│   │   ├── room.py           # Đối tượng Phòng mổ (OperatingRoom)
│   │   └── state.py          # Kiến trúc State Pattern cho vòng đời ca mổ
│   ├── services/             # Tầng nghiệp vụ chứa logic xử lý cốt lõi (Services)
│   │   ├── scheduler.py      # Bộ máy xếp lịch tự động và kiểm tra ràng buộc tài nguyên
│   │   └── report_service.py # Xử lý tính toán KPI nhân sự và tổng hợp số liệu
│   ├── routes/               # Tầng điều hướng tiếp nhận Request (Controllers)
│   │   ├── auth.py           # Phân quyền đăng nhập hệ thống theo vai trò trực
│   │   ├── surgery_routes.py # Tiếp nhận điều phối ca mổ và chuyển trạng thái State
│   │   └── staff_routes.py   # Quản lý CRUD nhân lực và theo dõi tiến độ KPI
│   ├── templates/            # Giao diện hiển thị Web (Jinja2 HTML Templates)
│   │   ├── base.html         # Bố cục giao diện nền tảng
│   │   ├── dashboard.html    # Màn hình tổng quan của Điều dưỡng trưởng phòng mổ
│   │   ├── schedule.html     # Biểu đồ Timeline dòng thời gian lịch mổ
│   │   └── post_op.html      # Form nhập y lệnh và nhật ký chăm sóc bệnh nhân
│   └── static/               # File tài nguyên tĩnh phục vụ front-end
│       ├── css/              # Tệp cấu hình giao diện custom
│       └── js/               # Tệp xử lý tương tác giao diện động
├── tests/                    # Kịch bản kiểm thử tự động (Unit Tests)
│   ├── test_models.py
│   └── test_scheduler.py
├── config.py                 # File cấu hình môi trường ứng dụng toàn cục
├── requirements.txt          # Danh sách thư viện Python bắt buộc
├── run.py                    # Entry Point - Điểm kích hoạt khởi chạy dự án chính
└── README.md                 # Tài liệu hướng dẫn này
