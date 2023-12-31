import urllib.request; import json; from time import sleep
while True:
    try:
        currency1 = input('Podaj walutę z której chcesz przeliczyć: ')
        if not currency1.lower() == 'pln':
            url1 = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency1}/last'
            with urllib.request.urlopen(url1) as server_answer:
                result1 = json.load(server_answer)
            mid1 = result1['rates'][0]['mid']; break
        else:
            mid1 = 1; break
    except Exception:
        print('Musisz wpisać ISO 4217 waluty, np. USD, PLN.'); sleep(1)
while True:
    try:
        currency2 = input('Podaj walutę na którą chcesz przeliczyć: ')
        if not currency2.lower() == 'pln':
            url2 = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency2}/last'
            with urllib.request.urlopen(url2) as server_answer:
                result2 = json.load(server_answer)
            mid2 = result2['rates'][0]['mid']; break
        else:
            mid2 = 1; break
    except Exception:
        print('Musisz wpisać ISO 4217 waluty, np. USD, PLN.'); sleep(1)
amount = float(input('Podaj kwotę z której chcesz przeliczyć: '))
rate = mid1 / mid2; result = amount * rate
answer = f'{result:.3f} {currency2.upper()}'
print(answer)
