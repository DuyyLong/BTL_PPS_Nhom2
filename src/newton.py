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
