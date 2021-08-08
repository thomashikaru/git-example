# example Python file
import numpy
import matplotlib.pyplot as plt

def example_function(n):
    return n**2

def graphing_function(x):
    y = example_function(x)
    
    plt.style.use("seaborn")
    fig, ax = plt.subplot()
    ax.plot(x, y)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.show()

if __name__ == "__main__":
    print(example_function(np.array(10)))
    graphing_function(np.linspace(0, 10))
