import sys
c="aeiouyAEIOUY "
sys.stdout.write("".join([l+'o' if l not in c else l for l in sys.stdin.read()]))