import subprocess

from glob import glob

# Gets files with each extension
java_files = glob('*.java')

cpp_files = glob('*.cpp')

for file in cpp_files:
    process = subprocess.run(f'g++ {file} -o out; ./out', shell=True, capture_output=True, text=True)
    
    output = process.stdout.strip() + ' BTW this was runned by Python'

    print(output)

for file in java_files:
    without_ext = file.strip('.java')
    process = subprocess.run(f'java {file}; java {without_ext}',shell=True, capture_output=True, text=True)

    output = process.stdout.strip() + ' A Python subprocess runned this :)'
    print(output)