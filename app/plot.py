
import os
import pandas as pd
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from pymongo import MongoClient


load_dotenv('existing/mflix/.env', override=True, verbose=True)

USERNAME = os.getenv('PGUSERNAME')
PASSWORD = os.getenv('PGPASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
SERVER = os.getenv('SERVER')
DATABASE = os.getenv('NAME').replace('"', '')
URL = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

client = MongoClient(URL)
db = client[DATABASE]

pipeline = [
    {
        '$group': {
            '_id': '$year',
            'amount': {'$sum': 1}
        }
    },
    {
        '$sort': {'_id': 1}
    }
]

answer = pd.DataFrame(list(db.movies.aggregate(pipeline)))



plt.figure(figsize=(12, 6))
plt.boxplot(answer['amount'], patch_artist=True)
plt.xticks(ticks=range(1, len(answer['_id'])+1), labels=answer['_id'], rotation=45)
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Number of Films by Year')
plt.legend(['Films'])
plt.tight_layout()
plt.savefig('plot.png')

