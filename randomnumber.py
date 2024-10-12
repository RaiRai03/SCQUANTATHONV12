import subprocess
import pandas as pd
import numpy as np

def generate_random_numbers(n_samples, max_value):
    try:
        # Run Q# program
        qsharp_output = subprocess.check_output(['dotnet', 'run'])
        qsharp_random_number = int(qsharp_output.decode('utf-8').split(':')[-1].strip())
    except subprocess.CalledProcessError as e:
        print(f"Error: The 'dotnet run' command failed with exit status {e.returncode}.")
        return None
    except FileNotFoundError:
        print("Error: The 'dotnet' command was not found. Please install .NET Core SDK and configure PATH environment variable.")
        return None

    # Generate classical RNG numbers
    classical_rnd_numbers = np.random.randint(0, max_value, size=n_samples)

    # Combine Q# output and classical RNG numbers
    combined_output = pd.DataFrame({'qsharp_random_number': [qsharp_random_number] * n_samples, 'classical_rnd_numbers': classical_rnd_numbers})

    return combined_output