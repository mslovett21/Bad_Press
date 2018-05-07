import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string

## returns dataframes for each of the 3 newspapers
def return_dataframe(news_data):
    news_df = pd.read_json(news_data)

    #FN_df=FN_df[["articles_date","article_text", "articles_title", "newspaper_name","first_name","last_name", "articles_link"]]
    news_df.rename(columns={'articles_text': 'article_text'}, inplace=True)

    return news_df

def return_data(table, index_column_name, value, desired_column):
    row = table[table[index_column_name] == value]
    row = row.reset_index(drop=True)
    return row[desired_column][0]

def substring_search(substring, string):
    if substring in string:
        return True
    return False

def connect_strings(all_data):
    for i in range(len(all_data)):
        if type(all_data["article_text"][i]) == list:
            all_data["article_text"][i] = ' '.join(all_data["article_text"][i])
        all_data["articles_title"][i] = ''.join(all_data["articles_title"][i])
        if type(all_data["articles_date"][i]) == list:
            all_data["articles_date"][i] = ' '.join(all_data["articles_date"][i])
    return all_data

def find_candidates(all_data, all_candidates):
    df_columns = list(all_data.columns.values)
    all_rows = [all_data]
    for index,row in all_data.iterrows():
        if(pd.isnull(row["first_name"])): ## check is cell value is NaN
            for name in all_candidates:
                if substring_search(name,row['article_text']):
                    new_row = pd.DataFrame(columns = df_columns)
                    new_row.loc[0] = all_data.iloc[index]
                    new_row["first_name"] = " ".join(name.split()[0:-1])
                    new_row["last_name"] = name.split()[-1]
                    all_rows.append(new_row)

    all_data = pd.concat(all_rows, ignore_index=True)

    return all_data

def remove_missing_data(all_data):
    # or substring_search(name.split()[-1],row['article_text'])
    all_data = all_data[all_data.article_text != ""]
    all_data = all_data[all_data.articles_title != ""]
    all_data = all_data[all_data.articles_date != ""]
    all_data = all_data[all_data.first_name != ""]
    all_data = all_data[all_data.first_name.notnull()]
    all_data = all_data[all_data.articles_link.notnull()]

    return all_data

def remove_misc_links(all_data):
    df_columns = list(all_data.columns.values)
    all_rows = []
    newspapers = ["cnn.com", "nytimes.com", "foxnews.com"]
    for index,row in all_data.iterrows():
        for paper in newspapers:
            if substring_search(paper, row["articles_link"]):
                new_row = pd.DataFrame(columns = df_columns)
                new_row.loc[0] = all_data.iloc[index]
                all_rows.append(new_row)
                continue

    all_data = pd.concat(all_rows, ignore_index=True)

    return all_data

def reorder_df(all_data):
    all_data = all_data.reset_index(drop=True) ## had to set it over otherwise change didn't apply
    last_id = all_data.shape[0] + 1
    all_data['id'] = list(range(1,last_id))

    return all_data

def get_candidate_fk(all_data, candidate_table):
    candidate_ids = []
    all_names = [x+" "+y for x,y in list(zip(all_data["first_name"].tolist(), all_data["last_name"].tolist()))]
    candidate_ids = [return_data(candidate_table, "name", x, "id") for x in all_names]

    all_data["candidate_fk"] = candidate_ids
    return all_data

def get_state_fk(all_data, candidate_table):
    state_ids = []
    all_candidate_ids = all_data["candidate_fk"].tolist()
    state_ids = [return_data(candidate_table, "id", x, "state_fk") for x in all_candidate_ids]

    all_data["state_fk"] = state_ids
    return all_data

def get_newspaper_fk(all_data, source_table):
    newspaper_to_key = {}
    for index, row in source_table.iterrows():
        #print(name)
        newspaper_to_key[row["name"]] = row['id']

    newspaper_shorthand = {'CNN':'CNN', 'NYT':'New York Times', 'foxnews':'FoxNews', "Fox News":'FoxNews'}

    for index, row in all_data.iterrows():
        newspaper_name = newspaper_shorthand[row['newspaper_name']]
        #print(row['source_fk'], " ", newspaper_name, " " , newspaper_to_key[newspaper_name])
        id_val = newspaper_to_key[newspaper_name]
        all_data.at[index,"source_fk"] = id_val

    return all_data

def standardize_date(all_data):
    days = list(range(1,32))
    months = {"january":1, "jan":1, "february":2, "feb":2, "march":3, "mar":3, "april":4, "apr":4,
              "may":5, "june":6, "july":7, "august":8, "aug":8,
              "september":9, "sept":9, "october":10, "oct":10, "november":11, "nov":11, "december":12, "dec":12}
    years = list(range(1850, 2019))

    for i in range(len(all_data)):
        month = ""
        day = ""
        year = ""
        date = all_data["articles_date"][i]

        if(all_data["newspaper_name"][i] != "foxnews"):
            date = date.split()
            date = [x.lower().replace(',','').replace('.','') for x in date]

            for x in date:
                try:
                    y = int(x)
                except ValueError:
                    y = -1
                if y in days:
                    day = day + x
                elif y in years:
                    year = year + x
                elif x in months.keys():
                    month = month + str(months[x])
                else:
                    continue
        else:
            year = date[:4]
            month =  date[5:7]
            day = date[8:10]
        all_data["articles_date"][i] = " ".join([day, month, year])

    return all_data

## TODO: pass in folder name, and state names/ids to loop through files
def structure_data(data_folder, state_data, all_candidates, candidate_table, source_table, output_file):
    ## create frames for each state
    frames = []
    count = 0;
    for state in state_data:
        for data_file in state:
            news_df = return_dataframe(data_folder+data_file)
            frames.append(news_df);
        count += 1

    # combine all frames
    all_data = pd.concat(frames, ignore_index=True)
    all_data.is_copy = False
    pd.options.mode.chained_assignment = None  ## to allow references to original objects and not copies

    all_data = connect_strings(all_data)

    all_data = find_candidates(all_data, all_candidates)

    all_data = remove_missing_data(all_data)

    all_data = reorder_df(all_data)

    all_data = remove_misc_links(all_data)

    all_data = reorder_df(all_data)

    all_data = get_candidate_fk(all_data, candidate_table)

    #all_data = get_state_fk(all_data, candidate_table)

    all_data = get_newspaper_fk(all_data, source_table)

    all_data = standardize_date(all_data)

    with open(output_file, 'w') as f:
        f.write(all_data.to_json(orient = "records"))
