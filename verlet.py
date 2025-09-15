
import numpy as np
import matplotlib.pyplot as plt

def verlet_integration(x0, v0, k, m, dt, total_time):
    """
    Verlet积分法模拟简谐振子
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
    """
    steps = int(total_time / dt)
    t = np.linspace(0, total_time, steps)
    x = np.zeros(steps)
    
    # 初始条件
    x[0] = x0
    x[1] = x0 + v0 * dt  # 使用欧拉法计算第一步
    
    for i in range(2, steps):
        x[i] = 2 * x[i-1] - x[i-2] - (k/m) * x[i-1] * dt**2
    
    return t, x

# 参数设置
x0 = 1.0      # 初始位移
v0 = 0.0      # 初始速度
k = 1.0       # 弹簧常数
m = 1.0       # 质量
dt = 0.01     # 时间步长
total_time = 10.0  # 总模拟时间

# 运行模拟
t, x = verlet_integration(x0, v0, k, m, dt, total_time)

# 计算理论解（用于对比）
omega = np.sqrt(k/m)
x_theory = x0 * np.cos(omega * t)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置全局字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Verlet数值解')
plt.plot(t, x_theory, '--', label='理论解')
plt.xlabel('时间 (s)')
plt.ylabel('位移 (m)')
plt.title('简谐振子模拟 - Verlet积分法')
plt.legend()
plt.grid(True)
plt.show()
