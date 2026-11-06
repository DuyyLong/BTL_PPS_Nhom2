"""
Bài toán ứng dụng: Dây cáp cầu treo (Chương 3 - Phương pháp số).
Phụ trách: Nguyễn Minh Quyết (SV6)
Nội dung:
  1. Mô hình hóa bài toán dây cáp cầu treo: a * cosh(L / (2a)) - a - d = 0.
  2. Tìm tham số a bằng phương pháp Newton và Lặp đơn (gọi từ package lõi src/).
  3. Kiểm tra điều kiện co của hàm g bằng hàm P2 (src.extra.check_contraction).
  4. Tính chiều dài dây S = 2a * sinh(L / (2a)) và khảo sát S khi d thay đổi từ 5 đến 20 m.
  5. Bộ kiểm thử pytest tích hợp đầy đủ các ca biên và ca bài giảng.

Dữ liệu đề bài: nhịp L = 100 m, độ võng d = 10 m => a ≈ 126.63 m, S ≈ 102.62 m.
"""
import math
import numpy as np
import pytest

# Kết hợp: Import các hàm lõi chuẩn từ package src/ của nhóm (SV1, SV2, SV3)
from src.lap_don import fixed_point
from src.newton import newton
from src.extra import check_contraction


# =============================================================================
# PHAN 1: CAC HAM CUA BAI TOAN DAY CAP CAU TREO
# =============================================================================
def f(a, L, d):
    """f(a) = a*cosh(L/(2a)) - a - d."""
    return a * math.cosh(L / (2.0 * a)) - a - d


def df(a, L, d):
    """Đạo hàm f'(a) dùng cho phương pháp Newton."""
    x = L / (2.0 * a)
    return math.cosh(x) - x * math.sinh(x) - 1.0


def g(a, L, d):
    """Hàm lặp đơn g(a) tương đương với phương trình f(a) = 0."""
    return L / (4.0 * math.asinh(math.sqrt(d / (2.0 * a))))


def dg(a, L, d):
    """Đạo hàm g'(a) dùng để kiểm tra điều kiện ánh xạ co."""
    s = math.sqrt(d / (2.0 * a))
    h = math.asinh(s)
    return (L / 4.0) * s / (2.0 * a * math.sqrt(1.0 + s * s) * h * h)


def cable_length(a, L):
    """Tính chiều dài dây S = 2a * sinh(L / (2a))."""
    if a <= 0 or L <= 0:
        raise ValueError("cable_length: can a > 0 va L > 0")
    return 2.0 * a * math.sinh(L / (2.0 * a))


def bracket(L, d):
    """Tìm khoảng [lo, hi] chứa nghiệm dựa trên xấp xỉ parabol a0 = L^2 / (8d)."""
    if L <= 0 or d <= 0:
        raise ValueError("bracket: can L > 0 va d > 0")
    a0 = L * L / (8.0 * d)
    lo, hi = 0.5 * a0, 2.0 * a0
    if f(lo, L, d) * f(hi, L, d) >= 0:
        raise ValueError("bracket: f(lo)*f(hi) >= 0, khong dam bao co nghiem")
    return lo, hi, a0


# =============================================================================
# PHAN 2: GIAI BAI TOAN TICH HOP DUNG THU VIEN LOI SRC/
# =============================================================================
def solve_catenary(L, d, method="newton", eps=1e-10, n_max=500):
    """Giải bài toán cầu treo bằng cách gọi trực tiếp thuật toán từ src/."""
    lo, hi, a0 = bracket(L, d)
    q = None
    
    if method == "newton":
        # Gọi hàm newton từ src.newton (SV2)
        a, iters, err = newton(
            f=lambda t: f(t, L, d),
            df=lambda t: df(t, L, d),
            x0=a0,
            eps=eps,
            n_max=n_max,
        )
    elif method == "fixed_point":
        # Kiểm tra điều kiện co bằng hàm từ src.extra (SV3)
        ok, q = check_contraction(
            g=lambda t: g(t, L, d),
            dg=lambda t: dg(t, L, d),
            a=lo,
            b=hi,
            n_sample=2000,
        )
        if not ok:
            raise ValueError("g không là ánh xạ co trên [%g, %g] (q=%g)" % (lo, hi, q))
        
        # Gọi hàm fixed_point từ src.lap_don (SV1)
        a, iters, err = fixed_point(
            g=lambda t: g(t, L, d),
            x0=a0,
            q=q,
            eps=eps,
            n_max=n_max,
        )
    else:
        raise ValueError("method phải là 'newton' hoặc 'fixed_point'")
        
    return {
        "a": a,
        "S": cable_length(a, L),
        "iters": iters,
        "err": err,
        "method": method,
        "q": q,
    }


# =============================================================================
# PHAN 3: BO KIEM THU PYTEST TICH HOP CHO BAI TOAN UNG DUNG
# =============================================================================
L0, D0 = 100.0, 10.0

def _d_cho_nghiem(a_true, L=100.0):
    """Hàm phụ trợ tạo dữ liệu kiểm thử chính xác."""
    return a_true * (math.cosh(L / (2.0 * a_true)) - 1.0)


def test_newton_vi_du_bai_giang():
    """Kiểm tra phương pháp Newton với dữ liệu chuẩn của bài giảng."""
    res = solve_catenary(L0, D0, "newton")
    assert res["a"] == pytest.approx(126.63, abs=0.01)
    assert abs(f(res["a"], L0, D0)) < 1e-9
    assert res["S"] == pytest.approx(102.62, abs=0.01)


def test_lap_don_vi_du_bai_giang():
    """Kiểm tra phương pháp Lặp đơn với dữ liệu chuẩn của bài giảng."""
    res = solve_catenary(L0, D0, "fixed_point")
    assert res["q"] < 1.0
    assert res["a"] == pytest.approx(126.63, abs=0.01)


def test_hai_phuong_phap_cho_cung_ket_qua():
    """So sánh kết quả giữa Newton và Lặp đơn phải khớp nhau."""
    r1 = solve_catenary(L0, 10.0, "newton")
    r2 = solve_catenary(L0, 10.0, "fixed_point")
    assert r1["a"] == pytest.approx(r2["a"], abs=1e-8)


# =============================================================================
# PHAN 4: THUC NGHIEM & KHAO SAT DO THI
# =============================================================================
def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    L = 100.0
    r1 = solve_catenary(L, 10.0, "newton")
    r2 = solve_catenary(L, 10.0, "fixed_point")
    print("=" * 65)
    print(" KẾT QUẢ BÀI TOÁN DÂY CÁP CẦU TREO (SV6 - Nguyễn Minh Quyết)")
    print("=" * 65)
    print(f"  d = 10m:")
    print(f"    Newton  : a = {r1['a']:.6f}  S = {r1['S']:.6f}  ({r1['iters']} bước, err = {r1['err']:.2e})")
    print(f"    Lập đơn : a = {r2['a']:.6f}  S = {r2['S']:.6f}  ({r2['iters']} bước, q = {r2['q']:.4f}, err = {r2['err']:.2e})")

    # Khảo sát S khi d thay đổi từ 5 đến 20 m
    ds = np.linspace(5, 20, 31)
    A, S, S_parabol = [], [], []
    print("\n  Khảo sát thay đổi độ võng d:")
    print("    d (m)      a (m)      S (m)     S - L (m)")
    print("-" * 45)
    for i, d in enumerate(ds):
        res = solve_catenary(L, d, "newton")
        A.append(res["a"])
        S.append(res["S"])
        S_parabol.append(L + 8 * d * d / (3 * L))  # Xấp xỉ parabol
        if i % 5 == 0:
            print(f"{d:5.1f} {res['a']:10.4f} {res['S']:10.4f} {res['S'] - L:10.4f}")

    # Vẽ và xuất đồ thị thực nghiệm
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].plot(ds, A, "o-", color="blue")
    ax[0].set(xlabel="d (m)", ylabel="a (m)", title="Tham số a theo độ võng d")
    ax[0].grid(True)

    ax[1].plot(ds, S, "o-", color="green", label="S (Dây xích)")
    ax[1].plot(ds, S_parabol, "--r", label="Xấp xỉ Parabol")
    ax[1].set(xlabel="d (m)", ylabel="S (m)", title="Chiều dài cáp S theo d")
    ax[1].legend()
    ax[1].grid(True)

    plt.tight_layout()
    plt.savefig("application_bridge.png", dpi=150)
    plt.close(fig)
    print("\n[SV6] Đã xuất thành công biểu đồ khảo sát vào file: application_bridge.png")
    print("=" * 65)


if __name__ == "__main__":
    main()
