import os
from ase.io import read, write
import numpy as np
import shutil
import glob

def divide_chunks(data_list, chunk_size):
    """Yield successive chunks of specified size from data_list."""
    for i in range(0, len(data_list), chunk_size):
        yield data_list[i:i + chunk_size]
def main():
    # Read data from the file
    data = read(glob.glob('structures_*.extxyz')[0], index=':')
    print(data)
    # Split data into chunks of 500 (depends on joblimit of your cluster)
    chunked_data = list(divide_chunks(data, 500))

    # Process each chunk
    for chunk_index, chunk in enumerate(chunked_data):
        chunk_dir = str(chunk_index)
        os.mkdir(chunk_dir)

        for structure_index, structure in enumerate(chunk):
            # Update structure's positions and cell
            structure.set_positions(structure.get_positions())
            structure.set_cell(structure.get_cell())

            # Create directory for each structure
            structure_dir = f"{chunk_dir}/run_{structure_index + 1}"
            os.makedirs(structure_dir)

            # Write structure to file
            write(f"{structure_dir}/fort.34", structure)

            # Copy the INPUT file to the structure's directory
            shutil.copy("./input_templates/input_template.txt", f"{structure_dir}/INPUT")
         
if __name__ == "__main__":
    main()            