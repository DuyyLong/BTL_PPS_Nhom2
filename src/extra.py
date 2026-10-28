# src/extra.py


def check_contraction(g, dg, a, b, n=1000):
  """Kiểm tra điều kiện hội tụ và ánh xạ đoạn cho phương pháp Lặp đơn.
  # Tính bước nhảy giữa các điểm chia mẫu trên đoạn [a, b]
  buoc_nhay = (b - a) / n
  q_lon_nhat = 0.0
  thoa_man_anh_xa = True

  # Vòng lặp duyệt qua các điểm chia để kiểm tra
  for i in range(n + 1):
    x = a + i * buoc_nhay

    # 1. Tìm hằng số lớn nhất q = max |g'(x)|
    gia_tri_dao_ham = abs(dg(x))
    if gia_tri_dao_ham > q_lon_nhat:
      q_lon_nhat = gia_tri_dao_ham

    # 2. Kiểm tra điều kiện ánh xạ vào đoạn g([a, b]) subset [a, b]
    gia_tri_ham_lap = g(x)
    if gia_tri_ham_lap < a or gia_tri_ham_lap > b:
      thoa_man_anh_xa = False

  # Kết quả hợp lệ khi thỏa mãn đồng thời hằng số q < 1 và bảo toàn đoạn [a, b]
  ket_qua_hop_le = (q_lon_nhat < 1.0) and thoa_man_anh_xa
  return ket_qua_hop_le, float(q_lon_nhat)
  
def fourier_start(f, d2f, a, b):
  """Chọn điểm xuất phát x0 theo điều kiện Fourier.

  - Require: f(x) là hàm gốc, d2f(x) là đạo hàm bậc hai, [a, b] là khoảng phân
  ly nghiệm (a < b).
  - Ensure: Trả về điểm xuất phát x0 kiểu float thỏa mãn f(x0)*f''(x0) > 0.
  - Định lý: Điều kiện hội tụ Fourier cho phương pháp Newton.
  """
  if a >= b:
    raise ValueError(
        "Lỗi: Khoảng [a, b] không hợp lệ (đầu mút a phải nhỏ hơn b)."
    )

  # Kiểm tra tại đầu mút trái a
  gia_tri_tai_a = f(a)
  dao_ham_bac_hai_tai_a = d2f(a)
  dieu_kien_tai_a = gia_tri_tai_a * dao_ham_bac_hai_tai_a

  # Kiểm tra tại đầu mút phải b
  gia_tri_tai_b = f(b)
  dao_ham_bac_hai_tai_b = d2f(b)
  dieu_kien_tai_b = gia_tri_tai_b * dao_ham_bac_hai_tai_b

  # Nếu đầu mút a thỏa mãn điều kiện Fourier thì chọn a
  if dieu_kien_tai_a > 0:
    return float(a)
  # Nếu đầu mút b thỏa mãn thì chọn b
  elif dieu_kien_tai_b > 0:
    return float(b)
  else:
    raise ValueError(
        "Lỗi: Không tìm thấy đầu mút nào thỏa mãn điều kiện Fourier"
        " f(x)*f''(x) > 0 trên đoạn [a, b]."
    )
def newton_error(x_k, x_truoc, m1, M2):
  """Đánh giá sai số bước lặp cho phương pháp Newton.
  # Bắt lỗi nếu m1 không hợp lệ (<= 0) 
  if m1 <= 0:
    raise ValueError(
        f"Lỗi: Cận m1 phải lớn hơn 0 để tránh chia cho số âm hoặc số 0 (giá trị"
        f" m1 hiện tại là {m1})."
    )

  # Tính khoảng cách giữa nghiệm hiện tại và nghiệm trước đó
  khoang_cach = abs(x_k - x_truoc)

  # Áp dụng công thức đánh giá sai số lý thuyết
  sai_so_uoc_luong = (M2 / (2 * m1)) * (khoang_cach**2)
  return float(sai_so_uoc_luong)
