import sys
c="bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
sys.stdout.write("".join([l+'o' if l in c else l for l in sys.stdin.read()]))