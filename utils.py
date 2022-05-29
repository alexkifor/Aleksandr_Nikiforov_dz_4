import requests
import re
import numpy as np
import datetime
def currency_rates(args):
    char_codes = []
    nominals = []
    values = []
    rates = []
    date = []
    answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    my_list = answer.text
    my_list_2 = re.split('Date="|" name', my_list)
    for i in my_list_2:
        i = i.replace('.', '')
        if i.isdigit():
            date.append(int(i))
    out_date = datetime.date(date[0] % 10000, (date[0] // 10000) % 10, date[0] // 1000000)
    my_list_1 = re.split('[><]', my_list)
    for cod in my_list_1:
        if cod.isupper():
            char_codes.append(cod)
    for nomin in my_list_1:
        if nomin.isdigit():
            if int(nomin) == 1 or int(nomin) == 10 or int(nomin) == 100 or int(nomin) == 1000 or int(nomin) == 10000:
                nominals.append(int(nomin))
    for value in my_list_1:
        if value.count(','):
            value = value.replace(',', '.')
            values.append(float(value))
    values = np.array(values)
    nominals = np.array(nominals)
    rates_1 = (values / nominals).tolist()
    for rate in rates_1:
        rate = round(rate, 8)
        rates.append(rate)
    out_dict = dict(zip(char_codes, rates))
    args = args.upper()
    return (out_dict.get(args), out_date.strftime('%Y-%m-%d'))





