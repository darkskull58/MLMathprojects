import os
import numpy as np

# Directories and file paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "grid_data_dir")
matrix_file_path = os.path.join(base_dir, "matrix_file.txt")

# Collect all data and labels
X = []
y = []

# Process each file for digits 0-9
for digit in range(10):
    file_path = os.path.join(data_dir, f"{digit}_grid_data.txt")
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            # Read each line in the file
            for line in f:
                # Extract the vector (removing 'x#: ' prefix)
                vector_str = line.split(': ')[1].strip()[1:-1]
                vector = [int(x) for x in vector_str.split(',')]
                
                # Append vector to X and corresponding label to y
                X.append(vector)
                y.append(digit)

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Verify dimensions
print(f"Matrix X shape: {X.shape}")
print(f"Labels vector shape: {y.shape}")

# Save matrix and labels
np.savetxt(matrix_file_path, X, fmt='%d', delimiter=',')
np.savetxt(matrix_file_path.replace('.txt', '_labels.txt'), y, fmt='%d')

print(f"Matrix saved to {matrix_file_path}")
print(f"Labels saved to {matrix_file_path.replace('.txt', '_labels.txt')}")