#!/usr/bin/env python3
import sh
import subprocess
import shlex

git = sh.git.bake(_cwd='/Users/marcus/github/hashpass')
output = git.log('--pretty=%G?',_tty_out=False)
for line in output:
    if 'N' in line:
        print('bad sig!')

output = git.tag()
out=''
for line in output:
    thing = line.strip('\n')
    out = git('verify-tag', 'lol')
    print(out)
    

# with open('f','w') as f:
#     subprocess.call(['/usr/bin/git','-C','../hashpass','tag'],stdout=f)

# with open('f','r') as f:
#     for line in f:
#         git = sh.git.bake(_cwd='/Users/marcus/github/hashpass')
#         try:
#             print(git.tag('-v', line.strip('\n')))
#         except sh.ErrorReturnCode_1:
#             print('INVALID')