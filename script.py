import argparse
from fano import *
from tabulate import tabulate
from scipy.stats import entropy
from math import log, ceil
from fxpmath import Fxp
from huffman import Huffman_Encoding_alt
parser = argparse.ArgumentParser(description="Optional app description")
parser.add_argument('type', help = "encoding type")
parser.add_argument('sequence',  help="Input sequence")
parser.add_argument('frac', nargs='?', help="If the input sequence is frac")
parser.add_argument('-b',type = int,  nargs='?', help="Base")
args = parser.parse_args()

def max_entropy(sequence, base=2):
    entropy = 0
    norm = 1/len(sequence)
    entropy = norm*log(1/norm, base)*len(sequence)
    return entropy

def entropy_2(sequence, base=2):
    entropy = 0
    for p in sequence:
        entropy += p*log(1/p, base)
    return entropy
def shannon(sequence, base=2):
    headers = ["p", "q", "l", "c"]
    q = []
    l = []
    c = []
    i = 0
    for p in sequence:
        l.append(ceil(-log(p, base)))
        if i == 0:
            i += 1
            q.append(0)
            continue
        q.append(q[i - 1] + sequence[i-1])
        i +=1
    i = 0 
    for x,y in zip(q, l):
        z = Fxp(x, signed=False, n_word=y + 1, n_frac=y)
        c.append(z.bin()[1:])
    table = zip(sequence, q, l, c)
    print(tabulate(table, headers = headers))
    H_x = entropy_2(sequence)
    l_avg = average_l(sequence, l)
    max_H = max_entropy(sequence)
    print(f"Entropy: {H_x}, Average length: {l_avg}, Max entropy: {max_H}")
    print(f"=> h = {(H_x/l_avg)*100}")
    print(f"=> k = {100 * max_H/l_avg}")
def average_l(p, l):
    res = 0
    for x, y in zip(p, l):
        res += x*y
    return res

def shannon_fano(sequence):
    i = 0
    symbol_lst = []
    for s in sequence:
        symbol_lst.append(Symbol(f'a{i}', s))
        i += 1
    code_word = calculate_symbol_codes(symbol_lst)
    a = []
    b = []
    c = []
    d = []
    for symbol in code_word:
        a.append(symbol.char)
        b.append(symbol.probability)
        c.append(symbol.code)
        l = int(len(symbol.code))
        d.append(l)
    headers = ["a", "Prob", "code", "len"]
    table = zip(a, b, c, d)
    print(tabulate(table, headers=headers))
    H_x = entropy_2(sequence)
    l_avg = average_l(sequence, d)
    max_H = max_entropy(sequence)
    print(f"Entropy: {H_x}, Average length: {l_avg}, Max entropy: {max_H}")
    print(f"=> h = {(H_x/l_avg)*100}")
    print(f"=> k = {100 * max_H/l_avg}")
    

def huffman(sequence):
    huffman_encoding, tree = Huffman_Encoding_alt(sequence)
    l = []
    k = []
    v = []
    for key, value in huffman_encoding.items():
        k.append(key)
        v.append(value)
        l.append(len(value))
    table = zip(k, v, l)
    headers = ["a", "code", "len"]
    print(tabulate(table, headers=headers, tablefmt="pretty"))
    H_x = entropy_2(sequence)
    l_avg = average_l(sequence, l)
    max_H = max_entropy(sequence)
    print(f"Entropy: {H_x}, Average length: {l_avg}, Max entropy: {max_H}")
    print(f"=> h = {(H_x/l_avg)*100}")
    print(f"=> k = {100 * max_H/l_avg}")
def solve_entropy(sequence, base=2):
    H_x = entropy_2(sequence, base)

def main():
    if args.frac == 'f':
        sequence = []
        for x in args.sequence.split():
            num, den = x.split('/')
            sequence.append(float(num)/float(den))
    else:
        sequence = [float(x) for x in args.sequence.split()]
    # shannon(sequence)
    if args.b:
        print(f"H_X = {entropy_2(sequence, args.b)}")
    if args.type == 's':
        sequence.sort(reverse = True)
        shannon(sequence)
    if args.type == 'f':
        sequence.sort(reverse = True)
        shannon_fano(sequence)
    if args.type == 'h':
        huffman(sequence)
if __name__ == '__main__':
    main()
