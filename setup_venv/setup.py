import subprocess

from pathlib import Path


VENV_NAME = '.venv'
REQUIREMENTS = 'requirements.txt'

process1 = subprocess.run(['which', 'python3'], capture_output=True, text=True)

if process1.returncode != 0:
    raise OSError('Sorry python3 is not installed')

python_bin = process1.stdout.strip()

print(f'Python found in: {python_bin}')

process2 = subprocess.run('echo "$SHELL"', shell=True, capture_output=True, text=True)

shell_bin = process2.stdout.split('/')[-1]

create_venv = subprocess.run([python_bin, '-m', 'venv', VENV_NAME], check=True)

if create_venv.returncode == 0:
    print(f'Your venv {VENV_NAME} has been created')

pip_bin = f'{VENV_NAME}/bin/pip3'

if Path(REQUIREMENTS).exists():
    print(f'Requirements file "{REQUIREMENTS}" found')
    print('Installing requirements')
    subprocess.run([pip_bin, 'install', '-r', REQUIREMENTS])

    print('Process completed! Now activate your environment with "source .venv/bin/activate"')

else:
    print("No requirements specified ...")