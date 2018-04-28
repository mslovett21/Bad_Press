import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string

## returns dataframes for each of the 3 newspapers
def return_dataframes(cnn, fn, nyt, state_id):
    CNN_df = pd.read_json(cnn)
    FN_df = pd.read_json(fn)
    NYT_df = pd.read_json(nyt)

    FN_df=FN_df[["articles_date","article_text", "articles_title", "newspaper_name","first_name","last_name", "articles_link"]]
    CNN_df.rename(columns={'articles_text': 'article_text'}, inplace=True)

    CNN_df["state_fk"] = state_id
    FN_df["state_fk"] = state_id
    NYT_df["state_fk"] = state_id

    return [CNN_df, FN_df, NYT_df]

def substring_search(substring, string):
    if substring in string:
        return True
    return False

## TODO: pass in folder name, and state names/ids to loop through files
def structure_data(all_candidates, output_file):
    ## create frames for each state
    frames = []
    frames.extend(return_dataframes("RAW_DATA/cnn_westvirginia.json","RAW_DATA/jsfoxnews_westvirginia.json","RAW_DATA/nyt_westvirginia.json",1 ))
    frames.extend(return_dataframes("RAW_DATA/cnn_virginia.json","RAW_DATA/jsfoxnews_virginia.json","RAW_DATA/nyt_westvirginia.json",2 ))
    frames.extend(return_dataframes("RAW_DATA/cnn_texas.json","RAW_DATA/jsfoxnews_texas.json","RAW_DATA/nyt_texas.json",3 ))

    # combine all frames
    all_data = pd.concat(frames, ignore_index=True)
    all_data.is_copy = False
    pd.options.mode.chained_assignment = None  ## to allow references to original objects and not copies

    for i in range(len(all_data)):
        all_data["article_text"][i] = ' '.join(all_data["article_text"][i])
        all_data["articles_title"][i] = ' '.join(all_data["articles_title"][i])
        if type(all_data["articles_date"][i]) == list:
            all_data["articles_date"][i] = ' '.join(all_data["articles_date"][i])


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

    # or substring_search(name.split()[-1],row['article_text'])
    all_data = all_data[all_data.article_text != ""]
    all_data = all_data[all_data.articles_title != ""]
    all_data = all_data[all_data.articles_date != ""]
    all_data = all_data[all_data.first_name != ""]
    all_data = all_data[all_data.first_name.notnull()]
    all_data = all_data[all_data.articles_link.notnull()]

    all_data = all_data.reset_index(drop=True) ## had to set it over otherwise change didn't apply
    last_id = all_data.shape[0] + 1
    all_data['id'] = list(range(1,last_id))

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
            #if(month == ""):
            #    print(i, date)
            #if(day == ""):
            #    print(i, date)
            #if(year == ""):
            #    print(i, date)
        else:
            year = date[:4]
            month =  date[5:7]
            day = date[8:10]
        all_data["articles_date"][i] = " ".join([day, month, year])

    with open(output_file, 'w') as f:
        f.write(all_data.to_json(orient = "records"))
