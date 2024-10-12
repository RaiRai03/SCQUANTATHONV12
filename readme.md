# Team 7: DoraHacks Quantum Random Number Generator Challenge

# Stage 1: Quantum Random Number Generator (QRNG) on IBM QPU
In Stage 1, the code generates a random number between 0 and a given max value using qubits. The operation GenerateRandomBit() places a qubit in superposition, measuring it to get a random bit (0 or 1). These bits are assembled into an integer. If the generated number exceeds max, the process repeats. The Main operation calls this function to generate a random number and display it.

# Stage 2: Achieving High Accuracy with Classification Models
In Stage 2, the classifier model is trained to classify whether the data is quantum or classical random numbers. To do this the backend code trains a support vector classifier (SVC) on features extracted from QRNG data. The dataset (datascript) provides training data, and a web interface (hap) enables users to input QRNG data for classification, with options for model optimization and enhancement.

# Stage 3: Characterizing Noise and Fidelity
In Stage 3, the focus was on resolving errors during the API training process from Step 2. Challenges included inputting data correctly into the API, debugging issues in VSCode, and managing file dependencies. The most complex task was setting up and integrating TensorFlow for the API, which required troubleshooting file management and ensuring compatibility with the development environment.

# Stage 4: Pre-processing and Post-processing for High Entropy
In Stage 4, the focus was on improving the quality of QRNG data by combining it with PRNG data and QRNG bits in real time. Stronger algorithms were applied to detect and enhance patterns. The data was validated for randomness using the NIST test suite, and quantum state tomography was employed to verify accuracy. The process involved analyzing the results, identifying potential patches or updates, and ensuring high-quality randomness for further applications.

# Stage 5: Building High-Accuracy Classification Models for QRNG Verification
In Stage 5, the work from previous stages was combined to train high-accuracy QRNG classification models. Applications like Azure Quantum were used to create a data loader, analyzer, and model trainer, which processed CSV files and generated random numbers using both quantum and classical RNG. Numpy and Pandas handled numerical manipulation and analysis, while Qsharp ensured accuracy in quantum number generation. Subprocess executed quantum number tasks. 
