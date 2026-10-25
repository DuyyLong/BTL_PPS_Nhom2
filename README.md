# BTL_PPS_Nhom2
# BÀI TẬP LỚN HỌC PHẦN PHƯƠNG PHÁP SỐ - NHÓM 2
**Đề tài:** Chương 3 - Phương trình phi tuyến: Phương pháp Lặp đơn và Phương pháp Newton.

## 1. Bảng phân công nhiệm vụ (Nhóm 7 sinh viên)
Nhóm điều chỉnh từ khung 8 sinh viên sang 7 sinh viên theo quy định mục 1.5 (SV3 đảm nhận phần P2 & P4):

| Vai trò | Họ và tên | Nhiệm vụ chính | Hàm / Nội dung phụ trách | File sở hữu (Commit) |
| :--- | :--- | :--- | :--- | :--- |
| **SV1** | Hoàng Đức Duy | Thuật toán Lặp đơn + Docstring + Báo cáo P1 | Hàm `fixed_point` | `src/lap_don.py` |
| **SV2** | Phạm Thị Tuyến | Thuật toán Newton + Docstring + Báo cáo P2 | Hàm `newton` | `src/newton.py` |
| **SV3** | Vũ Quốc Huy | Cài đặt P3 (Hàm bổ trợ) + Báo cáo P3 | Hàm `check_contraction`, `fourier_start`, `newton_error` | `src/extra.py` |
| **SV4** | Nguyễn Thu Hiền | Bộ kiểm thử `pytest`, ca biên, kiểm thử chéo Nhóm 1 | Kiểm thử 3 bài toán bắt buộc & ca biên | `tests/test_methods.py` |
| **SV5** | Đỗ Minh Chiến | Thực nghiệm so sánh: bảng sai số, đồ thị, nhận xét | So sánh tốc độ hội tụ, bậc 2, nghiệm bội | `experiments/compare.py` |
| **SV6** | Nguyễn Minh Quyết | Bài toán ứng dụng: Dây cáp cầu treo | Mô hình hóa, chạy code tìm `a` và chiều dài `S` | `application/main.py` |
| **SV7** | Lê Duy Long | Trưởng nhóm KT: Repo, chuẩn mã, tích hợp, báo cáo & slide | Quản lý chung, điều phối & tích hợp hệ thống | `README.md`, `main.py` |

## 2. Cấu trúc thư mục dự án
- `src/lap_don.py`: P1 - Phương pháp lặp đơn (`fixed_point`)
- `src/newton.py`: P2 - Phương pháp Newton (`newton`)
- `src/extra.py`: P3 - Kiểm tra điều kiện co, điều kiện Fourier & đánh giá sai số
- `tests/test_methods.py`: Bộ kiểm thử tự động `pytest`
- `experiments/compare.py`: Thực nghiệm so sánh và vẽ đồ thị
- `application/main.py`: Bài toán ứng dụng Dây cáp cầu treo
- `main.py`: Tệp chạy điều phối và tích hợp toàn dự án
- `requirements.txt`: Danh sách các thư viện cần thiết
- `README.md`: Tài liệu hướng dẫn dự án

        
