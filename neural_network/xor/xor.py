import math
import random


# Define the sigmoid function and its derivative
def sigmoid(x):
    """The sigmoid activation function maps any value to a value between 0 and 1."""
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(output):
    """The derivative of the sigmoid function used for gradient descent."""
    return output * (1.0 - output)

# Initialize a network with given number of inputs, hidden neurons, and outputs
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights': [random.uniform(-1, 1) for _ in range(n_inputs + 1)]} for _ in range(n_hidden)]
    output_layer = [{'weights': [random.uniform(-1, 1) for _ in range(n_hidden + 1)]} for _ in range(n_outputs)]
    network.append(hidden_layer)
    network.append(output_layer)
    return network

# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate(neuron['weights'], inputs)
            neuron['output'] = sigmoid(activation)
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs

# Calculate neuron activation for an input
def activate(weights, inputs):
    activation = weights[-1]  # The last weight is the bias
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = []
        if i != len(network)-1:  # Not the output layer
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += neuron['weights'][j] * neuron['delta']
                errors.append(error)
        else:  # Output layer
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * sigmoid_derivative(neuron['output'])

# Update network weights with error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)):
                neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
            neuron['weights'][-1] += l_rate * neuron['delta']  # Update bias

# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
    for epoch in range(n_epoch):
        sum_error = 0
        for row in train:
            outputs = forward_propagate(network, row)
            expected = [0 for _ in range(n_outputs)]
            expected[row[-1]] = 1
            sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
            backward_propagate_error(network, expected)
            update_weights(network, row, l_rate)
        print(f'Epoch={epoch}, lrate={l_rate}, error={sum_error}')

# Test training backprop algorithm
random.seed(1)  # Seed the random number generator
dataset = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]]
n_inputs = len(dataset[0]) - 1
n_outputs = len(set(row[-1] for row in dataset))
network = initialize_network(n_inputs, 2, n_outputs)
train_network(network, dataset, 0.5, 2000, n_outputs)

# Make a prediction with a network
def predict(network, row):
    outputs = forward_propagate(network, row)
    return outputs.index(max(outputs))
i 
# Display the network's predictions
for row in dataset:
    prediction = predict(network, row)
    print(f'Expected={row[-1]}, Got={prediction}')
