#!/usr/bin/env python

import subprocess

subprocess.call(['/usr/bin/git','-C','../hashpass','pull','origin'])

with open('f','w') as f:
    subprocess.call(['/usr/bin/git','-C','../hashpass','log','--pretty=%G?'],stdout=f)

with open('f','r') as f:
    for line in f:
        if 'G' in line:
            print('bad sig!')