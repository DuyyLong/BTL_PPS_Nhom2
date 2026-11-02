import math
import numbers
class ConvergenceError(RuntimeError, ValueError):
    """Loi khi phuong phap lap don chua dat do chinh xac eps sau n_max buoc."""
def fixed_point(g, x0, q, eps, n_max) -> tuple[float, int, float]:
    """Giai gan dung phuong trinh x = g(x) bang phuong phap lap don.
    Ten thuat toan: Thuat toan lap don (Muc 3.3), dung theo danh gia sai so
    qua he so co q - cong thuc (3.7): |x_k - x*| <= q/(1-q) * |x_k - x_{k-1}|.
    Require:
        g     : ham lap thoa Dinh ly 3.2 tren [a, b] (|g'(x)| <= q < 1,
                g([a, b]) chua trong [a, b]).
        x0    : xap xi ban dau thuoc (a, b).
        q     : he so co, 0 < q < 1.
        eps   : do chinh xac yeu cau, eps > 0.
        n_max : so buoc lap toi da, so nguyen >= 1.
    Ensure:
        (x, k, err): x la nghiem gan dung x_k, k la so buoc da lap,
        err = q/(1-q) * |x_k - x_{k-1}| <= eps.
    Raises:
        TypeError: g khong phai ham.
        ValueError: vi pham dieu kien ap dung hoac g(x) tran so / NaN / Inf.
        ConvergenceError: het n_max buoc ma van err > eps.
    # Kiem tra dieu kien ap dung (R6)
    if not callable(g):
        raise TypeError("'g' phai la mot ham.")
    if not isinstance(x0, numbers.Real) or not math.isfinite(x0):
        raise ValueError(f"'x0' phai la so thuc huu han, nhan duoc x0 = {x0}.")
    if not isinstance(q, numbers.Real) or not 0 < q < 1:
        raise ValueError(f"He so co 'q' phai thoa 0 < q < 1, nhan duoc q = {q}.")
    if not isinstance(eps, numbers.Real) or not eps > 0:
        raise ValueError(f"'eps' phai lon hon 0, nhan duoc eps = {eps}.")
    if isinstance(n_max, bool) or not isinstance(n_max, numbers.Integral) or n_max < 1:
        raise ValueError(f"'n_max' phai la so nguyen >= 1, nhan duoc n_max = {n_max}.")
    x_prev = float(x0)                          # dong 1 - Thuat toan lap don: x_{k-1} <- x0
    factor = q / (1 - q)                        # dong 2 - Thuat toan lap don: he so q/(1-q)
    for k in range(1, int(n_max) + 1):          # dong 3 - Thuat toan lap don: for k = 1..n_max
        try:
            x_curr = float(g(x_prev))           # dong 4 - Thuat toan lap don: x_k <- g(x_{k-1})
        except (OverflowError, ZeroDivisionError, ValueError) as exc:
            raise ValueError(f"Khong tinh duoc g(x) tai buoc k = {k} (day lap phan ky?): {exc}") from exc
        if not math.isfinite(x_curr):
            raise ValueError(f"g(x) = {x_curr} tai buoc k = {k}: day lap phan ky.")
        err = factor * abs(x_curr - x_prev)     # dong 5 - Thuat toan lap don: err <- q/(1-q)*|x_k - x_{k-1}|
        if err <= eps:                          # dong 6 - Thuat toan lap don: if err <= eps
            return x_curr, k, err               # dong 7 - Thuat toan lap don: return (x_k, k, err)
        x_prev = x_curr                         # dong 8 - Thuat toan lap don: x_{k-1} <- x_k

    raise ConvergenceError(                     # dong 9 - Thuat toan lap don: bao loi het n_max buoc
        f"Lap don khong hoi tu sau n_max = {n_max} buoc (err = {err:.3e} > eps = {eps:.3e})."
    )
