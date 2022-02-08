ledger = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'LProgramming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Berng Klein', 3, 24.99],
    [24387, ' на русском', 2, 4.59],
    [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
    [87236, 'C Programming Absolute Beginner\'s Guide', 1, 23.55],
    [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]



ledger.sort(key=lambda x: x[3])
print("Список отсортированный по цене:")
for el in ledger:
    print(el)

print("______________\n")
print("Список где книг > 5")
ledger_books_more_then_five = list(filter(lambda ledg: ledg[2] > 5, ledger))
for el in ledger_books_more_then_five:
    print(el)