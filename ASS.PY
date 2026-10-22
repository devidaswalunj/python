s = "ABBAAABABABABBBAAAAB"

a = 0

while True:
    a = s.find("A", a)

    if a == -1:
        break

    print(a)
    a += 1
