import sys
import json

import requests

seed_file = sys.argv[1]
output_file = sys.argv[2]

timemap_stem = "http://localhost:1208/timemap/json/"

print("reading from file {}".format(seed_file))

with open(seed_file) as f:

    print("writing out to file {}".format(output_file))

    with open(output_file, 'a') as g:

        for line in f:
    
            line = line.strip()

            print("looking at line {}".format(line))
    
            r = requests.get("{}{}".format(timemap_stem, line))
    
            if r.status_code == 200:
    
                data = json.loads(r.text)
        
                if len(data["mementos"]["list"]) > 0:
                    print("there are {} mementos in the list".format(len(data["mementos"]["list"])))
#                    print(data["mementos"]["list"])
#                    print(data["mementos"]["list"][0])
                    g.write("{}\t{}\t{} mementos\n".format(line, "ARCHIVED", len(data["mementos"]["list"])))
                else:
                    g.write("{}\t{}\t \n".format(line, "NOT ARCHIVED"))
    
            else:
                g.write("{}\t{}\t \n".format(line, "NOT ARCHIVED"))
