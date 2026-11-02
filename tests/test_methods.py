# File kiem thu pytest - Phu trach: Nguyen Thu Hien (SV4)
import math
import pytest
from src.lap_don import fixed_point
from src.newton import newton
from src.extra import check_contraction
def test_fixed_point_vi_du_bat_buoc():
    "Kiểm tra lặp đơn với f(x) = 5x^3 - 20x + 3."
    g = lambda x: (5 * x**3 + 3) / 20
    x, k, err = fixed_point(
        g=g,
        x0=0.0,
        q=0.75,
        eps=1e-8,
        n_max=1000,
    )
    assert abs(x - 0.150858) < 1e-5
    assert k > 0
    assert math.isfinite(err)
def test_newton_vi_du_bat_buoc():
    """Kiểm tra Newton với f(x) = 2^x - 5x - 3."""
    f = lambda x: 2**x - 5 * x - 3
    df = lambda x: math.log(2) * 2**x - 5
    x, k, err = newton(
        f=f,
        df=df,
        x0=-0.5,
        eps=1e-8,
        n_max=100,
    )
    assert abs(x - (-0.453996)) < 1e-5
    assert k > 0
    assert math.isfinite(err)
def test_fixed_point_tu_choi_q_bang_1():
    """Lặp đơn phải từ chối q=1 vì yêu cầu q < 1."""
    with pytest.raises(ValueError):
        fixed_point(
            g=lambda x: x,
            x0=0.5,
            q=1.0,
            eps=1e-8,
            n_max=100,
        )
def test_check_contraction_ca_bien_khong_co():
    """Kiểm tra hàm g bắt buộc có q >= 1."""
    g = lambda x: (20 * x - 3) / (5 * x**2)
    dg = lambda x: (6 - 20 * x) / (5 * x**3)
    ok, q = check_contraction(
        g=g,
        dg=dg,
        a=0.1,
        b=1.0,
        n_sample=1000,
    )
    assert q >= 1.0
    assert ok is False
def test_newton_bao_loi_khi_dao_ham_tai_x0_bang_0():
    """Newton phải báo lỗi nếu f'(x0)=0."""
    with pytest.raises((ValueError, ZeroDivisionError)):
        newton(
            f=lambda x: x**2 + 1,
            df=lambda x: 2 * x,
            x0=0.0,
            eps=1e-8,
            n_max=100,
        )
