import re; import urllib.request; import json

amount = input('Podaj sumę pieniędzy w zł: ')
currencies_amount = input('Ile walut chcesz porównać: ')
days = input('Ile dni chcesz użyć do porównania: ')

amount = float(re.sub(r'[^0-9]', '', amount))
currencies_amount = int(re.sub(r'[^0-9]', '', currencies_amount))
days = int(re.sub(r'[^0-9]', '', days))

difference_lowest = 10000000000000000000000000000000000000000000
difference_highest = -1000000000000000000000000000000000000000000

for x in range(currencies_amount):
    currency = input('Podaj ISO 4217 waluty: ')
    exec(f"currency{x} = currency")

    url = (f'http://api.nbp.pl/api'
           f'/exchangerates/rates/A/{currency}/last/{days}')
    with urllib.request.urlopen(url) as server_answer:
        url = json.load(server_answer)

    data_first = url['rates'][0]['mid']
    data_last = url['rates'][days - 1]['mid']

    day_first = amount * 1 / data_first
    day_last = day_first * data_last
    difference = day_last - amount
    exec(f"difference{x} = difference")

    if difference > difference_highest:
        difference_highest = difference
        currency_highest = currency.upper()
    if difference < difference_lowest:
        difference_lowest = difference
        currency_lowest = currency.upper()

for x in range(currencies_amount):
    exec(f"currency = currency{x}.upper()")
    exec(f"difference = difference{x}")
    statement = (f'Dla {currency} różnica po {days} dniach '
                 f'wynosi {difference:.4f} zł.')
    print(statement)

if difference_highest > 0:
    comparison_highest = 'Największy zysk'
if difference_highest < 0:
    comparison_highest = 'Najmniejsza strata'

if difference_lowest < 0:
    comparison_lowest = 'Największa strata'
if difference_lowest > 0:
    comparison_lowest = 'Najmniejszy zysk'

highest_statement = (f'{comparison_highest} wynosi '
                     f'{difference_highest:.4f} '
                     f'zł dla {currency_highest}.')

lowest_statement = (f'{comparison_lowest} wynosi '
                    f'{difference_lowest:.4f} '
                    f'zł dla {currency_lowest}.')

print(highest_statement); print(lowest_statement)
