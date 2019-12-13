from db_declarative import Flat

FREE = 'wolny'
SOLD = 'sprzedany'
RESERVED = 'zarezerwowany'


flat1 = Flat(floor=1,
             status=FREE,
             price=602000,
             flat_id='13902')

flat2 = Flat(floor=2,
             status=FREE,
             price=602000,
             flat_id='13941')

flat3 = Flat(floor=3,
             status=FREE,
             price=602000,
             flat_id='13931')

flat4 = Flat(floor=4,
             status=FREE,
             price=602000,
             flat_id='14023')

flat5 = Flat(floor=5,
             status=FREE,
             price=602000,
             flat_id='14005')

flat6 = Flat(floor=6,
             status=FREE,
             price=602000,
             flat_id='14011')

flat7 = Flat(floor=7,
             status=FREE,
             price=602000,
             flat_id='13968')

all_flats = [flat1, flat2, flat3, flat4, flat5, flat6, flat7]
