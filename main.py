w = (input('Podaj wagę: ')).lower()
wz = (input('Podaj wzrost: ')).lower()
if 'g' in w and 'k' not in w:
    w = float(w.strip('g.')) / 1000
else:
    w = float(w.strip('kg.'))
if 'c' in wz:
    wz = float(wz.strip('cm.')) / 100
else:
    wz = float(wz.strip('m.'))
bmi = w / (wz**2)
if bmi < 16.0:
    wer = 'wygłodzenie'
elif bmi < 17.0:
    wer = 'wychudzenie'
elif bmi < 18.5:
    wer = 'niedowaga'
elif bmi < 25.0:
    wer = 'OK'
elif bmi < 30.0:
    wer = 'nadwaga'
elif bmi < 35.0:
    wer = 'otyłość I stopnia'
elif bmi < 40.0:
    wer = 'otyłość II stopnia'
else:
    wer = 'otyłość III stopnia'
print(f'BMI wynosi: {bmi}, {wer}.')