import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string

def add_manual(output_file):
    all_rows = []
    original_data = pd.read_json("set_2_data/ALL_DATA.json")
    df_columns = list(original_data.columns.values)


    with open("manual_articles/freitas_1.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0]["article_text"] = content
    new_row[0]["articles_date"] = "16 3 2018"
    new_row[0]["articles_link"] = "http://www.foxnews.com/opinion/2018/03/16/gop-legislator-calls-out-democratic-hate-speech-on-second-amendment.html"
    new_row[0]["articles_title"] = "A GOP legislator calls out Democratic hate speech on the Second Amendment"
    new_row[0]["candidate_fk"] = 9
    new_row[0]["first_name"] = "Nicholas"
    new_row[0]["id"] = 1
    new_row[0]["last_name"] = "Freitas"
    new_row[0]["newspaper_name"] = "foxnews"
    new_row[0]["source_fk"] = 2
    new_row[0]["state_fk"] = 2
    all_rows.append(new_row)

    with open("manual_articles/freitas_2.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0]["article_text"] = content
    new_row[0]["articles_date"] = "11 4 2018"
    new_row[0]["articles_link"] = "http://insider.foxnews.com/2018/04/11/corey-stewart-illegal-immigration-ms-13-election-against-tim-kaine-nick-freitas"
    new_row[0]["articles_title"] = "GOP Kaine Opponent Rips VA Gov for Vetoing Bill Banning Sanctuary Cities"
    new_row[0]["candidate_fk"] = 9
    new_row[0]["first_name"] = "Nicholas"
    new_row[0]["id"] = 2
    new_row[0]["last_name"] = "Freitas"
    new_row[0]["newspaper_name"] = "foxnews"
    new_row[0]["source_fk"] = 2
    new_row[0]["state_fk"] = 2
    all_rows.append(new_row)

    with open("manual_articles/freitas_3.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0]["article_text"] = content
    new_row[0]["articles_date"] = "6 3 2018"
    new_row[0]["articles_link"] = "http://insider.foxnews.com/2018/03/06/virginia-senate-candidate-nick-freitas-goes-viral-fiery-defense-gun-rights"
    new_row[0]["articles_title"] = "'I Won't Accept a False Narrative': VA Lawmaker's Defense of Gun Rights Goes Viral"
    new_row[0]["candidate_fk"] = 9
    new_row[0]["first_name"] = "Nicholas"
    new_row[0]["id"] = 3
    new_row[0]["last_name"] = "Freitas"
    new_row[0]["newspaper_name"] = "foxnews"
    new_row[0]["source_fk"] = 2
    new_row[0]["state_fk"] = 2
    all_rows.append(new_row)

    with open("manual_articles/jackson_1.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0]["article_text"] = content
    new_row[0]["articles_date"] = "4 5 2018"
    new_row[0]["articles_link"] = "https://www.cnn.com/2018/05/04/opinions/strange-collection-of-extremists-running-as-republicans-opinion-love/index.html"
    new_row[0]["articles_title"] = "The strange collection of extremists running for office as Republicans"
    new_row[0]["candidate_fk"] = 10
    new_row[0]["first_name"] = "E.W."
    new_row[0]["id"] = 4
    new_row[0]["last_name"] = "Jackson"
    new_row[0]["newspaper_name"] = "CNN"
    new_row[0]["source_fk"] = 1
    new_row[0]["state_fk"] = 2
    all_rows.append(new_row)

    with open("manual_articles/jackson_2.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0]["article_text"] = content
    new_row[0]["articles_date"] = "22 6 2016"
    new_row[0]["articles_link"] = "https://www.cnn.com/2016/06/21/politics/donald-trump-hillary-clinton-religion/index.html"
    new_row[0]["articles_title"] = "Trump: 'We don't know anything about Hillary in terms of religion'"
    new_row[0]["candidate_fk"] = 10
    new_row[0]["first_name"] = "E.W."
    new_row[0]["id"] = 5
    new_row[0]["last_name"] = "Jackson"
    new_row[0]["newspaper_name"] = "CNN"
    new_row[0]["source_fk"] = 1
    new_row[0]["state_fk"] = 2
    all_rows.append(new_row)

    with open("manual_articles/jackson_3.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0]["article_text"] = content
    new_row[0]["articles_date"] = "17 5 2016"
    new_row[0]["articles_link"] = "https://www.cnn.com/2016/05/17/politics/conservatives-slow-walk-donald-trump-support/index.html"
    new_row[0]["articles_title"] = "Conservatives in secretive group 'slow walk' Trump support"
    new_row[0]["candidate_fk"] = 10
    new_row[0]["first_name"] = "E.W."
    new_row[0]["id"] = 6
    new_row[0]["last_name"] = "Jackson"
    new_row[0]["newspaper_name"] = "CNN"
    new_row[0]["source_fk"] = 1
    new_row[0]["state_fk"] = 2
    all_rows.append(new_row)

    all_data = pd.concat(all_rows, ignore_index=True)

    with open(output_file, 'w') as f:
        f.write(all_data.to_json(orient = "records"))
