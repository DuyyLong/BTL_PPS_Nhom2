# BTL_PPS_Nhom2
Bài tập lớn Phương Pháp Số - nhóm 2
# BÀI TẬP LỚN PHƯƠNG PHÁP SỐ - NHÓM 2
**Chủ đề:** Chương 3 — Giải phương trình phi tuyến bằng Phương pháp Lặp đơn và Phương pháp Newton.



## 1. Bảng phân công nhiệm vụ (Nhóm 7 sinh viên)
Nhóm thực hiện điều chỉnh phân công cho 7 thành viên nhưng vẫn giữ nguyên nguyên tắc mỗi sinh viên sở hữu ít nhất một phần mã nguồn trong lịch sử commit[cite: 1]:

| Vai trò | Họ và Tên | MSSV | Tài khoản GitHub | Nhiệm vụ & File phụ trách |
| :--- | :--- | :--- | :--- | :--- |
| **SV1** | Hoàng Đức Duy | 243030519 | @hducduy2006-hub | Cài đặt PP Lặp đơn (`src/lap_don.py`), docstring, báo cáo P1[cite: 1] |
| **SV2** | Phạm Thị Tuyến | 243030558 | @... | Cài đặt PP Newton (`src/newton.py`), docstring, báo cáo P2[cite: 1] |
| **SV3** | Vũ Quốc Huy | 243030528 | @vuquochuy-peel | Cài đặt PP Newton cải tiến/Sai phân & kiểm tra điều kiện (`src/mo_rong.py`), báo cáo P3-P4[cite: 1] |
| **SV4** | Nguyễn Thu Hiền | 243030523 | @... | Bộ kiểm thử `pytest` (`tests/test_methods.py`), ca biên, phản biện chéo Nhóm 1[cite: 1] |
| **SV5** | Đỗ Minh Chiến | 243030515 | @... | Thực nghiệm so sánh (`experiments/compare.py`), bảng sai số, đồ thị, nhận xét[cite: 1] |
| **SV6** | Nguyễn Minh Quyết | 243030549 | @... | Bài toán ứng dụng (`application/app_colebrook.py`), mô hình hóa, phân tích[cite: 1] |
| **SV7** | Lê Duy Long | 243030540 | @DuyyLong | Trưởng nhóm KT: Quản lý Repo, chuẩn mã, `README.md`, tích hợp, gộp báo cáo & slide[cite: 1] |
## 2. Cấu trúc thư mục
```text
BTL_PPS_Nhom2/
├── src/
│   ├── __init__.py
│   ├── lap_don.py          # SV1: Thuật toán lặp đơn
│   ├── newton.py           # SV2: Thuật toán Newton-Raphson
│   └── mo_rong.py          # SV3: Đạo hàm sai phân & kiểm tra hội tụ
├── tests/
│   └── test_methods.py     # SV4: Bộ kiểm thử pytest
├── experiments/
│   └── compare.py          # SV5: So sánh sai số và vẽ đồ thị
├── application/
│   └── app_colebrook.py    # SV6: Bài toán ứng dụng thực tế
├── requirements.txt
└── README.md               # SV7: Tài liệu hướng dẫn
