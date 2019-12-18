import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_declarative import Base, Flat
from my_logger import log

engine = create_engine('sqlite:///flats.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def _fill_up_table():
    from flats_template import all_flats
    for flat in all_flats:
        session.add(flat)
    session.commit()


def update_flat(flat_floor, new_status=None, new_price=None):
    flat = session.query(Flat).filter(Flat.floor == flat_floor).one()
    if new_price:
        flat.price = new_price
        log(logging.DEBUG, f'Flat #{flat.flat_id} updated with new price: {new_price}')
    if new_status:
        flat.status = new_status
        log(logging.DEBUG, f'Flat #{flat.flat_id} updated with new status: {new_status}')
    session.commit()


def select_all_flats():
    all_flats = session.query(Flat).all()
    return all_flats


if __name__ == '__main__':
    # _fill_up_table()  # fill up table with default values from flats_template.py
    # update_flat(flat_floor=6, new_status='rezerwacja')
    # update_flat(flat_floor=4, new_price=466815)
    update_flat(flat_floor=7, new_price=666815, new_status='sprzedany')

    flats = session.query(Flat).all()
    for flat in flats:
        print(flat)
