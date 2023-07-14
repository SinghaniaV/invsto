from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Float


class Tick_data(Base):
	__tablename__ = 'tick_data'

	id = Column(Integer, primary_key=True, autoincrement=True)
	datetime = Column(DateTime)
	close = Column('close', Float)
	high = Column(Float)
	low = Column(Float)
	open = Column(Float)
	volume = Column(Integer)
	instrument = Column(String(9))

	def __init__(self, datetime, close, high, low, open, volume, instrument):
		self.datetime = datetime
		self.close = close
		self.high = high
		self.low = low
		self.open = open
		self.volume = volume
		self.instrument = instrument

	def __repr__(self):
		return f'({self.datetime}, {self.close}, {self.high}, {self.low}, {self.open}, {self.volume}, {self.instrument})'