import fnmatch
#filter()
print(fnmatch.filter(['dlsf', 'ewro.txt', 'te.py', 'youe.py'], '*.txt'))
#fnmatch()
for file in ['word.doc','index.py','my_file.txt']:
    if fnmatch.fnmatch(file,'*.txt'):
        print(file)
#fnmatchcase()
print([addr for addr in ['word.doc','index.py','my_file.txt','a.TXT'] if fnmatch.fnmatchcase(addr, '*.txt')])
#translate()
print(fnmatch.translate('a*b.txt'))

