import locale

locale.setlocale(locale.LC_ALL,'')

def formatNumber(number):
    return locale.currency(number,grouping=True,symbol=False)