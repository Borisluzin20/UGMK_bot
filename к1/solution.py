import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--sort", "--up_case", action="store_true",
                    help="convert name to upper register")
parser.add_argument('name', type=str, nargs='*')
s = []
args = parser.parse_args()

if args.sort:
    lst = [i.split('=') for i in args.name]
    lst.sort(key=lambda x: x[0])
else:
    lst = [i.split('=') for i in args.name]
for i in lst:
    print(f"Key: {i[0]} Value: {i[1]}")