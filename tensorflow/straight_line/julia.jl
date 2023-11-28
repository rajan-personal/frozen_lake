using Dates

epochs = 2000000

function linear_regression(X, Y; learning_rate=0.01, epochs=epochs)
    m_current = c_current = 0.0
    n = length(Y)

    for _ in 1:epochs
        Y_pred = [m_current * x + c_current for x in X]
        D_m = (2/n) * sum((x * (y - y_pred)) for (x, y, y_pred) in zip(X, Y, Y_pred))
        D_c = (2/n) * sum(y - y_pred for (y, y_pred) in zip(Y, Y_pred))
        m_current += learning_rate * D_m
        c_current += learning_rate * D_c
    end

    return m_current, c_current
end

# Main script
start = now()

# Data generation
num_points = 21
m, c = 1, 0
X = -10:10
Y = [m * x + c for x in X]

# Model training
m_learned, c_learned = linear_regression(X, Y)

# Output
println("Learned values for m and c: ", m_learned, " ", c_learned)
println("Execution time: ", now() - start)
