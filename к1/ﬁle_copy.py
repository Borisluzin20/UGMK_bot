import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--upper",
                    help="convert name to upper register",
                    action="store_true")
parser.add_argument("--lines",
                    metavar="lines",
                    type=int,
                    nargs='?',
                    default=0)
parser.add_argument("file1", metavar="file1", type=str, nargs='?')
parser.add_argument("file2", metavar="file2", type=str, nargs='?')
args = parser.parse_args()
with open(args.file1, "r") as inp:
    if args.lines:
        s = inp.read().split('\n')[:args.lines]
    else:
        s = inp.read().split('\n')
    with open(args.file2, 'w') as out:

        if not args.upper:
            out.writelines([i + '\n' for i in s])
        else:
            out.writelines([i.upper() + '\n' for i in s])