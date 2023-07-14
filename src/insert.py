import pandas as pd
from database import session, Base, engine
from models import Tick_data
from datetime import datetime

Base.metadata.create_all(engine)

# data = Tick_data(datetime.now(), 1, 2, 3, 4, 5, "vishal")
# session.add(data)
# session.commit()

try:
	df = pd.read_excel('..\data\HINDALCO.xlsx')
except Exception as e:
	print('Unable to access csv file', repr(e))
	
try:
	for index, row in df.iterrows():
		data = Tick_data(datetime.now(), close=row['close'], high=['high'], low=['low'], open=['open'], volume=['volume'], instrument=['instrument'])

		session.add(data)

except Exception as e:
	session.rollback()
	print('Unable to populate tables', repr(e))
else:
	session.commit()
