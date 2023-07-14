from fastapi import FastAPI
from database import engine, Session, Base
from models import Tick_data
import pandas as pd

app = FastAPI()

Base.metadata.create_all(engine)

try:
	df = pd.read_excel('..\data\HINDALCO.xlsx')
except Exception as e:
	print('Unable to access csv file', repr(e))
	
try:
	for index, row in df.iterrows():
		data = Tick_data(datetime=row['datetime'], close=row['close'], high=['high'], low=['low '], open=['open'], volume=['volume'], instrument=['instrument'])
		Session.add(data)

except Exception as e:
	Session.rollback()
	print('Unable to populate tables', repr(e))
else:
	Session.commit()

@app.get('/')
def index():
    return "done"