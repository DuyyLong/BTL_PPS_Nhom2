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
