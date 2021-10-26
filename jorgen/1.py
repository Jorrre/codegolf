import sys
c="aeiouyAEIOUY "
sys.stdout.write("".join([l+'o'+l.lower() if l not in c else l for l in sys.stdin.read()[:-1]]))