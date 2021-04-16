import os

files=sorted(os.listdir('Database'))
print(len(os.listdir('Database')))
for f in files:
    print(f)
