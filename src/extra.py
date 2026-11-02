def check_contraction(g, dg, a, b, n_sample=1000) -> tuple[bool, float]:
    """
    Kiểm tra điều kiện hội tụ và ánh xạ đoạn cho phương pháp Lặp đơn.
    Tên thuật toán trong bài giảng: Điều kiện hội tụ phương pháp lặp đơn (Định lý 3...)
    
    Require:
        - g: Hàm lặp g(x) (callable).
        - dg: Đạo hàm g'(x) của hàm lặp (callable).
        - a, b: Hai đầu mút của đoạn [a, b] với a < b (float).
        - n_sample: Số khoảng chia lấy mẫu trên đoạn [a, b] (int, mặc định 1000).
        
    Ensure:
        - tuple[bool, float]: (ket_qua_hop_le, q_lon_nhat)
            + ket_qua_hop_le: True nếu g([a, b]) thuộc [a, b] và q < 1, ngược lại False
            + q_lon_nhat: Hệ số co ước lượng q = max |g'(x)| trên [a, b].
    """
    if a >= b:
        raise ValueError("Lỗi: Khoảng [a, b] không hợp lệ (đầu mút a phải nhỏ hơn b)")
    if n_sample <= 0:
        raise ValueError("Lỗi: Số mẫu n_sample phải là số nguyên dương.")
        
    # Tính bước nhảy dùng tham số n_sample đúng chuẩn chữ ký hàm R4
    buoc_nhay = (b - a) / n_sample
    q_lon_nhat = 0.0
    thoa_man_anh_xa = True
    
    for i in range(n_sample + 1):
        x = a + i * buoc_nhay
        
        # 1. Tìm hằng số lớn nhất q = max |g'(x)|
        gia_tri_dao_ham = abs(dg(x))
        if gia_tri_dao_ham > q_lon_nhat:
            q_lon_nhat = gia_tri_dao_ham
            
        # 2. Kiểm tra điều kiện ánh xạ vào đoạn g([a, b]) subset [a, b]
        gia_tri_ham_lap = g(x)
        if gia_tri_ham_lap < a or gia_tri_ham_lap > b:
            thoa_man_anh_xa = False
            
    ket_qua_hop_le = (q_lon_nhat < 1.0) and thoa_man_anh_xa
    return bool(ket_qua_hop_le), float(q_lon_nhat)

def fourier_start(f, d2f, a, b) -> float:
    """
    Chọn điểm xuất phát x0 theo điều kiện Fourier f(x0)*f''(x0) > 0.
    Tên thuật toán trong bài giảng: Điều kiện hội tụ Fourier cho phương pháp Newton.
    
    Require:
        - f: Hàm số f(x) (callable).
        - d2f: Đạo hàm bậc hai f''(x) (callable).
        - a, b: Hai đầu mút của đoạn phân ly nghiệm [a, b] với a < b (float).
        
    Ensure:
        - float: Điểm xuất phát x0 (a hoặc b) thỏa mãn f(x0)*f''(x0) > 0.
    """
    if a >= b:
        raise ValueError(
            "Lỗi: Khoảng [a, b] không hợp lệ (đầu mút a phải nhỏ hơn b)."
        )
        
    gia_tri_tai_a = f(a)
    dao_ham_bac_hai_tai_a = d2f(a)
    dieu_kien_tai_a = gia_tri_tai_a * dao_ham_bac_hai_tai_a
    
    gia_tri_tai_b = f(b)
    dao_ham_bac_hai_tai_b = d2f(b)
    dieu_kien_tai_b = gia_tri_tai_b * dao_ham_bac_hai_tai_b
    
    if dieu_kien_tai_a > 0:
        return float(a)
    elif dieu_kien_tai_b > 0:
        return float(b)
    else:
        raise ValueError(
            "Lỗi: Không tìm thấy đầu mút nào thỏa mãn điều kiện Fourier "
            "\"f(x)*f''(x) > 0 trên đoạn [a, b].\""
        )


def newton_error(x_k, x_prev, m1, M2) -> float:
    """
    Đánh giá sai số bước lặp cho phương pháp Newton qua m1, M2.
    Tên thuật toán trong bài giảng: Đánh giá sai số phương pháp Newton (Chương 3).
    
    Require:
        - x_k: Nghiệm xấp xỉ tại bước lặp hiện tại k (float).
        - x_prev: Nghiệm xấp xỉ tại bước lặp trước đó k-1 (float).
        - m1: Cận dưới của |f'(x)| trên [a, b], m1 > 0 (float).
        - M2: Cận trên của |f''(x)| trên [a, b], M2 >= 0 (float).
        
    Ensure:
        - float: Sai số ước lượng (M2 / (2 * m1)) * |x_k - x_prev|^2.
    """
    if m1 <= 0:
        raise ValueError(
            f"Lỗi: Cận m1 phải lớn hơn 0 để tránh chia cho số âm hoặc số 0 (giá trị m1 hiện tại là {m1})."
        )
    if M2 < 0:
        raise ValueError(
            f"Lỗi: Cận M2 phải không âm (M2 >= 0, hiện tại là {M2})."
        )
        
    khoang_cach = abs(x_k - x_prev)
    sai_so_uoc_luong = (M2 / (2 * m1)) * (khoang_cach ** 2)
    return float(sai_so_uoc_luong)
