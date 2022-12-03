import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

Database_name = "aps"
Collection_name = "sensor"
Datafile_path ='/config/workspace/aps_failure_training_set1.csv'

if __name__ =='__main__':
    df = pd.read_csv('/config/workspace/aps_failure_training_set1.csv')
    print(df.shape)

df.reset_index(inplace=True, drop=True)
json_record = list(json.loads(df.T.to_json()).values())
print(json_record[0])
client[Database_name][Collection_name].insert_many(json_record)