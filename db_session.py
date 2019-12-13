from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_declarative import Base, Flat

engine = create_engine('sqlite:///flats.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def fill_up_table():
    from flats_template import all_flats
    for flat in all_flats:
        session.add(flat)
    session.commit()


def update_flat(flat_floor, new_status=None, new_price=None):
    flat = session.query(Flat).filter(Flat.floor == flat_floor).one()
    if new_price:
        flat.price = new_price
    if new_status:
        flat.status = new_status
    session.commit()


def select_all_flats():
    all_flats = session.query(Flat).all()
    return all_flats


if __name__ == '__main__':
    # fill_up_table()
    update_flat(flat_floor=3, new_status='rezerwacja', new_price=315360)

    flats = session.query(Flat).all()
    for flat in flats:
        print(flat)
