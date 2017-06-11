
import sys
import pprint
import traceback
import easyquotation
import requests


stock = 'cn_601766'
start = '20170604'
end = '20170609'


def get_data(stock, start, end):
    data = []
    #data = quotation.real(stock)

    url = 'http://q.stock.sohu.com/hisHq?code=%s&start=%s&end=%s' % (stock, start, end)

    r = requests.get(url)
    data = r.json()
    data = data[0]
    pprint.pprint(data)
    return data


if __name__ == '__main__':
    data = get_data(stock, start, end)
    #pp.pprint(data)
