# files

f = open('demofile.txt')
print(f.read(), end='')
f.seek(0)
print(f.read(4))
f.seek(0)
print(f.readlines())
f.seek(0)
for x in f:
    print(x)

f = open('demofile2.txt', 'a') # appends new text
f.write('Now the file has more content!')
f.close()

f = open('demofile3.txt', 'w') # overwrites existing content
f.write('Now the file has more content!')
f.close()

try:
    f = open('demofile3.txt', 'x') # fails to open if the file already exists
except FileExistsError:
    print('File already exists.')

import os
os.remove('demofile3.txt')

if os.path.exists('demofile2.txt'):
    os.remove('demofile2.txt')
else:
    print('The file does not exist.')

os.mkdir('newfolder')
os.rmdir('newfolder')
