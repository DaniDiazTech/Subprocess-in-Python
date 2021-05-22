import subprocess

patterns_file = 'patterns.txt'
readfile = 'romeo-full.txt'

with open(patterns_file, 'r') as f:
    for pattern in f:
        pattern = pattern.strip()

        process = subprocess.run(
            ['grep', '-c', f'{pattern}', readfile], capture_output=True, text=True)

        if int(process.stdout) == 0:
            print(
                f'The pattern "{pattern}" did not match any line of {readfile}')

            continue

        print(f'The pattern "{pattern}" matched {process.stdout.strip()} times')
