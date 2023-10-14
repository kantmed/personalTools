import locale

locale.setlocale(locale.LC_ALL,'fr_FR')

def formatNumber(number):
    return locale.currency(number,grouping=True,symbol=False)