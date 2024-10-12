# Team 7: DoraHacks Quantum Random Number Generator Challenge

# Stage 1: Quantum Random Number Generator (QRNG) on IBM QPU
In Stage 1, the code generates a random number between 0 and a given max value using qubits. The operation GenerateRandomBit() places a qubit in superposition, measuring it to get a random bit (0 or 1). These bits are assembled into an integer. If the generated number exceeds max, the process repeats. The Main operation calls this function to generate a random number and display it.

# Stage 2: Achieving High Accuracy with Classification Models
In Stage 2, the classifier model is trained to classify whether the data is quantum or classical random numbers. To do this the backend code trains a support vector classifier (SVC) on features extracted from QRNG data. The dataset (datascript) provides training data, and a web interface (hap) enables users to input QRNG data for classification, with options for model optimization and enhancement.

# Stage 3: Characterizing Noise and Fidelity
In Stage 3, the focus was on resolving errors during the API training process from Step 2. Challenges included inputting data correctly into the API, debugging issues in VSCode, and managing file dependencies. The most complex task was setting up and integrating TensorFlow for the API, which required troubleshooting file management and ensuring compatibility with the development environment.
# Stage 4: Pre-processing and Post-processing for High Entropy

# Stage 5: Building High-Accuracy Classification Models for QRNG Verification
