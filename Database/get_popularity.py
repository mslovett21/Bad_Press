import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string

from datetime import datetime

from clean_data import return_data

def create_popularity_json(candidate_table, input_file, output_file):

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    months = {1:"january", 2:"february",  3:"march", 4:"april",
              5:"may", 6:"june", 7:"july", 8:"august",
              9:"september", 10:"october", 11:"november", 12:"december"}


    month_year_pairs = []

    month_year_pairs.extend([ (x,currentYear) for x in list(range(1,currentMonth+1)) ])
    month_year_pairs.extend([ (x,currentYear-1) for x in list(range(currentMonth+1,13)) ])

    all_data = pd.read_json(input_file)

    all_candidates = candidate_table["id"].tolist()

    table_columns = ["january", "february", "march", "april", "may", "june", "july", "august", "september"
                     , "october", "november", "december", "last_name"]

    popularity_table = pd.DataFrame(columns = table_columns)

    for candidate in all_candidates:

        counts = {}
        for i in range(1,13):
            counts[i] = 0

        current_table = all_data[all_data["candidate_fk"]==candidate]
        current_table = current_table.reset_index(drop=True) ## had to set it over otherwise change didn't apply
        print(len(current_table))
        for i in range(len(current_table)):
            date = current_table["articles_date"][i]
            date = date.split()

            if ( (int(date[1]), int(date[2])) in month_year_pairs):
                counts[int(date[1])] += 1

        one_row = pd.DataFrame(columns = table_columns)

        count_list = [counts[x] for x in range(1,13)]

        full_name = return_data(candidate_table, "id", candidate, "name").split()
        last_name = full_name[-1]

        row_values = count_list + [last_name]
        one_row.loc[0] = row_values
        frames = [popularity_table, one_row]
        popularity_table = pd.concat(frames)

    with open(output_file, 'w') as f:
        f.write(popularity_table.to_json(orient = "records"))
