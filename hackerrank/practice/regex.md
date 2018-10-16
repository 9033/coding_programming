# Practice > Regex
## Applications
### Detect the Email Addresses
```py
# python 3
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

### IP Address Validation
```js
// javascript (node.js)
function is_ipv4(i) {
    if (i.search(/^(\d{1,3}\.){3}\d{1,3}$/) < 0) return !1;
    return i.split('.').every(v => 0 <= v && v <= 255);
}
function is_ipv6(i) {
    if (i.search(/^(([0-9a-fA-F]{1,4}):){7}[0-9a-fA-F]{1,4}$/) < 0) return !1;
    return i.split(':').map(n => +("0x" + n)).every(v => 0 <= v && v <= 0xffff);
}

function whatis(i) {
    if (is_ipv4(i)) return 'IPv4';
    if (is_ipv6(i)) return 'IPv6';
    return 'Neither';
}

function processData(input) {
    input = input.split('\n');
    input.shift();
    let o;
    o = input.map(whatis);
    process.stdout.write(o.join('\n'));
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});
```

### Detect HTML Tags
```js
// javascript (node.js)
function processData(input) {
    s=new Set();
    e=input.match(/(?<=<\/*\s*)[\w]+(?=(\s+\S+)*\s*\/*>)/g);
    e.forEach(v=>{s.add(v);});
    console.log([...s].sort().join(';'));
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
```
### Split the Phone Numbers
```js
// javascript (node.js)
function processData(input) {
    input = input.split('\n');
    input.shift();
    let o = input.map(n => n.replace(/^([0-9]+)[ -]([0-9]+)[ -]([0-9]+)$/, 'CountryCode=$1,LocalAreaCode=$2,Number=$3'));
    process.stdout.write(o.join('\n'));
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});
```
### Detect HTML links
```py
# python 3
import re

lines=int(input(),10)
for l in range(lines):
    iss=input()
    regex=re.compile('<a[^>]*>.*?</a>')
    ret=regex.findall(iss)
    for a in ret:
        x=[]
        p=re.compile('href=([\'\"])(?P<href>[^\'\"]*?)\\1')    
        m=p.search(a)
        if m is not None:
            t=m.groupdict()
            x.append(t['href'])

        inn=re.compile('<([^<>]+)(?:\s+[^>]*)*>\s*(?P<inner>.*?)\s*</\\1>')    
        mm=inn.search(a)
        if mm is not None:
            t=mm.groupdict()
            x.append( re.sub(r'<[^>]*>','',t['inner'] ) )
        
        print(*x,sep=',')
```
