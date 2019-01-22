TAX_RATES = [
    (2200, 0),
    (2700, 0.14),
    (3200, 0.15),
    (3700, 0.16),
    (4200, 0.17),
    (4700, 0.18),
    (5200, 0.19),
    (5700, 0.20),
    (6200, 0.21),
    (6700, 0.22),
    (7200, 0.23),
]

def calc_tax(income):
    tax = 0
    min_income
    for max_income, tax_rate in TAX_RATES:
        if income <= max_income:
            tax += tax_rate * (income - min_income)
            min_income = max_income
        else:
            return tax
