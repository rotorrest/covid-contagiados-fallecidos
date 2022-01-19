import argparse

from graphs import CreateGraphs
from github import Update
from twitter import Twitter

parser = argparse.ArgumentParser()
parser.add_argument('update', type=int, help='update github of arg = 1')

args = parser.parse_args()

#E #T
date = CreateGraphs()

#L
if args.update == 1:
   Update()
   
# #Twiter
x = Twitter()
x.UpdateTwitter(date)