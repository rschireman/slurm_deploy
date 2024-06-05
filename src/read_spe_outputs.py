import os
import glob
import numpy as np
import h5py
from ase import Atoms
from ase.io import read, write
from ase.units import Hartree, Bohr
from ase.calculators.singlepoint import SinglePointCalculator
from CRYSTALpytools.crystal_io import Crystal_output

def process_directory(directory):
    try:
        outfile = glob.glob(f'{directory}/output_*.out')[0]
        print(f"Processing {outfile}")
    except IndexError:
        return

    output = Crystal_output().read_cry_output(outfile)
    geometry = read(f'{directory}/fort.34')
    output.get_forces(grad=False, initial=True)

    try:
        forces = output.forces_atoms * Hartree / Bohr
        energy = output.get_final_energy()
        print(f"Forces: {forces}")
        print(f"Energy: {energy}")

        curr_atoms = Atoms(
            positions=geometry.get_positions(),
            cell=geometry.get_cell(),
            symbols=geometry.get_chemical_symbols(),
            pbc=True
        )

        calculator = SinglePointCalculator(curr_atoms, energy=energy, forces=forces)
        curr_atoms.calc = calculator

        write('data.extxyz', curr_atoms, format='extxyz', append=True)
    except TypeError:
        print(f"TypeError encountered for {outfile}, skipping.")

def main():
    directories = glob.iglob('./*/**/')
    for i, directory in enumerate(directories):
        print(f"Directory: {directory}")
        process_directory(directory)

    data = read('data.extxyz', index=':')
    print("Final data read completed.")

if __name__ == "__main__":
    main()