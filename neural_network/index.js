class NeuralNetwork {
  constructor(inputNodes, hiddenNodes, outputNodes) {
    this.inputNodes = inputNodes;
    this.hiddenNodes = hiddenNodes;
    this.outputNodes = outputNodes;

    // Initialize weights with random values in a smaller range
    this.inputWeights = new Array(this.inputNodes)
      .fill()
      .map(() =>
        new Array(this.hiddenNodes)
          .fill()
          .map(() => (Math.random() - 0.5) * Math.sqrt(2 / inputNodes))
      );
    this.outputWeights = new Array(this.hiddenNodes)
      .fill()
      .map(() =>
        new Array(this.outputNodes)
          .fill()
          .map(() => (Math.random() - 0.5) * Math.sqrt(2 / hiddenNodes))
      );

    // Bias for hidden and output layer
    this.hiddenBias = new Array(this.hiddenNodes)
      .fill()
      .map(() => Math.random() - 0.5);
    this.outputBias = new Array(this.outputNodes)
      .fill()
      .map(() => Math.random() - 0.5);
    console.log("Neural network initialized with random weights.");
  }

  // Sigmoid activation function
  sigmoid(x, deriv = false) {
    if (deriv) {
      const fx = this.sigmoid(x);
      return fx * (1 - fx);
    }
    // Clip x to avoid numerical instability in the exponential function
    const clippedX = Math.max(Math.min(x, 10), -10);
    return 1 / (1 + Math.exp(-clippedX));
  }

  // Training function with added debugging
  // Inside the NeuralNetwork class

  // Train the neural network
  train(inputs, targets, epochs, learningRate) {
    for (let i = 0; i < epochs; i++) {
      // For each set of inputs and targets...
      for (let inputIndex = 0; inputIndex < inputs.length; inputIndex++) {
        // Forward pass - Calculate predicted output
        let hiddenInputs = this.inputWeights.map((weights, i) =>
          inputs[inputIndex].reduce(
            (sum, input, j) => sum + weights[j] * input,
            this.hiddenBias[i]
          )
        );
        let hiddenOutputs = hiddenInputs.map((h) => this.sigmoid(h));
        let finalInputs = this.outputWeights.map((weights, i) =>
          hiddenOutputs.reduce(
            (sum, output, j) => sum + weights[j] * output,
            this.outputBias[i]
          )
        );
        let finalOutputs = finalInputs.map((o) => this.sigmoid(o));

        // Calculate error (target - output)
        let outputErrors = targets[inputIndex].map(
          (target, k) => target - finalOutputs[k]
        );

        // Backpropagation - Calculate output layer deltas
        let outputDeltas = outputErrors.map(
          (error, k) => error * this.sigmoid(finalOutputs[k], true)
        );

        // Update output weights and biases
        for (let j = 0; j < this.outputWeights.length; j++) {
          for (let k = 0; k < this.outputWeights[j].length; k++) {
            this.outputWeights[j][k] +=
              outputDeltas[k] * hiddenOutputs[j] * learningRate;
          }
          this.outputBias[j] += outputDeltas[j] * learningRate;
        }

        // Calculate the deltas for the hidden layer
        let hiddenDeltas = hiddenOutputs.map(
          (output, j) =>
            output *
            (1 - output) *
            this.outputWeights[j].reduce(
              (acc, weight, k) => acc + weight * outputDeltas[k],
              0
            )
        );

        // Update input weights and biases
        for (let j = 0; j < this.inputWeights.length; j++) {
          for (let k = 0; k < this.inputWeights[j].length; k++) {
            this.inputWeights[j][k] +=
              hiddenDeltas[j] * inputs[inputIndex][k] * learningRate;
          }
          this.hiddenBias[j] += hiddenDeltas[j] * learningRate;
        }
      }
    }
    console.log("Training complete.");
  }

  // Predict function
  predict(input) {
    // Forward pass - Calculate predicted output
    let hiddenInputs = this.inputWeights.map((weights, i) =>
      input.reduce((sum, inp, j) => sum + inp * weights[j], this.hiddenBias[i])
    );
    let hiddenOutputs = hiddenInputs.map((h) => this.sigmoid(h));
    let finalInputs = this.outputWeights.map((weights, i) =>
      hiddenOutputs.reduce(
        (sum, output, j) => sum + weights[j] * output,
        this.outputBias[i]
      )
    );
    let finalOutputs = finalInputs.map((o) => this.sigmoid(o));

    console.log(`Prediction result: ${finalOutputs}`);
    return finalOutputs;
  }
}

// Initialize the neural network with 2 input nodes, 2 hidden nodes, and 1 output node
const nn = new NeuralNetwork(2, 2, 1);

// XOR input and output data
const inputs = [
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1],
];
const outputs = [[0], [1], [1], [0]];

// Train the neural network with a lower learning rate
console.log("Starting training...");
nn.train(inputs, outputs, 10000, 0.1); // Adjust the learning rate if necessary

// Predict the output for the inputs
console.log("Testing predictions after training:");
inputs.forEach((input) => {
  nn.predict(input);
});
