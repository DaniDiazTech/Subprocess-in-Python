import subprocess

# subprocess.run('ls')  # Simple command

# subprocess.run('ls -la', shell=True) # Dangerous command

list_of_files = subprocess.run(['ls', '-la'], capture_output=True, text=True)

print(list_of_files.stdout)