import numpy as np

gate = input("Choose a logic gate (AND, OR, NAND, NOR): ").strip().upper()

if gate == "AND":
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([0, 0, 0, 1])
elif gate == "OR":
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([0, 1, 1, 1])
elif gate == "NAND":
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([1, 1, 1, 0])
elif gate == "NOR":
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([1, 0, 0, 0])
else:
    print("Invalid logic gate!")
    exit()

n_inputs = inputs.shape[1]
weights = np.array([float(input(f"Enter initial weight for input {i + 1}: ")) for i in range(n_inputs)])
bias = float(input("Enter initial bias: "))
learning_rate = float(input("Enter the learning rate (0-1): "))
epochs = int(input("Enter the maximum number of training epochs: "))

# Training Perceptron
for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}/{epochs}")

    total_error = 0  # Initialize total error to zero

    for i in range(len(inputs)):
        # Step 4 & 5: Calculate the weighted sum (Net) = Σ aiwi + bias
        net_input = np.dot(inputs[i], weights) + bias
        output = 1 if net_input >= 0 else 0  # Step 6: Activation function (step function)

        # Step 7: Calculate the error
        error = targets[i] - output
        total_error += abs(error)  # Accumulate the error

        # Update weights and bias if there is an error
        if error != 0:
            weights = weights + learning_rate * error * inputs[i]
            bias = bias + learning_rate * error

        print(f"Input: {inputs[i]}, Target: {targets[i]}, Output: {output}, Weights: {weights}, Bias: {bias}")

    # Stop training if total error is zero
    if total_error == 0:
        print("Training complete. No more errors!")
        break

# Testing
print("\nTraining complete. You can now test the perceptron.")
while True:
    test_input = input("Enter test input (two binary values separated by space, or 'exit' to stop): ")
    if test_input.lower() == 'exit':
        break

    test_input = np.array([int(x) for x in test_input.split()])

    # Calculate the output based on current weights and bias
    net_input = np.dot(test_input, weights) + bias
    output = 1 if net_input >= 0 else 0
    print(f"Output for {test_input}: {output}")
