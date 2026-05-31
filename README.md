<div align="center">

# 🏥 Hospital Surgery Scheduling Management System (HSSMS)
### ⚡ Hệ thống Quản lý và Xếp lịch Phẫu thuật Bệnh viện — Bài 10

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/SQLite-SQLAlchemy_ORM-003B57?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap" />
  <img src="https://img.shields.io/badge/Architecture-Pure_OOP_|_State_Pattern-red?style=for-the-badge" />
</p>

<p>
  <b>Ứng dụng Web số hóa toàn bộ quy trình tiếp nhận bệnh án, tự động điều phối lịch mổ thông minh, tối ưu hóa kíp trực y tế và quản lý y lệnh chăm sóc hậu phẫu chuẩn kiến trúc hướng đối tượng.</b>
</p>

</div>

---

## 👨‍💻 Đội ngũ Phát triển — MedTech Team

Hệ thống được thiết kế, xây dựng và vận hành bởi các thành viên:

| Họ và Tên | Mã Sinh Viên | Vai trò & Trách nhiệm chính trong Dự án |
|---|---|---|
| **Vương Đức Đạt** | `25112239` | 👑 **Nhóm trưởng (Leader) / Lead Architect**<br>• Thiết kế cấu trúc hệ thống tổng thể và vẽ sơ đồ lớp UML.<br>• Hiện thực hóa mô hình State Design Pattern quản lý vòng đời ca mổ.<br>• Đóng gói, kiểm soát chất lượng mã nguồn và tích hợp hệ thống. |
| **Lê Duy Anh** | `25112004` | 💻 **Core Backend Developer**<br>• Thiết kế cơ sở dữ liệu quan hệ chuyển đổi qua SQLAlchemy ORM.<br>• Lập trình các lớp thực thể nhân sự, hồ sơ bệnh nhân và kho vật tư.<br>• Viết hệ thống APIs xử lý và cung cấp dữ liệu logic cho Front-end. |
| **Nguyễn Bùi Tú** | `25112119` | 🎨 **Frontend Developer / UI-UX Designer**<br>• Xây dựng toàn bộ giao diện người dùng trực quan bằng Bootstrap 5.<br>• Thiết kế bảng dòng thời gian (Timeline) theo dõi lịch trực phòng mổ.<br>• Render dữ liệu động từ Backend thông qua Jinja2 Templates. |
| **Nguyễn Khắc Trung Dũng** | `25112030` | ⚙️ **Logic & QA Engineer**<br>• Lập trình bộ máy thuật toán tự động xếp lịch `SchedulerService`.<br>• Xử lý logic kiểm tra xung đột thời gian thực của kíp mổ/phòng mổ.<br>• Viết kịch bản kiểm thử tự động (Unit Tests) bằng thư viện `pytest`. |

---

## 🎯 Mục tiêu & Ngữ cảnh Dự án

Dự án này được nghiên cứu và phát triển nghiêm túc nhằm giải quyết trọn vẹn bài toán nghiệp vụ của **Đề tài số 10: Quản lý lịch phẫu thuật bệnh viện** thuộc khuôn khổ Bài tập lớn môn học **Lập trình Hướng đối tượng (OOP)**.

* **Đối tượng đích:** Điều dưỡng trưởng phòng mổ, Bác sĩ phẫu thuật chính, Y tá trực phòng hồi sức và Bộ phận quản lý kho vật tư y tế.
* **Mục tiêu học thuật:** Chứng minh năng lực phân tích hệ thống y tế thực tế; áp dụng thực chiến 4 tính chất cốt lõi của OOP (Đóng gói, Kế thừa, Đa hình, Trừu tượng) kết hợp với Design Pattern nâng cao để tạo ra phần mềm có cấu trúc sạch (Clean Code), dễ bảo trì và mở rộng.
* **Hệ thống nộp bài chính thức:** sv12.bcse-vju.com

---

## ✨ Các Tính năng Nghiệp vụ (Use Cases Implemented)

Hệ thống cung cấp giải pháp chuyển đổi số toàn diện qua 7 phân hệ tính năng cốt lõi:

1. **📋 Tiếp nhận Bệnh án & Duyệt Vật tư:** Hỗ trợ điều dưỡng khởi tạo ca phẫu thuật từ bệnh án. Bộ phận vật tư kiểm kho thuốc, thiết bị tiêu hao; nếu đủ điều kiện hệ thống sẽ phê duyệt ca mổ vào hàng đợi.
2. **📅 Thuật toán Xếp lịch Tự động:** Tự động quét lịch trống của các phòng mổ chuyên dụng, ưu tiên đẩy các ca thuộc diện **Khẩn cấp (Emergency)** lên đầu và xếp khung giờ tối ưu cho ca thường.
3. **👨‍⚕️ Điều phối Kíp mổ & Tránh xung đột:** Tự động ràng buộc cấu trúc kíp mổ (1 Bác sĩ chính, Y tá, Kỹ thuật viên) và đưa ra cảnh báo chặn ngay lập tức nếu nhân sự bị trùng lịch ở phòng mổ khác.
4. **🔄 State Machine điều phối ca mổ:** Cho phép Điều dưỡng trưởng cập nhật trạng thái ca mổ theo thời gian thực: *Chờ duyệt ➔ Đã xếp lịch ➔ Đang mổ ➔ Phòng hồi tỉnh ➔ Xuất viện*.
5. **📝 Ghi Y lệnh Hậu phẫu:** Bác sĩ chính nhập báo cáo kết quả ca phẫu thuật, cập nhật ghi
