
import numpy as np
import matplotlib.pyplot as plt


def simulate_harmonic_oscillator(x0, v0, k, m, dt, total_time):
    """
    使用前向欧拉法模拟简谐振子运动
    参数:
        x0: 初始位移
        v0: 初始速度
        k: 弹簧常数
        m: 质量
        dt: 时间步长
        total_time: 总模拟时间
    返回:
        t: 时间数组
        x: 位移数组
        v: 速度数组
    """
    steps = int(total_time / dt)
    t = np.linspace(0, total_time, steps)
    x = np.zeros(steps)
    v = np.zeros(steps)
    
    x[0] = x0
    v[0] = v0
    
    for i in range(1, steps):
        v[i] = v[i-1] - (k/m) * x[i-1] * dt
        x[i] = x[i-1] + v[i-1] * dt
    
    return t, x, v

# 参数设置
x0 = 0.0      # 初始位移
v0 = 1.0      # 初始速度
k = 1.0       # 弹簧常数
m = 1.0       # 质量
dt = 0.01     # 时间步长
total_time = 10.0  # 总模拟时间

# 运行模拟
t, x, v = simulate_harmonic_oscillator(x0, v0, k, m, dt, total_time)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置全局字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 绘制结果
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x, label='位移')
plt.ylabel('位移 (m)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, v, label='速度', color='orange')
plt.xlabel('时间 (s)')
plt.ylabel('速度 (m/s)')
plt.legend()

plt.suptitle('简谐振子模拟 (前向欧拉法)')
plt.tight_layout()
plt.show()
