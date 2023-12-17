import time
while True:
    linguae = input('Choose a language:\n'
                    '1 - Latin\n'
                    '2 - English\n'
                    '3 - Polish\n'
                    '4 - Ukrainian\n'
                    '5 - Russian\n'
                    '6 - Sindarin\n'
                    '7 - Orcish\n'
                    '8 - Valyrian\n')
    if linguae == '1' or linguae.lower() == 'latin':
        from linguae_numerus_coniectura import Latin
        linguae = Latin; break
    if linguae == '2' or linguae.lower() == 'english':
        from linguae_numerus_coniectura import English
        linguae = English; break
    if linguae == '3' or linguae.lower() == 'polish':
        from linguae_numerus_coniectura import Polish
        linguae = Polish; break
    if linguae == '4' or linguae.lower() == 'ukrainian':
        from linguae_numerus_coniectura import Ukrainian
        linguae = Ukrainian; break
    if linguae == '5' or linguae.lower() == 'russian':
        from linguae_numerus_coniectura import Russian
        linguae = Russian; break
    if linguae == '6' or linguae.lower() == 'sindarin':
        from linguae_numerus_coniectura import Sindarin
        linguae = Sindarin; break
    if linguae == '7' or linguae.lower() == 'orcish':
        from linguae_numerus_coniectura import Orcish
        linguae = Orcish; break
    if linguae == '8' or linguae.lower() == 'valyrian':
        from linguae_numerus_coniectura import Valyrian
        linguae = Valyrian; break
    else: print('You need to type in 1, 2, 3, 4, 5, 6, 7 or 8.')
    time.sleep(1)
primus_terminus = int(input(linguae[0]))
secundus_terminus = int(input(linguae[1]))
while True:
    numerus = int(input(f'{linguae[2]}'
                        f'{linguae[3]}{primus_terminus} '
                        f'{linguae[4]}{secundus_terminus}: '))
    if numerus in range(primus_terminus, secundus_terminus + 1):
        break
    else:
        print(linguae[5]); continue
while True:
    coniectura = (primus_terminus + secundus_terminus) // 2
    print(f'{linguae[6]} {coniectura}?')
    respondere = input(
        f'+ ({linguae[7]} {coniectura})\n'
        f'- ({linguae[8]} {coniectura})\n'
        f'= ({linguae[9]} {coniectura})\n')
    if respondere == '+' and numerus > coniectura:
        primus_terminus = coniectura
    elif respondere == '-' and numerus < coniectura:
        secundus_terminus = coniectura
    elif respondere == '=' and numerus == coniectura:
        print(linguae[10]); exit()
    elif (respondere == '+' and not numerus > coniectura
          or respondere == '-' and not numerus < coniectura
          or respondere == '=' and not numerus == coniectura):
        print(linguae[11]); time.sleep(0.5)
    else:
        print(f"{linguae[12]} '+', '-' lub '='."); time.sleep(0.5)
