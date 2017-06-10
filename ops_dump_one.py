
import sys
import pprint as pp
import traceback
import easyquotation


stock = 'sh000001'
start = '2017-01-01'
end = '2017-06-07'

quotation = easyquotation.use('sina')

def get_data(stock, start, end):
    data = []
    data = quotation.real(stock)
    return data


if __name__ == '__main__':
    data = get_data(stock, start, end)
    pp.pprint(data)
