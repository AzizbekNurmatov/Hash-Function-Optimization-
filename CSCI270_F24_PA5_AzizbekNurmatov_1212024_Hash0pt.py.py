import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from matplotlib.animation import FuncAnimation

# Hash Table Functions

# First an empty table for the 
# hash is made provided a given size
def createTable(size):
    table = []
    for i in range(size):
        table.append(list())
    return table 

# The actual has function with the provided equation
def hashFunc(x, a, b, m):
    return int((a * x + b) % m)

# Geting the laod factor 
def loadFactor(count, size):
    return count / size

# Rehashing if we have more than one value 
# being assigned to a bucket 
def rehash(firstTable, a, b, newSize):
    newTable = createTable(newSize)
    for buck in firstTable:
        for value in buck:
            index = hashFunc(value, a, b, newSize)
            newTable[index].append(value)
    return newTable

# Cost function that calculates the number of rehashes
# over a series of insertions and returns the collision
# rate and rehash count 
def calcCost(data, a, b, initialSize, loadThreshold=0.75):
    table = createTable(initialSize)
    m = initialSize
    collisions = 0
    count = 0
    rehashCount = 0
    
    for value in data:
        index = hashFunc(value, a, b, m)
        if table[index]:
            collisions += 1
        if value not in table[index]:
            table[index].append(value)
            count += 1
        
        if loadFactor(count, m) > loadThreshold:
            rehashCount += 1
            newSize = m * 2
            table = rehash(table, a, b, newSize)
            m = newSize
    
    collisionRate = collisions / len(data)
    return rehashCount, collisionRate

# Optimizing the table itself  
def objectiveFuncHash(params, data, initialSize, loadThreshold=0.75):
    a, b = params
    rehashCount, collisionRate = calcCost(data, a, b, initialSize, loadThreshold)
    return collisionRate + 0.1 * rehashCount

# Objective function for nelder mead
# Quadratic Function Optimization
def quadratic_function(x):
    return x**2 + 3*x + 5

# Hill Climbing Function
def hill_climbing(starting, learningRate, steps):
    x = starting
    path = [x]
    for i in range(steps):
        grad = gradient(x)
        x += learningRate * grad
        path.append(x)
    return path

# Gradient calculation for hill climbing 
def gradient(x):
    return 2 * np.pi * np.cos(2 * np.pi * x) + 0.2 * x

# Code for hill climbing objective function 
def objective_function_hill(x):
    return np.sin(2 * np.pi * x) + 0.1 * (x ** 2)

# Initial Hash optimization 
data = np.random.randint(0, 1000, size=100)
initialSize = 10
loadThreshold = 0.75
initialGuess = np.array([1.0, 1.0])

# Optimize Hash Function provided that 
# the given method is nelder-mead
resultHash = minimize(
    objectiveFuncHash, 
    initialGuess, 
    args=(data, initialSize, loadThreshold), 
    method='Nelder-Mead'
)


optimized_a = resultHash.x[0]
optimized_b = resultHash.x[1]


# Optimize Quadratic Function
resultQuad = minimize(quadratic_function, np.array([5.0]), method='Nelder-Mead')

# Hill Climbing Setup
learningRate = 0.1
steps = 100
startingPoint = np.random.uniform(-3, 3)
path = hill_climbing(startingPoint, learningRate, steps)

# Visualization
figure, axes = plt.subplots(3, 1, figsize=(8, 20))

# Following code snippets all 

# Hill Climbing Animation
hillX = np.linspace(-3, 3, 400)
hillY = objective_function_hill(hillX)
axes[0].plot(hillX, hillY, color='blue', label='Objective Function')
axes[0].set_title("Hill Climbing")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].set_ylim(-1.5, 3)
axes[0].legend()

# Simulated Annealing 
a_values = np.linspace(0.5, 5.0, 100)
objective_values = [objectiveFuncHash([a, optimized_b], data, initialSize, loadThreshold) for a in a_values]
axes[1].plot(a_values, objective_values, label="Objective Function (varying a)")
axes[1].scatter(optimized_a, resultHash.fun, color='red', label="Optimized Parameters")
axes[1].set_title("Simulated Annealing")
axes[1].set_xlabel("a")
axes[1].set_ylabel("Cost")
axes[1].legend()
axes[1].grid()

# Nelder mead
x_values = np.linspace(-10, 10, 100)
y_values = quadratic_function(x_values)
axes[2].plot(x_values, y_values, label="Quadratic Function")
axes[2].scatter(resultQuad.x, resultQuad.fun, color='red', label="Optimized Solution")
axes[2].set_title("Quadratic Function with Nelder-Mead Optimization")
axes[2].set_xlabel("x")
axes[2].set_ylabel("f(x)")
axes[2].legend()
axes[2].grid()



# Animation Function
def update(frame):
    x_val = path[frame]
    y_val = objective_function_hill(x_val)
    axes[0].scatter(x_val, y_val, color='red', s=50)
    
    return []

# Code to create animation function 
ani = FuncAnimation(figure, update, frames=len(path), interval=100, blit=False, repeat=False)

plt.tight_layout()
plt.show()
