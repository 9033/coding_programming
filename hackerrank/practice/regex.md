# Practice > Regex
## Applications
### Detect the Email Addresses
```py
import re

lines=int(input(),10)
mails=set()

for l in range(lines):
    s=input()
    r=re.finditer(r'(\w+(\.\w+)*@\w+(\.\w+)+)',s)
    for rs in r:
        mails.add(rs.group(0))

r=list(mails)
r.sort()

print(*r,sep=';')
```