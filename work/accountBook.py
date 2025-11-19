import argparse

p = argparse.ArgumentParser()
p.add_argument("input")
p.add_argument("-n", type=int, default=1)
p.add_argument("--flag", action="store_true")
args = p.parse_args()
print("input=", args.input, "n=", args.n, "flag=", args.flag)
