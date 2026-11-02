from typing import Callable, Tuple
import math
class ConvergenceError:
    def newton(
        f: Callable[[float], float],
        Df: Callable[[float], float],
        x0: float,
        eps: float,
        n_max: int
    )-> tuple[float, int, float]:
        """
        Giải gần đúng phương trình phi tuyến f(x) = 0 bằng phương pháp Newton.
        Tên thuật toán trong bài giảng: Algorithm 5 Phương pháp Newton (Chương 3, trang 48).
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
     x_curr = float(x0)
     err = float("int")
    # dong 1 - Algorithm 5: for i = 1 → n_max do 
    for i in range(1, n_max + 1):
        Df_val = float(df(x_curr))
        if math. isnan(Df_val) or math.isinf(Df_val):
            raise ValueError(
                f"Giá trị đạo hàm Df tại bước i = {i} (x = {x_curr}) không xác định (NaN/Inf).")
        # Kiểm tra điều kiện biên đạo hàm bằng 0 theo yêu cầu P3 & R6 
        if df_val == 0.0:
            raise ValueError(
                f"Lỗi chia cho 0: Đạo hàm Df(x) tại x = {x_curr} (bước i = {i}) bằng 0. Không thể tiếp tục phương pháp Newton.")
        f_val = float (f(x_curr))
        if math.isnan(f_val) or math.isinf(f_val):
            raise ValueError(
                f"Giá trị hàm f(x) tại bước i = {i} (x = {x_curr}) không xác định (NaN/Inf).")
        #dong 2 - Algorithm 5: Cap nhat x_new <- x_0 - f (x_0) / Df (x_0)
        x_new = x_curr - f_val / Df_val
        if math. isnan (x_new) or math.isinf(x_new):
            raise ValueError(
               f"Nghiệm gần đúng x_new tại bước i = {i} không xác định (NaN/Inf)."
            )
        # dong 3 - Algorithm 5 (ket hop Nhan xet thuc hanh): Tinh sai so giua 2 buoc
        err = abs (x_new - x_curr)
        # dong 4 - Algorithm 5: if err ‹ eps then 
        if err ‹ eps:
            # dong 5 & dong 10 - Algorithm 5: Thuat toan dung va tra ve (x_new, i, err)
            return float(x_new), i, float(err)
        # dong 6 - Algorithm 5: else
        else:
            # dong 7 - Algorithm 5: x <- x_new
            x_curr = x_new
        # dong 8 - Algorithm 5: end if
    # dong 9 - Algorithm 5: end for
    # Báo lỗi rõ ràng khi hết số bước lặp tối đa n_max mà chưa đạt sai số eps (R6)
    raise ConvergenceError(
    f"Algorithm 5 (Newton) không hội tụ sau n_max = {n_max} bước lặp "
    f" (sai số cuối err = {err: .6e} >= eps = {eps: .6e}) ."
    )
