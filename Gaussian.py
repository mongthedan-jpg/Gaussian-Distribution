
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def normal_pdf(x, mu, sigma):
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))

mu = float(input("mu: "))
sigma = float(input("sigma: "))
x0 = float(input("x (để thử pdf tại 1 điểm): "))

print("pdf tại x0:", normal_pdf(x0, mu, sigma))


x = np.linspace(mu - 8 * sigma, mu + 8 * sigma, 1000001)
y = normal_pdf(x, mu, sigma)
print("tích phân:", np.trapezoid(y, x))     


rng = np.random.default_rng(0)
samples = rng.normal(mu, sigma, 10000)
sns.histplot(samples, bins=50, stat="density", label="mẫu")
plt.plot(x, y, "r", label="pdf")
plt.legend()
plt.show()


