import os

dirname = os.path.dirname(__file__)
fname = 'greet.txt'
fpath = os.path.join(dirname, fname)

with open(fpath, mode='w', encoding='utf_8') as f:
    f.write('Hello world!')

print('Finished!')