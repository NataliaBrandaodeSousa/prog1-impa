a, b, c, d, e = map(float, input("Digite 5 valores separados por espaço: ").split())

if a > b: 
    temp = a 
    a = b 
    b = temp 
else: 
    a = a 
    b = b 

if c > d: 
    temp = c
    c = d 
    d = temp 
else: 
    c = c 
    d = d 

if a < c: 
    a = a
    temp = b 
    b = c 
    c = d 
    d = temp 
else: 
    temp = a 
    a = c 
    c = b 
    b = temp 
    d = d

if e < b: 
    if e < a: 
        temp1 = a 
        a = e
        temp2 = c 
        c = b 
        b = temp1 
        e = d 
        d = temp2 
    else: 
        a = a 
        temp1 = b 
        b = e 
        temp2 = c 
        c = temp1
        e = d 
        d = temp2 
else: 
    if e > c: 
        a = a
        b = b 
        c = c 
        temp = d 
        d = e 
        e = temp 
    else: 
        a = a 
        b = b 
        temp = c
        c = e 
        e = d
        d = temp 

if e < c: 
    if e < b: 
        a = a 
        temp1 = b 
        b = e 
        temp2 = c 
        c = temp1
        e = d 
        d = temp2 
    else: 
        a = a 
        b = b 
        temp1 = c 
        c = e 
        e = d 
        d = temp1 
else: 
    if e > d: 
        a = a 
        b = b 
        c = c 
        d = d 
        e = e 
    else: 
        a = a 
        b = b 
        c = c 
        temp1 = d 
        d = e 
        e = temp1 

print( a , b ,c, d , e)