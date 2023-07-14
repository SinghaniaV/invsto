import pandas as pd
from database import session, Base, engine
from models import Tick_data
import pandas as pd

Base.metadata.create_all(engine)

def read_data(xlsx: pd.ExcelFile):

	try:
		df = pd.read_excel(xlsx)
		return df

	except Exception as e:
		return f'Unable to access Excel file, {repr(e)}'
	
def insert_data(df: pd.DataFrame):
	try:
		for index, row in df.iterrows():
			data = Tick_data(datetime=row['datetime'], close=row['close'], high=row['high'], low=row['low'], open=row['open'], volume=row['volume'], instrument=row['instrument'])

			session.add(data)

	except Exception as e:
		session.rollback()
		return f'Unable to populate tables, {repr(e)}'
	else:
		session.commit()
