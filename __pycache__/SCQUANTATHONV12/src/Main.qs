namespace SCQUANTATHONV12 {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    // Function to generate a quantum random number
    operation GenerateQuantumRandomNumber() : Result {
        using (qubit = Qubit()) {
            H(qubit); // Apply Hadamard gate to create superposition
            let measurement = Measure(qubit); // Measure the qubit
            Reset(qubit); // Reset the qubit after measurement
            return measurement; // Return the measurement result
        }
    }

    // Function to calculate the mean of results
    function Mean(results: Result[]) : Double {
        let sum = 0.0;
        for (result in results) {
            sum += (result == One ? 1.0 : 0.0);
        }
        return sum / results.Length; // Return the mean
    }

    // Function to verify the randomness of the generated numbers
    operation VerifyRandomness(numSamples: Int) : Unit {
        mutable results = new Result[numSamples];
        for (i in 0..numSamples - 1) {
            set results w/= i <- GenerateQuantumRandomNumber();
        }

        let mean = Mean(results);
        mutable variance = 0.0;
        for (result in results) {
            let diff = (result == One ? 1.0 : 0.0) - mean;
            set variance += diff * diff; // Variance calculation
        }
        set variance /= results.Length;

        // Output the results
        Message($"Generated {numSamples} random numbers.");
        Message($"Mean: {mean}");
        Message($"Variance: {variance}");

        // Check if the results are truly random
        if (mean >= 0.45 && mean <= 0.55 && variance >= 0.2 && variance <= 0.3) {
            Message("Results are likely quantum random numbers.");
        } else {
            Message("Results may be classical numbers.");
        }
    }

    @EntryPoint()
    operation Main() : Unit {
        Message("Hello quantum world!");
        VerifyRandomness(100); // Verify randomness with 100 samples
    }
}
