import sys
import csv

from archivenow import archivenow

seedfile = sys.argv[1]
outputfile = sys.argv[2]

with open(seedfile) as f:

    with open(outputfile, 'w') as g:

        for line in f:
    
            line = line.strip()
            print("working on URI-R {}".format(line))
    
            urim = archivenow.push(line, "ia")[0]
            g.write('{}\t{}\n'.format(line, urim))

            urim = archivenow.push(line, "is")[0]
            g.write('{}\t{}\n'.format(line, urim))

            urim = archivenow.push(line, "wc")
            g.write('{}\t{}\n'.format(line, urim))
