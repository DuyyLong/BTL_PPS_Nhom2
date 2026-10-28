from typing import Callable
import math
class ConvergenceError
def fixed_point(
  g: Callable[[float], float],
  x0: float,
  q: float,
  eps: float,
  n_max: int,
) -> tuple[float, int, float]:
  if not callalbe(g) :
    raise TypeError("Tham số g phải là 1 hàm khả gọi.")
    if not isintance(x0, (int, float)) or mathisnan(x0) or math.isinf(x0):
      raise ValueError(f" Điểm khởi tạo x0 k hợp lệ: {x0}.")
      if not isintance(q, (int, float)) or math.isnan(q) or not (0.0 < q < 1.0):
        raise ValueError(f"Hệ số co 'q' phải thỏa mãn 0 < q < 1 (Định lý 3.2), nhận được q = {q}."
                        )
if not isinstance(eps, (int, float)) or math.isnan(eps) or eps <= 0.0:
        raise ValueError(f"Độ chính xác 'eps' phải lớn hơn 0, nhận được eps = {eps}.")
    if not isinstance(n_max, int) or isinstance(n_max, bool) or n_max < 1:
        raise ValueError(
            f"Số bước lặp tối đa 'n_max' phải là số nguyên dương >= 1, nhận được n_max = {n_max}."
        )
      x_prev: float = float(x0)
      factor: float = q / (1.0 - q)
for k in range(1, n_max + 1):
  x_curr: float = float(g(x_prev))
   if math.isnan(x_curr) or math.isinf(x_curr):
            raise ValueError(
                f"Giá trị hàm lặp g(x) tại bước k = {k} không xác định (NaN/Inf)."
            )
     err: float = factor * abs(x_curr - x_prev)
 if err <= eps:
   return x_curr, k, err 
x_prev = x_curr
  raise ConvergenceError(
        f"Phương pháp lặp đơn không hội tụ sau n_max = {n_max} bước lặp "
        f"(sai số cuối cùng err = {err:.6e} > eps = {eps:.6e})."
    )
