import urllib.request; import json; from time import sleep

while True:
    try:
        currency = input('Podaj walutę: ')
        if not currency.lower() == 'pln':
            compare_currency = 'zł'
            url = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency}/last/7'
            with urllib.request.urlopen(url) as server_answer:
                url = json.load(server_answer)
            day1 = url['rates'][0]['mid']
            day2 = url['rates'][1]['mid']
            day3 = url['rates'][2]['mid']
            day4 = url['rates'][3]['mid']
            day5 = url['rates'][4]['mid']
            day6 = url['rates'][4]['mid']
            day7 = url['rates'][6]['mid']; break
        else:
            compare_currency = '$'
            url = 'http://api.nbp.pl/api/exchangerates/rates/A/usd/last/7'
            with urllib.request.urlopen(url) as server_answer:
                url = json.load(server_answer)
            day1 = 1 / url['rates'][0]['mid']
            day2 = 1 / url['rates'][1]['mid']
            day3 = 1 / url['rates'][2]['mid']
            day4 = 1 / url['rates'][3]['mid']
            day5 = 1 / url['rates'][4]['mid']
            day6 = 1 / url['rates'][4]['mid']
            day7 = 1 / url['rates'][6]['mid']; break
    except Exception:
        print('Musisz wpisać ISO 4217 waluty, np. USD, PLN.'); sleep(1)

if day7 > day1:
    rise = day7 - day1
    difference_answer = f'Wartość wzrosła o {rise:.4f} {compare_currency}.'
else:
    fall = day1 - day7
    difference_answer = f'Wartość spadła o {fall:.4f} {compare_currency}.'
print(difference_answer)

max = max(day1, day2, day3, day4, day5, day6, day7)
min = min(day1, day2, day3, day4, day5, day6, day7)
max_answer = f'Najwyższy kurs to {max:.4f} {compare_currency}.'
min_answer = f'Najniższy kurs to {min:.4f} {compare_currency}.'
print(max_answer); print(min_answer)