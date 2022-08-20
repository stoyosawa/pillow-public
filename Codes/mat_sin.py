import matplotlib.pyplot as plt
import math

x = [xi * 0.05 - 4.0 for xi in range(0, 160)]       # -4.0から4.0。0.05刻み
y = [math.sin(xi) for xi in x]                      # sin(x)

fig, ax = plt.subplots()                            # 描画領域を生成
ax.plot(x, y)                                       # (x, y)をプロット
plt.savefig('sin.png')                              # 保存
plt.show()                                          # 表示
