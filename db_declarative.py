from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///flats.db')

Base = declarative_base()


class Flat(Base):
    __tablename__ = 'flats'

    id = Column(Integer, primary_key=True)
    floor = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)
    flat_id = Column(String(10), nullable=False)

    def __repr__(self):
        return f"<Flat(floor='{self.floor}', status='{self.status}', price='{self.price}', flat_id='{self.flat_id}')>"


if __name__ == '__main__':
    Base.metadata.create_all(engine)  # create db
