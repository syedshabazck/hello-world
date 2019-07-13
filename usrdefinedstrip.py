'''
Created on Jul 6, 2019

@author: syedshabaz
'''
import re
def usrsplit(strin,key=0):
    stringregex = re.compile(r'^\s+')
    if key == 0:
        print('Argument not passed')
#         stri = stringregex.search(strin)
        stri = stringregex.sub('',strin)
#         print(stri.groups())
    else:
        print('Argument is passed')
#         stringregex = re.compile(r'')
        stri = stringregex.sub(key,strin)
        print(stri)
    


a= '   Helloworld  '
usrsplit(a)