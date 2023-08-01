import json

import glob

import uuid

import os

import pandas as pd

#folder paths are hard coded

#schemas.json path is also hard coded

#modularization with reusability

def get_columns(ds):

    with open('C:/Users/Ganesh Naidu/AppData/Local/Programs/Python/who-converter/data/retail_db/schemas.json') as fp:

        schemas = json.load(fp)

    try:

        schema = schemas.get(ds)

        if not schema:

            raise KeyError

        cols = sorted(schema, key=lambda s: s['column_position'])

        columns = [col['column_name'] for col in cols]

        return columns

    except KeyError:

        print(f'schema not found {ds}')

        return

def main():

    for path in glob.glob('C:/Users/Ganesh Naidu/AppData/Local/Programs/Python/who-converter/data/retail_db/*'):

        if os.path.isdir(path):

            ds = os.path.split(path)[1]

            for file in glob.glob(f'{path}/part*'):

                df = pd.read_csv(file, names=get_columns(ds))

                os.makedirs(f'data/retail_demo/{ds}', exist_ok=True)

                df.to_json(

                    f'data/retail_demo/{ds}/part-{str(uuid.uuid1())}.json',

                    orient='records',

                    lines=True

                )

                print(f'Number of records processed for {os.path.split(file)[1]} in {ds} is {df.shape[0]}')

 

 

if __name__ == '__main__':

    main()