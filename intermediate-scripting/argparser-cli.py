import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file input')
args = parser.parse_args()
print(args)