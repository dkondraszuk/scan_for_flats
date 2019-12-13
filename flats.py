from collections import namedtuple

FlatStatus = namedtuple('FlatStatus', 'floor, status, price, id')


flat1 = FlatStatus(floor=1,
                   status='wolny',
                   price=602000,
                   id='13902')

flat2 = FlatStatus(floor=2,
                   status='wolny',
                   price=602000,
                   id='13941')

flat3 = FlatStatus(floor=3,
                   status='wolny',
                   price=602000,
                   id='13931')

flat4 = FlatStatus(floor=4,
                   status='wolny',
                   price=602000,
                   id='14023')

flat5 = FlatStatus(floor=5,
                   status='wolny',
                   price=602000,
                   id='14005')

flat6 = FlatStatus(floor=6,
                   status='wolny',
                   price=602000,
                   id='14011')

flat7 = FlatStatus(floor=7,
                   status='wolny',
                   price=602000,
                   id='13968')

all_flats = [flat1, flat2, flat3, flat4, flat5, flat6, flat7]
