import argparse

parser = argparse.ArgumentParser()
parser.add_argument('update', help='update github')

args = parser.parse_args()

print(type(args.update))