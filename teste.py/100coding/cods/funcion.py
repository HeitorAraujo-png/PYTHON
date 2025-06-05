def life_in_weeks(years):
    rest = (90 * 365) / 7
    print(f'Quantos anos você tem? {years}')
    rest_life = (years * 365) / 7
    x = rest - rest_life
    print(f'You have {x:.0f} weeks left.')
life_in_weeks(56)