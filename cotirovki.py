import requests
import json

print('Здравствуйте, эта программа предоставляет возожность узнать самый свежий курс валют(если вы хотите узнать курс по отношению к рублю, введите один и тот же Charcode дважды)')

charcode = ['AUD - Австралийский доллар',
'AZN - Азербайджанский манат',
'GBP - Фунт Стрелингов Сеоинённого королевства',
'AMD - Армянские драмы',
'BYN - Белорусский рубль',
'BGN - Болгарский лев',
'BRL - Бразильский реал',
'HUF - Венгерские форинты',
'HKD - Гонгонский доллар',
'DKK - Датская крона',
'USD - Доллар США',
'EUR - Евро',
'INR - Индийский рупий',
'KZT - Казахстанский тенге',
'CAD - Канадский доллар',
'KGS - Киргизский сом',
'CNY - Китайский юань',
'MDL - Молдавский лей',
'NOK - Норвежская крона',
'PLN - Польский злотый',
'RON - Румынский лей',
'XDR - СДР(специальные права заимствования)',
'SGD - Сингапурский доллар',
'TJS - Таджитский сомони',
'TRY - Турецкая лира',
'TMT - Новый туркенский манат',
'UZS - Узбекский сум',
'UAH - Украинская гривна',
'CZK - Чешская крона',
'SEK - Шведская крона',
'CHF - Швейцарский франк',
'ZAR - Южноафриканский рэнд',
'KRW - Вон Республики Корея',
'JPY - Японский иен']

def toFixed(numObj, digits = 0):
    return f"{numObj:.{digits}f}"

r = f'https://www.cbr-xml-daily.ru/daily_json.js'

response = requests.get(r)

cotirovki = response.json()

cot1 = cotirovki['Valute']
n = input('Показать список CharCode?: ')
if n == 'да':
    for x in range(0, 33):
        print(charcode[x])

cot2 = cot1[input('Введите CharCode1: ')]
no = cot2['Nominal']
na = cot2['Name']
v = cot2['Value']
p = cot2['Previous']

cot3 = cot1[input('Введите CharCode2: ')]
if cot3 == cot2:
    print('Номинал: ',no)
    print('Название: ',na)
    print('Стоимость: ',toFixed(v, 2), 'р')
    print('Предыдущая: ',toFixed(p, 2), 'р')
else:
    no1 = cot3['Nominal']
    na1 = cot3['Name']
    v1 = cot3['Value']
    p1 = cot3['Previous']
    vv1 = v / v1
    print('Номиналы: ', no, '/', no1)
    print('Название: ', na, '/', na1)
    print('Стоимость: ', toFixed(vv1, 2))
