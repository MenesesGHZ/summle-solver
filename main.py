import argparse
import summle

parser = argparse.ArgumentParser(description='summle solver args.')
parser.add_argument('--nums', metavar='N', type=int, nargs='+', help='list of numbers')
parser.add_argument('--target', type=int, nargs=1, help='target')
args = parser.parse_args()

if __name__ == '__main__':
    target = args.target[0]
    nums = args.nums
    summle.interface(target, nums) 
