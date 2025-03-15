import random
massziv = random.sample(range(1, 101), 5)
a, b, c, d, e=massziv
def kerdesek(massziv):
    kerdes = input("következő kérdés")
    if ">" in kerdes:
        a,b=kerdes.split(">")
        a = a.strip()
        b = b.strip().replace("?", "")
        igaz = massziv[ord(a) - ord('a')] > massziv[ord(b) - ord('a')]
    elif "<" in kerdes:
        a, b = kerdes.split("<")
        a = a.strip()
        b = b.strip().replace("?", "")
        igaz = massziv[ord(a) - ord('a')] < massziv[ord(b) - ord('a')]
    else:
        print("Használj relációs jelet")
        return kerdesek(massziv)
    print("Igaz" if igaz else "Hamis")
def sorrendek(massziv):
    print("mi a sorrend?")
    tipp = input().strip().lower().split()
    sorrend = [massziv[ord(f) - ord('a')] for f in tipp]
    return sorrend == sorted(massziv)
i = 0
for i in range(6):
    kerdesek(massziv)
    i +=1
if sorrendek(massziv):
    print("A sorrend helyes")
else:
    betusorrend = sorted(range(5), key=lambda k: massziv[k])
    betuk = ['a', 'b', 'c', 'd', 'e']
    helyessorrend = ' '.join([betuk[i] for i in betusorrend])
    print(f"helytelen sorrend, a helyes: {helyessorrend}")