"""
Tệp điều phối và tích hợp chính - Bài tập lớn Phương pháp số (Nhóm 2).
Đề tài: Chương 3 - Phương trình phi tuyến (Lặp đơn và Newton).
Phụ trách: SV7 (Lê Duy Long - Trưởng nhóm kỹ thuật)
"""

import numpy as np


def run_core_demos():
    """Chạy kiểm tra các module thuật toán lõi (P1, P2, P3, P4) và 3 bài toán bắt buộc."""
    print("\n" + "=" * 65)
    print(" PHẦN 1: KIỂM TRA CÁC MODULE THUẬT TOÁN LÕI (P1, P2, P3, P4)")
    print("=" * 65)

    # -----------------------------------------------------------------
    # [1] Bài toán 1: Lặp đơn (Ví dụ 3.2 trong đề bài)
    # -----------------------------------------------------------------
    print("\n[1] Bài toán 1: Giải f(x) = 5x^3 - 20x + 3 = 0 trên đoạn [0, 1] bằng Lặp đơn")
    g = lambda x: (5.0 * (x ** 3) + 3.0) / 20.0
    dg = lambda x: (15.0 * (x ** 2)) / 20.0

    q_est = 0.75
    try:
        from src.extra import check_contraction
        ok, q_est = check_contraction(g, dg, a=0.0, b=1.0, n_sample=1000)
        print(f"   + [P2 - SV3] Kiểm tra điều kiện co trên [0, 1]: ok = {ok}, hệ số co q ≈ {q_est:.4f}")
    except Exception as e:
        print(f"   + [P2 - SV3] Lỗi hoặc chờ tích hợp hàm check_contraction ({e})")

    try:
        from src.lap_don import fixed_point
        x_fp, k_fp, err_fp = fixed_point(g, x0=0.5, q=q_est, eps=1e-6, n_max=100)
        print(f"   + [P1 - SV1] Nghiệm Lặp đơn: x* = {x_fp:.6f} (Đáp số mẫu: 0.150858)")
        print(f"                Số bước lặp k = {k_fp}, Sai số ước lượng = {err_fp:.2e}")
    except Exception as e:
        print(f"   + [P1 - SV1] Lỗi hoặc chờ tích hợp hàm fixed_point ({e})")

    # -----------------------------------------------------------------
    # [2] Bài toán 2: Phương pháp Newton trên [-1, 0]
    # -----------------------------------------------------------------
    print("\n[2] Bài toán 2: Giải f(x) = 2^x - 5x - 3 = 0 trên đoạn [-1, 0] bằng Newton")
    f = lambda x: (2.0 ** x) - 5.0 * x - 3.0
    df = lambda x: (2.0 ** x) * np.log(2.0) - 5.0
    d2f = lambda x: (2.0 ** x) * (np.log(2.0) ** 2)

    x0_newton = -1.0
    try:
        from src.extra import fourier_start
        x0_newton = fourier_start(f, d2f, a=-1.0, b=0.0)
        print(f"   + [P4 - SV3] Điểm xuất phát Fourier tìm được trên [-1, 0]: x0 = {x0_newton}")
    except Exception as e:
        print(f"   + [P4 - SV3] Lỗi hoặc chờ tích hợp hàm fourier_start ({e})")

    try:
        from src.newton import newton
        from src.extra import newton_error
        x_nw, k_nw, err_nw = newton(f, df, x0=x0_newton, eps=1e-6, n_max=100)
        print(f"   + [P3 - SV2] Nghiệm Newton: x* = {x_nw:.6f} (Đáp số mẫu: -0.453996)")
        print(f"                Số bước lặp k = {k_nw}, Sai số bước cuối = {err_nw:.2e}")

        # Minh họa thêm hàm newton_error (P4) trên đoạn [-1, 0]
        # Trên [-1, 0]: m1 = min|f'(x)| = |2^0*ln(2) - 5| ≈ 4.3068, M2 = max|f''(x)| = (ln 2)^2 ≈ 0.4805
        m1_val = abs(df(0.0))
        M2_val = abs(d2f(0.0))
        err_bound = newton_error(x_nw, x_nw - err_nw, m1=m1_val, M2=M2_val)
        print(f"   + [P4 - SV3] Đánh giá sai số Newton qua m1, M2 (newton_error): {err_bound:.2e}")
    except Exception as e:
        print(f"   + [P3 - SV2] Lỗi hoặc chờ tích hợp hàm newton ({e})")

    # -----------------------------------------------------------------
    # [3] Bài toán 3: Kiểm tra Ca biên bắt buộc (R6)
    # -----------------------------------------------------------------
    print("\n[3] Bài toán 3 (Ca biên): Lặp đơn với q >= 1 và Newton với f'(x0) = 0")
    g_bad = lambda x: (20.0 * x - 3.0) / (5.0 * (x ** 2))
    dg_bad = lambda x: (-20.0 * x + 6.0) / (5.0 * (x ** 3))
    try:
        from src.extra import check_contraction
        ok_bad, q_bad = check_contraction(g_bad, dg_bad, a=0.2, b=1.0, n_sample=1000)
        print(f"   + [Ca biên Lặp đơn] g(x) = (20x-3)/(5x^2): ok = {ok_bad}, q ≈ {q_bad:.2f} (>= 1 -> Không hội tụ)")
    except Exception as e:
        print(f"   + [Ca biên Lặp đơn] Đã bắt lỗi thành công: {e}")

    try:
        from src.newton import newton
        newton(f=lambda x: x**2 - 1.0, df=lambda x: 2.0 * x, x0=0.0, eps=1e-6, n_max=100)
    except Exception as e:
        print(f"   + [Ca biên Newton] Khi f'(x0) = 0, hàm đã bắt lỗi đúng yêu cầu R6: {e}")


def run_experiments_demo():
    """Chạy tích hợp phần Thực nghiệm so sánh và vẽ đồ thị của SV5."""
    print("\n" + "=" * 65)
    print(" PHẦN 2: THỰC NGHIỆM SO SÁNH & VẼ ĐỒ THỊ (SV5 - experiments/compare.py)")
    print("=" * 65)
    try:
        import experiments.compare as exp_module
        if hasattr(exp_module, "main"):
            exp_module.main()
    except Exception as e:
        print(f"   + [SV5] Chờ tích hợp module thực nghiệm từ experiments/compare.py ({e})")


def run_application_demo():
    """Chạy tích hợp Bài toán ứng dụng dây cáp cầu treo của SV6."""
    print("\n" + "=" * 65)
    print(" PHẦN 3: BÀI TOÁN ỨNG DỤNG DÂY CÁP CẦU TREO (SV6 - application/main.py)")
    print("=" * 65)
    try:
        import application.main as app_module
        if hasattr(app_module, "main"):
            app_module.main()
    except Exception as e:
        print(f"   + [SV6] Chờ tích hợp bài toán dây cáp từ application/main.py ({e})")


def main():
    print("*****************************************************************")
    print("*      HỆ THỐNG TÍCH HỢP BÀI TẬP LỚN PHƯƠNG PHÁP SỐ - NHÓM 2    *")
    print("*      Chủ đề: Chương 3 - Phương pháp Lặp đơn & Newton          *")
    print("*      Trưởng nhóm kỹ thuật (SV7): Lê Duy Long                  *")
    print("*****************************************************************")

    run_core_demos()
    run_experiments_demo()
    run_application_demo()

    print("\n" + "=" * 65)
    print(" HOÀN TẤT CHẠY TÍCH HỢP HỆ THỐNG. ĐỂ CHẠY KIỂM THỬ (SV4), GÕ: pytest")
    print("=" * 65)


if __name__ == "__main__":
    main()
