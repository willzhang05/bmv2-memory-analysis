#!/usr/bin/python3
import sys
import os
import re

def main():
    args = sys.argv[1:]
    i = 0
    output = []
    with open(args[0], 'r') as f:
        for line in f:
            #test = re.match(r'(Wrote register|Read register)', line)
            if "Wrote register" in line or "Read register" in line:
                action = line.rstrip().split()[8:]
                if action[0] == "Wrote":
                    output.append(' '.join([str(i), 'W', action[5], hex(int(action[5]))]))
                else:
                    output.append(' '.join([str(i), 'R', action[5], hex(int(action[5]))]))

                print(output[-1])
                i += 1

if __name__ == '__main__':
    main()
