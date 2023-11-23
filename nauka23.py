imiona = [
    'Mateusz',
    'Adam',
    'Michał',
    'Iwo',
    'Stanisław',
    'Artem',
    'Karina',
    'Maria',
]
z = []
m = []
l_lit = 0
print("Lista uczniów:")
for im in imiona:
    im = im.title()
    dl_im = len(im)
    l_lit = len(im) + l_lit
    if im[-1] == 'a':
        z.append(im)
    else:
        m.append(im)
    print(f'* {im}, {dl_im}')
dl_d_im = len(max(imiona, key = len))
dl_k_im = len(min(imiona, key = len))
k_im = min(imiona, key = len)
d_im = max(imiona, key = len)
print(f'Liczba liter wynosi: {l_lit}')
print(f'Długość najdłuższego imienia wynosi: {dl_d_im}')
print(f'Długość najkrótszego imienia wynosi: {dl_k_im}')
print(f'Najkrótsze imię: {k_im}')
print(f'Najdłuższe imię: {d_im}')
print('Imiona męskie:')
for im_m in m:
    print('* ' + im_m)
print('Imiona żeńskie:')
for im_z in z:
    print('* ' + im_z)
print("---KONIEC---")