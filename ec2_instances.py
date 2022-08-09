#!/usr/bin/env python

import subprocess
from copy import copy
import shlex
import sys

instances = subprocess.getoutput("""aws ec2 describe-instances | grep -i instanceid | cut -d ":" -f 2 | sed 's/\"//g'""").split(',')

instances = [item.lstrip(' \n') for item in instances.copy()]

del instances[-1]

if sys.argv[1] == 'start':
    subprocess.run(shlex.split(f"""aws ec2 start-instances --instance-ids {' '.join(instances)}"""))
elif sys.argv[1] == 'stop':
    subprocess.run(shlex.split(f"""aws ec2 stop-instances --instance-ids {' '.join(instances)}"""))
