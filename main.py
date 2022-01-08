import argparse

from graphs import CreateGraphs
from github import Update
#from twitter import Twitter

parser = argparse.ArgumentParser()
parser.add_argument('update', type=int, help='update github')

args = parser.parse_args()

#E #T
CreateGraphs()

#L
if args.update == 1:
    Update()

#Twiter
#x = Twitter()
#x.UpdateTwitter()