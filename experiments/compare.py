import numpy as np
import matplotlib.pyplot as plt

def mock_lap_don(x0, eps, max_iter=50):
    # Giải x^2 - 2 = 0 bằng lặp đơn: x = x - 0.2*(x^2 - 2)
    x_hist = [x0]
    for _ in range(max_iter):
        x_new = x_hist[-1] - 0.2 * (x_hist[-1]**2 - 2)
        x_hist.append(x_new)
        if abs(x_new - x_hist[-2]) < eps:
            break
    return np.array(x_hist)

def mock_newton(x0, eps, max_iter=50):
    # Giải f(x) = x^2 - 2 = 0, đạo hàm f'(x) = 2x
    x_hist = [x0]
    for _ in range(max_iter):
        fx = x_hist[-1]**2 - 2
        dfx = 2 * x_hist[-1]
        x_new = x_hist[-1] - fx / dfx
        x_hist.append(x_new)
        if abs(x_new - x_hist[-2]) < eps:
            break
    return np.array(x_hist)

def mock_newton_nghiem_boi(x0, eps, max_iter=50):
    # Giải f(x) = (x-1)^2 * (x+2) = 0. Nghiệm bội x* = 1.
    # f'(x) = (x-1)*(3x+3)
    x_hist = [x0]
    for _ in range(max_iter):
        x = x_hist[-1]
        fx = (x - 1)**2 * (x + 2)
        dfx = (x - 1) * (3 * x + 3)
        x_new = x - fx / dfx
        x_hist.append(x_new)
        if abs(x_new - x_hist[-2]) < eps:
            break
    return np.array(x_hist)


# 2. Thực nghiệm & Đồ thị

def analyze_convergence(x_history, x_star):
    """Tính mảng sai số e_k và các tỉ số đánh giá bậc hội tụ"""
    errors = np.abs(x_history - x_star)
    
    # Bỏ qua cảnh báo chia cho 0 ở bước cuối
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio_linear = errors[1:] / errors[:-1]           # |e_{k+1}| / |e_k|
        ratio_quadratic = errors[1:] / (errors[:-1]**2)   # |e_{k+1}| / |e_k|^2
        
    return errors, ratio_linear, ratio_quadratic

# THỰC NGHIỆM 1: So sánh tốc độ hội tụ (Nghiệm đơn)
x_star_1 = np.sqrt(2)
hist_ld = mock_lap_don(x0=2.0, eps=1e-6)
hist_nw = mock_newton(x0=2.0, eps=1e-6)

err_ld, _, _ = analyze_convergence(hist_ld, x_star_1)
err_nw, _, _ = analyze_convergence(hist_nw, x_star_1)

plt.figure(figsize=(8, 5))
plt.plot(err_ld, label='Lặp đơn', marker='o', linestyle='--')
plt.plot(err_nw, label='Newton', marker='s', linewidth=2)
plt.yscale('log') # Quan trọng: Yêu cầu của đề bài vẽ trên thang log
plt.xlabel('Số bước lặp k')
plt.ylabel('Sai số tuyệt đối $|x_k - x^*|$')
plt.title('Thực nghiệm 1: So sánh Lặp đơn và Newton (Thang Log)')
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.show()

# THỰC NGHIỆM 2: Newton với nghiệm bội 
# Cần chứng minh khi gặp nghiệm bội, Newton bị suy biến về hội tụ bậc 1
x_star_boi = 1.0
hist_nw_boi = mock_newton_nghiem_boi(x0=1.5, eps=1e-6)
err_nw_boi, ratio_1, ratio_2 = analyze_convergence(hist_nw_boi, x_star_boi)

print("--- THỰC NGHIỆM 2: TỈ SỐ HỘI TỤ NEWTON VỚI NGHIỆM BỘI ---")
print("Nhận xét: Tỉ số bậc 1 tiến về 0.5 (hằng số), trong khi tỉ số bậc 2 tăng vọt. Thuật toán bị suy biến xuống hội tụ tuyến tính.\n")
print(f"{'Bước k':<10} | {'|e_{k+1}| / |e_k|':<20} | {'|e_{k+1}| / |e_k|^2':<20}")
print("-" * 55)
for k in range(len(ratio_1)-1):
    r1 = f"{ratio_1[k]:.4f}"
    r2 = f"{ratio_2[k]:.4f}" if ratio_2[k] < 1000 else "Rất lớn (Vô cực)"
    print(f"Bước {k:<4} | {r1:<20} | {r2:<20}")
