# salary_utils.py

def gross_salary(basic, hra, da):
    return basic + hra + da


def deductions(gross):
    # PF = 12% of gross salary
    pf = gross * 0.12

    # Tax = 5% of gross salary
    tax = gross * 0.05

    return pf + tax


def net_salary(gross, deduction):
    return gross - deduction