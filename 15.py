from baza_danych_15 import osoby
print('1. Wszystkie osoby o wzroście powyżej 1.80:')
for persona in osoby:
    nomen = persona['imie']; cognomen = persona['nazwisko']
    altitudo = persona['wzrost']
    if altitudo > 1.8:
        print(nomen + ' ' + cognomen)
print('\n2. Wszystkie osoby urodzone przed 1960 rokiem:')
for persona in osoby:
    nomen = persona['imie']; cognomen = persona['nazwisko']
    annus_natalis = persona['rok_urodzenia']
    if annus_natalis < 1960:
        print(nomen + ' ' + cognomen)
print('\n3. Wszystkie osoby o wadze poniżej 80:')
for persona in osoby:
    nomen = persona['imie']; cognomen = persona['nazwisko']
    pondus = persona['waga']
    if pondus < 80:
        print(nomen + ' ' + cognomen)
print('\n4. Liczba osób z imieniem Jakub:')
numerare = 0
for persona in osoby:
    nomen = persona['imie']
    if nomen == 'Jakub':
        numerare += 1
print(numerare)
print('\n5. Wszystkie osoby wraz z ich BMI:')
for persona in osoby:
    nomen = persona['imie']; cognomen = persona['nazwisko']
    pondus = persona['waga']; altitudo = persona['wzrost']
    BMI = pondus / altitudo ** 2
    print(nomen + ' ' + cognomen + '   BMI: ' + str(BMI))
print('\n6. Największe i najmniejsze BMI:')
max_BMI = 0
min_BMI = 1000000000
for persona in osoby:
    pondus = persona['waga']; altitudo = persona['wzrost']
    BMI = pondus / altitudo ** 2
    if BMI > max_BMI:
        max_BMI = BMI
    if BMI < min_BMI:
        min_BMI = BMI
print(f'Największe BMI: {max_BMI}')
print(f'Najmniejsze BMI: {min_BMI}')
