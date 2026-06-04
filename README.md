# 🩺 SurgOps — Hệ thống Điều phối Phòng mổ & Vật tư Y tế

**SurgOps** là giải pháp phần mềm thông minh hỗ trợ các bệnh viện tối ưu hóa hiệu suất sử dụng phòng mổ, quản lý lịch phẫu thuật theo thời gian thực và tự động đưa ra cảnh báo về tình trạng thiếu hụt vật tư y tế khẩn cấp.

---

## 🌟 Tính Năng Cốt Lõi Của Hệ Thống

Dự án hiện tại đã hoàn thiện phân hệ **Tổng quan (Dashboard)** dành cho Quản lý viện với các tính năng:
- **Thống kê thông minh:** Hiển thị trực quan tổng số ca phẫu thuật, tỉ lệ sử dụng phòng (đạt 50%) và số lượng vật tư dưới ngưỡng an toàn.
- **Quản lý trạng thái ca mổ:** Biểu đồ tiến độ trực quan phân chia từ *Chờ xếp lịch, Đã xếp lịch, Đang phẫu thuật* cho đến *Hồi tỉnh* và *Hoàn thành*.
- **Hệ thống cảnh báo sớm (Alerts):** Tự động phát hiện và highlight các ca cấp cứu đang chờ xử lý cũng như danh mục thiết bị y tế sắp hết (ví dụ: Bộ dao mổ, Thuốc gây mê).
- **Bảng điều phối trực quan:** Danh sách lịch phẫu thuật chi tiết trong ngày, phân loại rõ ràng mức độ ưu tiên (*Cấp cứu* vs *Thường*).

---

## 🛠️ Công Nghệ Sử Dụng

- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Tailwind CSS (qua file styles hệ thống).
- **Bộ Icons:** Sử dụng thư viện Lucide Icons chuyên nghiệp cho ngành y tế.
- **Mô hình kiến trúc:** Giao diện Responsive (tương thích tốt trên cả máy tính và thiết bị di động).

---

## 📂 Cấu Trúc Thư Mục Dự Án

```text
├── assets/                  # Chứa các file bổ trợ hệ thống
│   ├── styles-7R0-AbNL.css  # Tệp định dạng giao diện chính
│   └── index-fs79kseD.js   # Script xử lý logic luồng dữ liệu
├── index.html               # Trang giao diện chính (Dashboard)
└── README.md                # Tài liệu hướng dẫn dự án
