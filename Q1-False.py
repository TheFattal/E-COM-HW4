
a = 1
b = 0
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

a = 0
b = 0
c = 0
d = 0
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 3
c = 0
d = 0
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 2
c = 3
d = 1
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 1
d = 0
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 0
b = 0
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

# Hi Itay, not sure if the next one possible....(OR TRUE).
a = 1
b = 0
c = 3
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 1
b = 0
c = 0
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 22
b = 1
c = 1
d = 1
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")