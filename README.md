# BÀI TẬP LỚN HỌC PHẦN PHƯƠNG PHÁP SỐ - NHÓM 2

**Đề tài:** Chương 3 - Phương trình phi tuyến: Phương pháp Lặp đơn và Phương pháp Newton.

---

## 1. Bảng phân công nhiệm vụ (Nhóm 7 sinh viên)

*Nhóm điều chỉnh từ khung 8 sinh viên sang 7 sinh viên theo quy định mục 1.5 (SV3 đảm nhận phần P2 & P4):*

| Vai trò | Họ và tên | Nhiệm vụ chính | Hàm / Nội dung phụ trách | File sở hữu (Commit) |
| :--- | :--- | :--- | :--- | :--- |
| **SV1** | Hoàng Đức Duy | Thuật toán Lặp đơn + Docstring + **Báo cáo P1** | Hàm `fixed_point` | `src/lap_don.py` |
| **SV2** | Phạm Thị Tuyến | Thuật toán Newton + Docstring + **Báo cáo P3** | Hàm `newton` | `src/newton.py` |
| **SV3** | Vũ Quốc Huy | Cài đặt P2 & P4 (Hàm bổ trợ) + **Báo cáo P2 & P4** | Hàm `check_contraction`, `fourier_start`, `newton_error` | `src/extra.py` |
| **SV4** | Nguyễn Thu Hiền | Bộ kiểm thử `pytest`, ca biên, kiểm thử chéo Nhóm 1 + **Báo cáo kiểm thử** | Kiểm thử 3 bài toán bắt buộc & ca biên | `tests/test_methods.py` |
| **SV5** | Đỗ Minh Chiến | Thực nghiệm so sánh: bảng sai số, đồ thị, nhận xét + **Báo cáo thực nghiệm** | So sánh tốc độ hội tụ, bậc 2, nghiệm bội | `experiments/compare.py` |
| **SV6** | Nguyễn Minh Quyết | Bài toán ứng dụng: Dây cáp cầu treo + **Báo cáo ứng dụng** | Mô hình hóa, chạy code tìm `a` và chiều dài `S` | `application/main.py` |
| **SV7** | Lê Duy Long | Trưởng nhóm KT: Repo, chuẩn mã, tích hợp, **Tổng hợp báo cáo & slide** | Quản lý chung, điều phối & tích hợp hệ thống | `README.md`, `main.py` |

---

## 2. Cấu trúc thư mục dự án

```text
├── src/
│   ├── __init__.py          # Khai báo và gom các hàm phục vụ bộ kiểm thử chung
│   ├── lap_don.py           # [SV1] P1: Cài đặt hàm fixed_point
│   ├── newton.py            # [SV2] P3: Cài đặt hàm newton
│   └── extra.py             # [SV3] P2 & P4: Cài đặt check_contraction, fourier_start, newton_error
├── tests/
│   └── test_methods.py      # [SV4] Bộ kiểm thử pytest (ví dụ bài giảng, tự chọn, ca biên)
├── experiments/
│   └── compare.py           # [SV5] Thực nghiệm so sánh hội tụ, kiểm chứng bậc 2, nghiệm bội
├── application/
│   └── main.py              # [SV6] Bài toán ứng dụng: Dây cáp cầu treo
├── main.py                  # [SV7] File chạy tích hợp toàn bộ hệ thống
└── README.md                # [SV7] Tài liệu hướng dẫn và bảng phân công nhiệm vụ
