import numpy as np

alpha = float(input("Enter the learning rate (0-1): "))
w0 = np.array([float(input(f"Enter initial weight for bias {i + 1}: ")) for i in range(2)])
w1 = np.array([float(input(f"Enter initial weight from input neuron 1 to hidden neuron {i + 1}: ")) for i in range(2)])
w2 = np.array([float(input(f"Enter initial weight from input neuron 2 to hidden neuron  {i + 1}: ")) for i in range(2)])
v0 = float(input("Enter the bias for output neuron: "))
v = np.array([float(input(f"Enter initial weights from hidden neuron {i + 1} to output neuron: ")) for i in range(2)])

gate = input("Choose a logic gate (AND, OR, NAND, NOR, XOR, XNOR): ").strip().upper()

if gate == "AND":
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 0, 0, 1])
elif gate == "OR":
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 1, 1, 1])
elif gate == "NAND":
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([1, 1, 1, 0])
elif gate == "NOR":
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([1, 0, 0, 0])
elif gate == "XOR":
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([0, 1, 1, 0])
elif gate == "XNOR":
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    target = np.array([1, 0, 0, 1])
else:
    print("Invalid logic gate!")
    exit()

print('Training.......')

z = [0, 0]
gradient = [0, 0]
count = 0

while count < 50000:
    output = []
    for i in range(len(x)):
        a1, a2 = x[i]
        t = target[i]

        for j in range(len(z)):
            Zin = w0[j] + a1 * w1[j] + a2 * w2[j]
            z[j] = 1 / (1 + np.exp(-Zin))

        Yin = v0 + z[0] * v[0] + z[1] * v[1]
        y = 1 / (1 + np.exp(-Yin))
        output.append(y)

        # Backpropagate error
        error = (t - y) * y * (1 - y)
        v0 = v0 + alpha * error

        # Update weights for hidden and input layers
        for j in range(len(z)):
            gradient[j] = z[j] * (1 - z[j]) * error * v[j]
            v[j] = v[j] + alpha * error * z[j]
            w1[j] = w1[j] + alpha * gradient[j] * a1
            w2[j] = w2[j] + alpha * gradient[j] * a2
            w0[j] = w0[j] + alpha * gradient[j]

    count += 1

print('Trained')

# Testing phase with continuous input prompt
while True:
    print('Testing')
    x1 = int(input('Enter the first input: '))
    x2 = int(input('Enter the second input: '))

    # Forward pass to predict output for given input
    for j in range(len(z)):
        Zin = w0[j] + x1 * w1[j] + x2 * w2[j]
        z[j] = 1 / (1 + np.exp(-Zin))

    Yin = v0 + z[0] * v[0] + z[1] * v[1]
    y = 1 / (1 + np.exp(-Yin))

    print('Output is: ', round(y))

    cont = input("Want to do more? (y/n): ").strip().lower()
    if cont != 'y':
        break