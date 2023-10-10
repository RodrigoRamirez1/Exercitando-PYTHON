# UTILIZANDO MATPLOTLIB E NUMPY

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)

print(y)

plt.plot(t,y)
plt.title("Gráfico do Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.show()