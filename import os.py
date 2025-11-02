import os

arquivo1 = open("dados1.txt", 'w')
print(os.path.abspath(arquivo1.name))