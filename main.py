import argparse

from graphs import CreateGraphs
from github import Update
#from twitter import Twitter

parser = argparse.ArgumentParser()
parser.add_argument('update', type=str, help='update github')

args = parser.parse_args()

#E #T
CreateGraphs()

#L
if args.update == 'u':
    Update()

#Twiter
#x = Twitter()
#x.UpdateTwitter()


import argparse

parser = argparse.ArgumentParser()
parser.add_argument('update', help='update github')

args = parser.parse_args()

print(type(args.update))