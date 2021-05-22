'''Program checker with subprocess'''

import subprocess

import re

programs = input('Separe the programs with a space: ').split()

secure_pattern = '[\w\d]'

for program in programs:

    if not re.match(secure_pattern, program):
        print("Sorry we can't check that program")

        continue

    process = subprocess. run(
        ['which', program], capture_output=True, text=True)

    if process.returncode == 0:
        print(f'The program "{program}" is installed')

        print(f'The location of the binary is: {process.stdout}')
    else:
        print(f'Sorry the {program} is not installed')

        print(process.stderr)

    print('\n')
