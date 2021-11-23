from script import entropy_2
import numpy as np
import argparse as ap

parser = ap.ArgumentParser(description='stuff')
parser.add_argument('sequence', help='sequence')
parser.add_argument('frac', help = 'IF the sequence is frac')
parser.add_argument('-b', type=int,  nargs = '?', help = "base")
args = parser.parse_args()


def main():
    if args.frac == 'f':
        sequence = []
        for x in args.sequence.split():
            num, den = x.split('/')
            sequence.append(float(num)/float(den))
    else:
        sequence = [float(x) for x in args.sequence.split()]

    if args.b:
        print(f' H_X base {args.b} = {entropy_2(sequence, args.b)}')

    print("test")


if __name__ == '__main__':
    main()




