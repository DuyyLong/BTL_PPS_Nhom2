# BTL_PPS_Nhom2
# BÀI TẬP LỚN HỌC PHẦN PHƯƠNG PHÁP SỐ - NHÓM 2
**Đề tài:** Chương 3 - Phương trình phi tuyến: Phương pháp Lặp đơn và Phương pháp Newton.

## 1. Bảng phân công nhiệm vụ (Nhóm 7 sinh viên)
Nhóm điều chỉnh từ khung 8 sinh viên sang 7 sinh viên theo quy định mục 1.5 (SV3 đảm nhận phần P2 & P4):

| Vai trò | Họ và tên | Nhiệm vụ chính | Hàm / Nội dung phụ trách | File sở hữu (Commit) |
| :--- | :--- | :--- | :--- | :--- |
| **SV1** | Hoàng Đức Duy | Thuật toán Lặp đơn + Docstring + Báo cáo P1 | Hàm `fixed_point` | `src/lap_don.py` |
| **SV2** | Phạm Thị Tuyến | Thuật toán Newton + Docstring + Báo cáo P3 | Hàm `newton` | `src/newton.py` |
| **SV3** | Vũ Quốc Huy | Cài đặt P2–P4 (Hàm bổ trợ) + Báo cáo P2, P4 | Hàm `check_contraction`, `fourier_start`, `newton_error` | `src/extra.py` |
| **SV4** | Nguyễn Thu Hiền | Bộ kiểm thử `pytest`, ca biên, kiểm thử chéo Nhóm 1 | Kiểm thử 3 bài toán bắt buộc & ca biên | `tests/test_methods.py` |
| **SV5** | Đỗ Minh Chiến | Thực nghiệm so sánh: bảng sai số, đồ thị, nhận xét | So sánh tốc độ hội tụ, bậc 2, nghiệm bội | `experiments/compare.py` |
| **SV6** | Nguyễn Minh Quyết | Bài toán ứng dụng: Dây cáp cầu treo | Mô hình hóa, chạy code tìm `a` và chiều dài `S` | `application/main.py` |
| **SV7** | Lê Duy Long | Trưởng nhóm KT: Repo, chuẩn mã, tích hợp, báo cáo & slide | Quản lý chung, điều phối & tích hợp hệ thống | `README.md`, `main.py` |

## 2. Cấu trúc thư mục dự án
- `src/lap_don.py`: P1 - Phương pháp lặp đơn (`fixed_point`)
- `src/newton.py`: P3 - Phương pháp Newton (`newton`)
- `src/extra.py`: P2 & P4 - Kiểm tra điều kiện co, điều kiện Fourier & đánh giá sai số
- `tests/test_methods.py`: Bộ kiểm thử tự động `pytest`
- `experiments/compare.py`: Thực nghiệm so sánh và vẽ đồ thị
- `application/main.py`: Bài toán ứng dụng Dây cáp cầu treo
- `main.py`: Tệp chạy điều phối và tích hợp toàn dự án
- `requirements.txt`: Danh sách các thư viện cần thiết
- `README.md`: Tài liệu hướng dẫn dự án
"""
Tệp điều phối và tích hợp chính - Bài tập lớn Phương pháp số (Nhóm 2).
Phụ trách: SV7 (Lê Duy Long - Trưởng nhóm kỹ thuật)
"""
import numpy as np

def main():
    print("==========================================================")
    print("   CHƯƠNG TRÌNH TÍCH HỢP BÀI TẬP LỚN - NHÓM 2 (CHƯƠNG 3)  ")
    print("==========================================================")

    # 1. Thử nghiệm P1: Phương pháp Lặp đơn (SV1)
    print("\n--- 1. Kiểm tra module Lặp đơn (src/lap_don.py) ---")
    try:
        from src.lap_don import fixed_point
        g = lambda x: (5 * (x ** 3) + 3) / 20
        x_fp, k_fp, err_fp = fixed_point(g, x0=0.5, q=0.375, eps=1e-6, n_max=100)
        print(f"[Thành công] Nghiệm Lặp đơn x* = {x_fp:.6f} sau {k_fp} bước (sai số: {err_fp:.2e})")
    except Exception as e:
        print(f"[Chờ tích hợp từ SV1]: {e}")

    # 2. Thử nghiệm P3: Phương pháp Newton (SV2)
    print("\n--- 2. Kiểm tra module Newton (src/newton.py) ---")
    try:
        from src.newton import newton
        f = lambda x: (2 ** x) - 5 * x - 3
        df = lambda x: (2 ** x) * np.log(2) - 5
        x_nw, k_nw, err_nw = newton(f, df, x0=-0.5, eps=1e-6, n_max=100)
        print(f"[Thành công] Nghiệm Newton x* = {x_nw:.6f} sau {k_nw} bước (sai số: {err_nw:.2e})")
    except Exception as e:
        print(f"[Chờ tích hợp từ SV2]: {e}")

    # 3. Thử nghiệm P2 & P4: Các hàm bổ trợ (SV3)
    print("\n--- 3. Kiểm tra module Bổ trợ (src/extra.py) ---")
    try:
        from src.extra import check_contraction, fourier_start, newton_error
        print("[Thành công] Đã nạp đủ 3 hàm: check_contraction, fourier_start, newton_error.")
    except Exception as e:
        print(f"[Chờ tích hợp từ SV3]: {e}")

if __name__ == "__main__":
    main()






