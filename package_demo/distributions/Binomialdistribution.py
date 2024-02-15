import math
import matplotlib as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    def __init__(self, prob=0.5, size=20):
        self.n = size
        self.p = prob
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self):
        self.mean = 1.0 * self.p * self.n
        return self.mean

    def calculate_stdev(self):
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n

    def plot_bar(self):
        plt.bar(x=["0", "1"], height=[(1 - self.p) * self.n, self.p * self.n])
        plt.title("Bar chart of data")
        plt.xlabel("Outcome")
        plt.ylabel("count")

    def pdf(self, k):
        part1 = math.factorial(self.n) / (
            math.factorial(k) * (math.factorial(self.n - k))
        )
        part2 = (self.p**k) * ((1 - self.p) ** (self.n - k))
        return part1 * part2

    def plot_bar_pdf(self):
        x = []
        y = []

        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        plt.bar(x, y)
        plt.title("Distribution of outcomes")
        plt.xlabel("Probability")
        plt.ylabel("Outcome")

        plt.show()

        return x, y

    def __add__(self, other):
        try:
            assert self.p == other.p, "p values are not equal"
        except AssertionError as error:
            raise

        res = Binomial()
        res.n = self.n + other.n
        res.p = self.p
        res.mean = self.calculate_mean()
        res.stdev = self.calculate_stdev()

        return res

    def __repr__(self):
        return (
            f"Mean {self.mean}, Standard deviation {self.stdev}, p {self.p}, n {self.n}"
        )
