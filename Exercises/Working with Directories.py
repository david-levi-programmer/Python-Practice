from pathlib import Path

reference = Path()
# why is the search method called 'glob'?
for file in reference.glob('*'):
    print(file)
