"""
Bài toán ứng dụng: Dây cáp cầu treo (Chương 3 - Phương pháp số).
Phụ trách: Nguyễn Minh Quyết (SV6)
Nội dung:
    1. Mô hình hóa bài toán dây cáp cầu treo: a * cosh(L / (2a)) - a - d = 0.
    2. Tìm tham số a bằng phương pháp Newton và Lặp đơn (tự xây dựng hàm g thỏa điều
       kiện co, có kiểm tra bằng hàm P2).
    3. Kiểm tra điều kiện co của hàm g bằng hàm P2 (check_contraction).
    4. Tính chiều dài dây S = 2a * sinh(L / (2a)) và khảo sát S khi d thay đổi từ 5 đến 20 m.

Dữ liệu đề bài: nhịp L = 100 m, độ võng d = 10 m  =>  a ≈ 126,63 m, S ≈ 102,62 m.

Cách chạy:
    pytest                    -> chạy toàn bộ kiểm thử (PHẦN 3)
    python test_catenary.py   -> in kết quả + vẽ đồ thị khảo sát S theo d (PHẦN 4)

Cấu trúc file:
    PHẦN 1: các hàm của bài toán (f, f', g, g', S)
    PHẦN 2: thuật toán (Newton, Lặp đơn, check_contraction)
    PHẦN 3: kiểm thử pytest
    PHẦN 4: thực nghiệm khảo sát S theo d

Lưu ý: số hiệu "Thuat toan N" / "dong k" trong chú thích là số tạm,
       cần đổi cho khớp với pseudocode trong bài giảng.
"""
import math
import numpy as np
import pytest


# =====================================================================
# PHAN 1: CAC HAM CUA BAI TOAN
# =====================================================================
def f(a, L, d):
    """f(a) = a*cosh(L/(2a)) - a - d.

    Require: a > 0, L > 0, d > 0.
    Ensure : gia tri f(a) (so thuc).
    """
    return a * math.cosh(L / (2.0 * a)) - a - d


def df(a, L, d):
    """Dao ham f'(a) = cosh(x) - x*sinh(x) - 1, voi x = L/(2a). (Dung cho Newton)

    Require: a > 0, L > 0.
    Ensure : gia tri f'(a).
    """
    x = L / (2.0 * a)
    return math.cosh(x) - x * math.sinh(x) - 1.0


def g(a, L, d):
    """Ham lap don g(a), thoa: a = g(a)  <=>  f(a) = 0.

    Cach tim g: dung cong thuc cosh(2y) - 1 = 2*sinh(y)^2 voi y = L/(4a):
        a*(cosh(L/(2a)) - 1) = d   <=>   2a*sinh(L/(4a))^2 = d
        =>  sinh(L/(4a)) = sqrt(d/(2a))
        =>  a = L / (4*asinh(sqrt(d/(2a))))  =: g(a)

    Require: a > 0, L > 0, d > 0.
    Ensure : g(a).
    """
    return L / (4.0 * math.asinh(math.sqrt(d / (2.0 * a))))


def dg(a, L, d):
    """Dao ham g'(a) (dung de kiem tra g la anh xa co).

    Voi s = sqrt(d/(2a)), h = asinh(s):
        g'(a) = (L/4) * s / (2a * sqrt(1+s^2) * h^2)

    Require: a > 0.   Ensure: g'(a).
    """
    s = math.sqrt(d / (2.0 * a))
    h = math.asinh(s)
    return (L / 4.0) * s / (2.0 * a * math.sqrt(1.0 + s * s) * h * h)


def cable_length(a, L):
    """Chieu dai day S = 2a*sinh(L/(2a)).

    Require: a > 0, L > 0.   Ensure: S >= L.
    """
    if a <= 0 or L <= 0:
        raise ValueError("cable_length: can a > 0 va L > 0")
    return 2.0 * a * math.sinh(L / (2.0 * a))


# =====================================================================
# PHAN 2: CAC THUAT TOAN
# =====================================================================
def check_contraction(gfun, dgfun, lo, hi, n=2001):
    """Kiem tra g la anh xa co tren [lo, hi] (dieu kien P2):
         (i)  g(x) nam trong [lo, hi] voi moi x trong [lo, hi]
         (ii) q = max|g'(x)| < 1
    Cach lam: lay n diem deu tren [lo, hi] va kiem tra tai cac diem do.

    Require: lo < hi.
    Ensure : (ok, q) - ok=True neu thoa ca (i) va (ii); q la he so co.
    """
    if not lo < hi:
        raise ValueError("check_contraction: can lo < hi")
    xs = np.linspace(lo, hi, n)
    gs = np.array([gfun(x) for x in xs])
    q = float(np.max(np.abs([dgfun(x) for x in xs])))
    maps_into = bool(np.all(gs >= lo) and np.all(gs <= hi))
    return (maps_into and q < 1.0), q


def newton(func, dfunc, x0, tol=1e-12, max_iter=50):
    """Phuong phap Newton: x_{k+1} = x_k - f(x_k)/f'(x_k).

    Require: func (f), dfunc (f'), x0 (so bat dau), tol > 0, max_iter >= 1.
    Ensure : (x, so_buoc, lich_su) - nghiem xap xi, so buoc lap, danh sach x_k.
    Dung khi |x_{k+1} - x_k| <= tol*(1+|x_{k+1}|).
    Bao loi: f'(x)=0 (ZeroDivisionError); het max_iter (RuntimeError).
    """
    if tol <= 0 or max_iter < 1:                        # dong 1 - Thuat toan Newton
        raise ValueError("newton: can tol > 0 va max_iter >= 1")
    x = float(x0)                                       # dong 2 - Thuat toan Newton
    history = [x]
    for k in range(1, max_iter + 1):                    # dong 3 - Thuat toan Newton
        dfx = dfunc(x)
        if dfx == 0.0:                                  # dong 4 - Thuat toan Newton
            raise ZeroDivisionError("newton: f'(x)=0 tai x=%r" % x)
        x_new = x - func(x) / dfx                       # dong 5 - Thuat toan Newton
        history.append(x_new)
        if abs(x_new - x) <= tol * (1.0 + abs(x_new)):  # dong 6 - Thuat toan Newton
            return x_new, k, history                    # dong 7 - Thuat toan Newton
        x = x_new                                       # dong 8 - Thuat toan Newton
    raise RuntimeError("newton: het %d buoc lap ma chua hoi tu" % max_iter)


def fixed_point(gfun, x0, q, tol=1e-12, max_iter=500):
    """Lap don: x_{k+1} = g(x_k), voi g la anh xa co he so q (0 < q < 1).

    Require: gfun, x0 (nam trong khoang co), 0 < q < 1, tol > 0, max_iter >= 1.
    Ensure : (x, so_buoc, lich_su).
    Dieu kien dung (sai so hau nghiem): q/(1-q)*|x_k - x_{k-1}| <= tol
        => |x_k - nghiem| <= tol.
    Bao loi: q ngoai (0,1) (ValueError); het max_iter (RuntimeError).
    """
    if not (0.0 < q < 1.0):                             # dong 1 - Thuat toan lap don
        raise ValueError("fixed_point: can 0 < q < 1 (g phai la anh xa co)")
    if tol <= 0 or max_iter < 1:
        raise ValueError("fixed_point: can tol > 0 va max_iter >= 1")
    x = float(x0)                                       # dong 2 - Thuat toan lap don
    history = [x]
    for k in range(1, max_iter + 1):                    # dong 3 - Thuat toan lap don
        x_new = gfun(x)                                 # dong 4 - Thuat toan lap don
        history.append(x_new)
        if q / (1.0 - q) * abs(x_new - x) <= tol:       # dong 5 - Thuat toan lap don
            return x_new, k, history                    # dong 6 - Thuat toan lap don
        x = x_new                                       # dong 7 - Thuat toan lap don
    raise RuntimeError("fixed_point: het %d buoc lap ma chua hoi tu" % max_iter)


def bracket(L, d):
    """Tim khoang [lo, hi] chua nghiem: lo = 0.5*a0, hi = 2*a0, a0 = L^2/(8d).
    (a0 la nghiem xap xi khi xem day cap la parabol.)

    Require: L > 0, d > 0.
    Ensure : (lo, hi, a0) voi f(lo)*f(hi) < 0; neu khong thi nem ValueError.
    """
    if L <= 0 or d <= 0:
        raise ValueError("bracket: can L > 0 va d > 0")
    a0 = L * L / (8.0 * d)
    lo, hi = 0.5 * a0, 2.0 * a0
    if f(lo, L, d) * f(hi, L, d) >= 0:
        raise ValueError("bracket: f(lo)*f(hi) >= 0, khong dam bao co nghiem")
    return lo, hi, a0


def solve_catenary(L, d, method="newton", tol=1e-12):
    """Giai bai toan: tra ve a va S.

    Require: L > 0, d > 0, method la "newton" hoac "fixed_point".
    Ensure : dict {a, S, iters, method, q}.
    """
    lo, hi, a0 = bracket(L, d)
    q = None
    if method == "newton":
        a, it, _ = newton(lambda t: f(t, L, d), lambda t: df(t, L, d), a0, tol)
    elif method == "fixed_point":
        ok, q = check_contraction(lambda t: g(t, L, d),
                                  lambda t: dg(t, L, d), lo, hi)
        if not ok:
            raise ValueError("g khong la anh xa co tren [%g, %g] (q=%g)" % (lo, hi, q))
        a, it, _ = fixed_point(lambda t: g(t, L, d), a0, q, tol)
    else:
        raise ValueError("method phai la 'newton' hoac 'fixed_point'")
    return {"a": a, "S": cable_length(a, L), "iters": it, "method": method, "q": q}


# =====================================================================
# PHAN 3: KIEM THU (chay bang lenh: pytest)
# =====================================================================
L0, D0 = 100.0, 10.0


def _d_cho_nghiem(a_true, L=100.0):
    """Chon truoc a_true, tinh nguoc d de a_true la nghiem DUNG cua f."""
    return a_true * (math.cosh(L / (2 * a_true)) - 1.0)


# ---- Newton: 3 ca ----
def test_newton_vi_du_bai_giang():
    a, _, _ = newton(lambda t: f(t, L0, D0), lambda t: df(t, L0, D0), 125.0)
    assert a == pytest.approx(126.63, abs=0.01)
    assert abs(f(a, L0, D0)) < 1e-9
    assert cable_length(a, L0) == pytest.approx(102.62, abs=0.01)


def test_newton_nghiem_dung_tu_chon():
    d = _d_cho_nghiem(50.0)
    a, _, _ = newton(lambda t: f(t, L0, d), lambda t: df(t, L0, d), 40.0)
    assert a == pytest.approx(50.0, abs=1e-8)


def test_newton_ca_bien():
    with pytest.raises(ValueError):
        newton(lambda t: t, lambda t: 1.0, 1.0, tol=-1)
    with pytest.raises(ZeroDivisionError):                       # f'(0) = 0
        newton(lambda t: t * t + 1, lambda t: 2 * t, 0.0)
    with pytest.raises(RuntimeError):                            # vo nghiem
        newton(lambda t: t * t + 1, lambda t: 2 * t, 2.0, max_iter=3)


# ---- Lap don: 3 ca ----
def test_lap_don_vi_du_bai_giang():
    lo, hi, a0 = bracket(L0, D0)
    ok, q = check_contraction(lambda t: g(t, L0, D0), lambda t: dg(t, L0, D0), lo, hi)
    assert ok and q < 1
    a, _, _ = fixed_point(lambda t: g(t, L0, D0), a0, q)
    assert a == pytest.approx(126.63, abs=0.01)
    a_newton = newton(lambda t: f(t, L0, D0), lambda t: df(t, L0, D0), a0)[0]
    assert a == pytest.approx(a_newton, abs=1e-9)


def test_lap_don_nghiem_dung_tu_chon():
    d = _d_cho_nghiem(50.0)
    lo, hi, a0 = bracket(L0, d)
    ok, q = check_contraction(lambda t: g(t, L0, d), lambda t: dg(t, L0, d), lo, hi)
    assert ok
    a, _, _ = fixed_point(lambda t: g(t, L0, d), a0, q)
    assert a == pytest.approx(50.0, abs=1e-8)


def test_lap_don_ca_bien():
    with pytest.raises(ValueError):                              # q khong hop le
        fixed_point(lambda t: 2 * t, 1.0, q=2.0)
    with pytest.raises(RuntimeError):                            # het so buoc lap
        fixed_point(lambda t: 0.99 * t + 1.0, 0.0, q=0.99, tol=1e-15, max_iter=3)
    ok, q = check_contraction(lambda t: 2 * t, lambda t: 2.0, 1.0, 2.0)
    assert not ok and q == 2.0                                   # khong phai anh xa co


# ---- Ham tong hop ----
def test_dau_vao_sai():
    with pytest.raises(ValueError):
        bracket(-1.0, 10.0)
    with pytest.raises(ValueError):
        solve_catenary(100.0, 0.0)
    with pytest.raises(ValueError):
        solve_catenary(100.0, 10.0, method="abc")


@pytest.mark.parametrize("d", [5, 10, 15, 20])
def test_hai_phuong_phap_cho_cung_ket_qua(d):
    r1 = solve_catenary(L0, d, "newton")
    r2 = solve_catenary(L0, d, "fixed_point")
    assert r1["a"] == pytest.approx(r2["a"], abs=1e-8)
    assert abs(f(r1["a"], L0, d)) < 1e-8
    assert r1["S"] > L0


# =====================================================================
# PHAN 4: THUC NGHIEM (chay bang lenh: python test_catenary.py)
# =====================================================================
def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    L = 100.0
    r1 = solve_catenary(L, 10.0, "newton")
    r2 = solve_catenary(L, 10.0, "fixed_point")
    print("d = 10:")
    print("  Newton : a = %.6f  S = %.6f  (%d buoc)" % (r1["a"], r1["S"], r1["iters"]))
    print("  Lap don: a = %.6f  S = %.6f  (%d buoc, q = %.4f)"
          % (r2["a"], r2["S"], r2["iters"], r2["q"]))

    # Khao sat S khi d thay doi tu 5 den 20 m
    ds = np.linspace(5, 20, 31)
    A, S, S_parabol = [], [], []
    print("\n   d        a          S       S-L")
    for i, d in enumerate(ds):
        res = solve_catenary(L, d, "newton")
        A.append(res["a"])
        S.append(res["S"])
        S_parabol.append(L + 8 * d * d / (3 * L))   # xap xi parabol
        if i % 5 == 0:
            print("%5.1f %10.4f %10.4f %8.4f" % (d, res["a"], res["S"], res["S"] - L))

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].plot(ds, A, "o-")
    ax[0].set(xlabel="d (m)", ylabel="a (m)", title="Tham so a theo d")
    ax[1].plot(ds, S, "o-", label="S (day xich)")
    ax[1].plot(ds, S_parabol, "--", label="xap xi parabol")
    ax[1].set(xlabel="d (m)", ylabel="S (m)", title="Chieu dai day S theo d")
    ax[1].legend()
    for x in ax:
        x.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("khao_sat_S_theo_d.png", dpi=150)
    print("\nDa luu do thi: khao_sat_S_theo_d.png")


if __name__ == "__main__":
    main()
