from typing import Callable, Tuple
import math
class ConvergenceError:
    def newton(
        f: Callable[[float], float],
        Df: Callable[[float], float],
        x0: float,
        n_max: int
    )-> tuple[float, int, float]:
        Require:
        -f: hàm số f(x) cần tìm nghiệm (Callable)
        -Df: đạo hàm f`(x) của hàm số (Callable)
        -x0: Giá trị dự đoán ban đầu (float)
        -eps: sai số cho phép của phương pháp(float,>0)
        -n_max: số bước lặp lớn nhất(int,>=1)
        Ensure:
        -Trả về tuple gồm (x, k, err) trong đó:
         +x: Nghiệm gần đúng tại bước lặp thứ i
         +i: số bước lặp
      +err: sai số tại bước lặp thứ i
        Tên thuật toán trong bài giảng: Phương pháp newton(Algorithm 5).
     # Kiểm tra tính hợp lệ của hàm số và đạo hàm 
        if not callable(f) or not callable(Df):
            raise TypeError("Tham số f và Df phải là các hàm khả gọi.")
     # Kiểm tra điểm khởi tạo x0
        if not isinstance(x0, (int, float)) or math.isnan(x0) or math.isinf(x0):
            raise ValueError(f"Điểm khởi tạo x0 không hợp lệ: {x0}.")
     # Kiểm tra sai số eps
        if not isinstance(eps, (int, float)) or math.isnan(eps) or eps <= 0.0:
            raise ValueError(f"Độ chính xác 'eps' phải lớn hơn 0, nhận được eps = {eps}.")
     # Kiểm tra số bước lặp tối đa n_max
        if not isinstance(n_max, int) or isinstance(n_max, bool) or n_max < 1:
            raise ValueError(f"Số bước lặp tối đa 'n_max' phải là số nguyên dương >= 1, nhận được n_max = {n_max}.")
         x_k = float(x0)
     # dong 1 - Thuat toan: Vong lap qua cac buoc lap tu 1 den n_max
        for k in range(1, n_max + 1):
     # dong 2 - Thuat toan: Tinh gia tri dao ham tai diem x_k de kiem tra dieu kien bien chia cho 0      
        df_val = df(x_k)
          if math.isnan(df_val) or math.isinf(df_val):
               raise ValueError(f"Giá trị đạo hàm df tại x_{k-1} = {x_k} không xác định (NaN/Inf).")
          if df_val == 0.0: 
               raise ValueError(f"Lỗi: Đạo hàm tại x_{k-1} = {x_k} bằng 0. Không thể tiếp tục phương pháp Newton.")
          f_val = f(x_k)
          if math.isnan(f_val) or math.isinf(f_val):
               raise ValueError(f"Giá trị hàm số f tại x_{k-1} = {x_k} không xác định (NaN/Inf).")
    # dong 2 (tiep) - Thuat toan: Cap nhat x_new (x_next) theo cong thuc Newton
          x_next = x_k - f_val / df_val
         if math.isnan(x_next) or math.isinf(x_next):
            raise ValueError(f"Giá trị tính toán xấp xỉ tại bước k = {k} không xác định (NaN/Inf).")
     # dong 3 - Thuat toan: Tinh sai so err giua hai buoc lap lien tiep
          err = abs(x_next - x_k)
        
     # dong 4, 5 - Thuat toan: Kiem tra dieu kien dung (err < eps)
         if err < eps or abs(f(x_next)) < eps:
     # dong 10 - Thuat toan: Return ket qua (k, err, x_new)
            return x_next, k, err
            
     # dong 7 - Thuat toan: Gan x = x_new cho buoc lap tiep theo
        x_k = x_next
        
     # dong 10 (truong hop vuot qua n_max ma chua dat sai so)
      raise ConvergenceError(
        f"Phương pháp Newton không hội tụ sau n_max = {n_max} bước lặp "
        f"(sai số cuối cùng err = {err:.6e} > eps = {eps:.6e})."
    )      
