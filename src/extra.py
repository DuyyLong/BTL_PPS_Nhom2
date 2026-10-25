
def check_contraction(g, dg, a, b, n_sample=1000):
  """Kiểm tra điều kiện co cho phương pháp Lặp đơn."""
  step_size = (b - a) / n_sample
  max_q = 0.0
  for i in range(n_sample + 1):
    x = a + i * step_size
    val = abs(dg(x))
    if val > max_q:
      max_q = val

  ok = max_q < 1.0
  return ok, float(max_q)

def fourier_start(f, d2f, a, b):
  """Chọn điểm xuất phát Fourier."""
  fa = f(a)
  d2fa = d2f(a)

  if fa * d2fa > 0:
    return float(a)
  else:
    return float(b)

def newton_error(x_k, x_prev, m1, M2):
  """Đánh giá sai số cho phương pháp Newton."""
  diff = abs(x_k - x_prev)
  if m1 == 0:
    return float(diff)
  return float((M2 / (2 * m1)) * (diff**2))
