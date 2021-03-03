import os, os.path
#change dir
os.chdir(r"C:\Users\Adil\Documents\KBTU\2 semester\PP2\Python\TSIS 5")
# os.rename('p1', 'part1')
os.rename('p2', 'p2_dir_and_files')

#number of files
dir = "C:/Users/Adil/Documents/KBTU/2 semester/PP2/Python/TSIS 5"
print('number of files:', len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))

#number of dirs
files = folders = 0
for _, dirnames, filenames in os.walk(dir):
    files += len(filenames)
    folders += len(dirnames)
print("{:,} files, {} folders".format(files, folders))

#list the content of directory
print(*os.listdir(dir))

#add file and dir
# os.mkdir('test')
os.chdir(dir + '/test')
with open('text.txt', 'w') as f:
    f.write('God damn, coding is great')

