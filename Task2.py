ledger = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'LProgramming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Berng Klein', 3, 24.99]
]


ledger_upd = list(map(lambda prise: (prise[0], prise[2]*prise[3] if prise[2]*prise[3] >= 100 else round(prise[2]*(prise[3] + 10), 2)), ledger))
print(ledger_upd)

