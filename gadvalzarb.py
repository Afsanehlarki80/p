
import matplotlib.pyplot as plt

def multiplication_table(n):
    table = [[i*j for j in range(1, n+1)] for i in range(1, n+1)]
    return table

def plot_table(table):
    fig, ax = plt.subplots()
    ax.axis('off')
    ax.table(cellText=table, loc='center', cellLoc='center')
    plt.show()

n = 10
table = multiplication_table(n)
plot_table(table)