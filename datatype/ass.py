a = "abaabbbaabbbabbbab"
p = -1
n = len(a)

while True:
    p = a.find("ab", p + 1)

    if p == -1:
        break

    print(p)