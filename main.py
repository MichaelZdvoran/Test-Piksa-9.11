def roustouci_usek(cisla, n):
    nejdelsi = 0 

    if n == 0:
        return 0

    delka = 1
    nejdelsi = 1

    i = 1

    while i < n:
        if cisla[i] > cisla[i - 1]:
            delka = delka + 1 
        else:
            delka = 1

        if delka > nejdelsi:
            nejdelsi = delka

        i = i + 1 

    return nejdelsi 

print(roustouci_usek([1, 3, 2, 4, 5], 5))
print(roustouci_usek([5, 4, 3], 3))
print(roustouci_usek([2, 2, 2], 3))
print(roustouci_usek([-3, -2, -1, 0], 4))
print(roustouci_usek([], 0))
print(roustouci_usek([7], 1))