import subprocess
import pandas as pd
import numpy as np

# Run Q# program
try:
    qsharp_output = subprocess.check_output(['dotnet', 'run'])
    qsharp_random_number = int(qsharp_output.decode('utf-8').split(':')[-1].strip())
except FileNotFoundError:
    print("Error: dotnet command not found. Please install .NET Core SDK and configure PATH environment variable.")
    exit(1)

# Generate classical RNG numbers
def generate_classical_rnd_numbers(n_samples, max_value):
    rnd_numbers = np.random.randint(0, max_value, size=n_samples)
    return pd.DataFrame(rnd_numbers, columns=['number'])

n_samples = 10000
max_value = 100000
classical_rnd_numbers = generate_classical_rnd_numbers(n_samples, max_value)

# Combine Q# output and classical RNG numbers
combined_output = pd.DataFrame({'qsharp_random_number': [qsharp_random_number] * n_samples, 'classical_rnd_numbers': classical_rnd_numbers['number'].tolist()})
print(combined_output)