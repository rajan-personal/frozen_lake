import time

start = time.time()

# Data generation
num_points = 21
m, c = 1, 0
X = [x for x in range(-10, 11)]
Y = [m * x + c for x in X]

# Linear regression using gradient descent
def linear_regression(X, Y, learning_rate=0.01, epochs=200000):
    m_current = c_current = 0
    n = float(len(Y))

    for _ in range(epochs):
        Y_pred = [m_current * x + c_current for x in X]
        D_m = (2/n) * sum(x * (y - y_pred) for x, y, y_pred in zip(X, Y, Y_pred))
        D_c = (2/n) * sum(y - y_pred for y, y_pred in zip(Y, Y_pred))
        m_current += learning_rate * D_m
        c_current += learning_rate * D_c

    return m_current, c_current

# Model training
m_learned, c_learned = linear_regression(X, Y)

# Output
print("Learned values for m and c:", m_learned, c_learned)
print("Execution time:", time.time() - start)
