
"""
Thực nghiệm so sánh phương pháp Lặp đơn và phương pháp Newton (Chương 3).
Phụ trách: Đỗ Minh Chiến (SV5)
"""

import numpy as np
import matplotlib.pyplot as plt
from src.lap_don import fixed_point
from src.newton import newton
from src.extra import check_contraction


def analyze_convergence(x_history, x_star):
    """Tính mảng sai số e_k và các tỉ số đánh giá bậc hội tụ."""
    errors = np.abs(x_history - x_star)

    with np.errstate(divide='ignore', invalid='ignore'):
        ratio_linear = errors[1:] / errors[:-1]
        ratio_quadratic = errors[1:] / (errors[:-1]**2)

    return errors, ratio_linear, ratio_quadratic


def main():

    print("--- [THỰC NGHIỆM 1] SO SÁNH SỐ BƯỚC LẶP VÀ ĐỒ THỊ SAI SỐ (THANG LOG) ---")

    # Bài toán chuẩn theo đề bài Nhóm 2: f(x) = 5x^3 - 20x + 3 = 0 trên [0, 1]
    f = lambda x: 5.0 * (x ** 3) - 20.0 * x + 3.0
    df = lambda x: 15.0 * (x ** 2) - 20.0
    g = lambda x: (5.0 * (x ** 3) + 3.0) / 20.0
    dg = lambda x: (15.0 * (x ** 2)) / 20.0

    x_star = 0.150858  # Nghiệm mẫu chính xác từ đề bài
    x0 = 0.5
    eps = 1e-12

    _, q = check_contraction(g, dg, a=0.0, b=1.0)

    # Chạy lưu vết qua từng bước lặp bằng các hàm chuẩn của nhóm (SV1 & SV2)

    # Lặp đơn
    hist_ld = [x0]
    x_cur = x0
    factor = q / (1.0 - q) if q > 0 else 1.0

    for _ in range(100):
        x_nxt = g(x_cur)
        hist_ld.append(x_nxt)

        if factor * abs(x_nxt - x_cur) <= eps:
            break

        x_cur = x_nxt

    hist_ld = np.array(hist_ld)

    # Newton
    hist_nw = [x0]
    x_cur = x0

    for _ in range(100):
        df_val = df(x_cur)

        if df_val == 0:
            break

        x_nxt = x_cur - f(x_cur) / df_val
        hist_nw.append(x_nxt)

        if abs(x_nxt - x_cur) < eps:
            break

        x_cur = x_nxt

    hist_nw = np.array(hist_nw)

    err_ld, _, _ = analyze_convergence(hist_ld, x_star)
    err_nw, _, _ = analyze_convergence(hist_nw, x_star)

    # Vẽ đồ thị
    plt.figure(figsize=(8, 5))
    plt.plot(
        range(len(err_ld)), err_ld,
        label='Lặp đơn (Bậc 1)',
        marker='o',
        linestyle='--',
        linewidth=2
    )
    plt.plot(
        range(len(err_nw)), err_nw,
        label='Newton (Bậc 2)',
        marker='s',
        linewidth=2
    )

    plt.yscale('log')  # Thang log theo yêu cầu đề bài
    plt.xlabel('Số bước lặp k')
    plt.ylabel('Sai số tuyệt đối |x_k - x*| (Thang Log)')
    plt.title('Thực nghiệm 1: So sánh tốc độ hội tụ Lặp đơn và Newton')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig("experiments_convergence.png", dpi=150)
    plt.close()

    print("-> Đã vẽ và lưu đồ thị thành công vào file: experiments_convergence.png")

    print("\n--- [THỰC NGHIỆM 2] KHẢO SÁT NEWTON VỚI NGHIỆM BỘI f(x) = (x - 1)^2 * (x + 2) ---")

    f_boi = lambda x: ((x - 1.0) ** 2) * (x + 2.0)
    df_boi = lambda x: 3.0 * ((x ** 2) - 1.0)
    x_star_boi = 1.0

    hist_boi = [1.5]
    x_cur = 1.5

    for _ in range(20):
        df_v = df_boi(x_cur)

        if df_v == 0:
            break

        x_nxt = x_cur - f_boi(x_cur) / df_v
        hist_boi.append(x_nxt)

        if abs(x_nxt - x_cur) < 1e-10:
            break

        x_cur = x_nxt

    hist_boi = np.array(hist_boi)

    err_boi, ratio_lin, ratio_quad = analyze_convergence(
        hist_boi, x_star_boi
    )

    print(
        f"{'Bước k':<10} | "
        f"{'|e_{k+1}| / |e_k| (Bậc 1 -> 0.5)':<32} | "
        f"{'|e_{k+1}| / |e_k|^2 (Bậc 2)':<32}"
    )
    print("-" * 80)

    for k in range(len(ratio_lin)):
        r1 = f"{ratio_lin[k]:.4f}"
        r2 = (
            f"{ratio_quad[k]:.4f}"
            if ratio_quad[k] < 1000
            else "Rất lớn (Vô cực)"
        )

        print(f"{k:<10} | {r1:<32} | {r2}")

if __name__ == "__main__":
    main()
