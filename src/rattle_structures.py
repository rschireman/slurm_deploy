"""
Generate displaced structures using
* Standard rattle, gaussian displacements
* Monte Carlo rattle, gaussian displacements w penatly for short atomic dists
* Phonon rattle, construct a rough guess of fc2 and populate phonon modes with
  thermal energy corresponding to a temperature

The hyper parameters for the different methods are chosen such that the
magnitude of the displacements will be roughly the same

This script may take a few minutes to run.
"""


from ase.io import read,write
from hiphive.structure_generation import (generate_rattled_structures,
                                          generate_mc_rattled_structures,
                                          generate_phonon_rattled_structures)

prim = read('./structure_files/iceXI.cif')

# parameters
size = 2            # supercell size
n_structures = 10      # number of configurations to generate

rattle_std = 0.001
min_distance = 0.00003 

supercell = prim.repeat(size)
reference_positions = supercell.get_positions()
write('reference_structure.xyz', supercell)

# standard rattle
print('standard rattle')
structures_rattle = generate_rattled_structures(
    supercell, n_structures, rattle_std)
write('structures_rattle.extxyz', structures_rattle)

# Monte Carlo rattle
print('Monte Carlo rattle')
structures_mc_rattle = generate_mc_rattled_structures(
    supercell, n_structures, rattle_std, min_distance, n_iter=10)
write(f'structures_mc_rattle_supercell_{size}_{rattle_std}_{min_distance}_{n_structures}.extxyz', structures_mc_rattle)


