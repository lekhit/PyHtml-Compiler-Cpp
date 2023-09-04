import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old
lt=[]

code = """
i = [0,1,2]
for j in i :
    print(j)
"""
codes=['i = [0,1,2]\n','for j in i :\n print(j)\n if j==2:\n  print(j)']
with stdoutIO() as s:
    for code in codes:
        exec(code)
lt.append(str(s.getvalue()))
for i in lt:
    print(i)
print("out:", s.getvalue())
