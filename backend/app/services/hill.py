def hill_equation(concentration:float,mic:float,n:float = 1.0)->float:
    survival_rate = 1 / (1+(concentration / mic) ** n)
    return survival_rate