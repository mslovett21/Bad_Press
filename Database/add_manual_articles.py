import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string

def add_manual(output_file):
    all_rows = []
    original_data = pd.read_json("set_2_data/ALL_DATA.json")
    df_columns = list(original_data.columns.values)
    df_columns.append("issue")

    new_table = pd.DataFrame(columns = df_columns)

    with open("manual_articles/freitas_1.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_table = new_table.append(pd.DataFrame([[content,"16 3 2018","http://www.foxnews.com/opinion/2018/03/16/gop-legislator-calls-out-democratic-hate-speech-on-second-amendment.html","A GOP legislator calls out Democratic hate speech on the Second Amendment",9,"Nicholas",1,"Freitas","foxnews",2,2,6]],columns= df_columns), ignore_index=True)

    with open("manual_articles/freitas_2.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)

    new_table = new_table.append(pd.DataFrame([[content,"11 4 2018","http://insider.foxnews.com/2018/04/11/corey-stewart-illegal-immigration-ms-13-election-against-tim-kaine-nick-freitas","GOP Kaine Opponent Rips VA Gov for Vetoing Bill Banning Sanctuary Cities",9,"Nicholas",2,"Freitas","foxnews",2,2,5]],columns= df_columns), ignore_index=True)

    with open("manual_articles/freitas_3.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)

    new_table = new_table.append(pd.DataFrame([[content,"6 3 2018","http://insider.foxnews.com/2018/03/06/virginia-senate-candidate-nick-freitas-goes-viral-fiery-defense-gun-rights","'I Won't Accept a False Narrative': VA Lawmaker's Defense of Gun Rights Goes Viral",9,"Nicholas",3,"Freitas","foxnews",2,2,3]],columns= df_columns), ignore_index=True)


    with open("manual_articles/jackson_1.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)

    new_table = new_table.append(pd.DataFrame([[content,"4 5 2018","https://www.cnn.com/2018/05/04/opinions/strange-collection-of-extremists-running-as-republicans-opinion-love/index.html","The strange collection of extremists running for office as Republicans",10,"E.W.",4,"Jackson","CNN",1,2,6]],columns= df_columns), ignore_index=True)

    with open("manual_articles/jackson_2.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)

    new_table = new_table.append(pd.DataFrame([[content,"22 6 2016","https://www.cnn.com/2016/06/21/politics/donald-trump-hillary-clinton-religion/index.html","Trump: 'We don't know anything about Hillary in terms of religion'",10,"E.W.",5,"Jackson","CNN",1,2,6]],columns= df_columns), ignore_index=True)

    with open("manual_articles/jackson_3.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)

    new_table = new_table.append(pd.DataFrame([[content,"17 5 2016","https://www.cnn.com/2016/05/17/politics/conservatives-slow-walk-donald-trump-support/index.html","Conservatives in secretive group 'slow walk' Trump support",10,"E.W.",6,"Jackson","CNN",1,2,6]],columns= df_columns), ignore_index=True)


    '''

    with open("manual_articles/freitas_1.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0] = original_data.iloc[0]
    new_row["article_text"][0] = content
    new_row["articles_date"][0] = "16 3 2018"
    new_row["articles_link"][0] = "http://www.foxnews.com/opinion/2018/03/16/gop-legislator-calls-out-democratic-hate-speech-on-second-amendment.html"
    new_row["articles_title"][0] = "A GOP legislator calls out Democratic hate speech on the Second Amendment"
    new_row["candidate_fk"][0] = 9
    new_row["first_name"][0] = "Nicholas"
    new_row["id"][0] = 1
    new_row["last_name"][0] = "Freitas"
    new_row["newspaper_name"][0] = "foxnews"
    new_row["source_fk"][0] = 2
    new_row["state_fk"][0] = 2
    all_rows.append(new_row)

    with open("manual_articles/freitas_2.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0] = original_data.iloc[0]
    new_row["article_text"][0] = content
    new_row["articles_date"][0] = "11 4 2018"
    new_row["articles_link"][0] = "http://insider.foxnews.com/2018/04/11/corey-stewart-illegal-immigration-ms-13-election-against-tim-kaine-nick-freitas"
    new_row["articles_title"][0] = "GOP Kaine Opponent Rips VA Gov for Vetoing Bill Banning Sanctuary Cities"
    new_row["candidate_fk"][0] = 9
    new_row["first_name"][0] = "Nicholas"
    new_row["id"][0] = 2
    new_row["last_name"][0] = "Freitas"
    new_row["newspaper_name"][0] = "foxnews"
    new_row["source_fk"][0] = 2
    new_row["state_fk"][0] = 2
    all_rows.append(new_row)

    with open("manual_articles/freitas_3.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0] = original_data.iloc[0]
    new_row["article_text"][0] = content
    new_row["articles_date"][0] = "6 3 2018"
    new_row["articles_link"][0] = "http://insider.foxnews.com/2018/03/06/virginia-senate-candidate-nick-freitas-goes-viral-fiery-defense-gun-rights"
    new_row["articles_title"][0] = "'I Won't Accept a False Narrative': VA Lawmaker's Defense of Gun Rights Goes Viral"
    new_row["candidate_fk"][0] = 9
    new_row["first_name"][0] = "Nicholas"
    new_row["id"][0] = 3
    new_row["last_name"][0] = "Freitas"
    new_row["newspaper_name"][0] = "foxnews"
    new_row["source_fk"][0] = 2
    new_row["state_fk"][0] = 2
    all_rows.append(new_row)

    with open("manual_articles/jackson_1.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0] = original_data.iloc[0]
    new_row["article_text"][0] = content
    new_row["articles_date"][0]= "4 5 2018"
    new_row["articles_link"][0] = "https://www.cnn.com/2018/05/04/opinions/strange-collection-of-extremists-running-as-republicans-opinion-love/index.html"
    new_row["articles_title"][0] = "The strange collection of extremists running for office as Republicans"
    new_row["candidate_fk"][0] = 10
    new_row["first_name"][0]= "E.W."
    new_row["id"][0] = 4
    new_row["last_name"][0] = "Jackson"
    new_row["newspaper_name"][0] = "CNN"
    new_row["source_fk"][0] = 1
    new_row["state_fk"][0] = 2
    all_rows.append(new_row)

    with open("manual_articles/jackson_2.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0] = original_data.iloc[0]
    new_row["article_text"][0] = content
    new_row["articles_date"][0] = "22 6 2016"
    new_row["articles_link"][0] = "https://www.cnn.com/2016/06/21/politics/donald-trump-hillary-clinton-religion/index.html"
    new_row["articles_title"][0] = "Trump: 'We don't know anything about Hillary in terms of religion'"
    new_row["candidate_fk"][0] = 10
    new_row["first_name"][0] = "E.W."
    new_row["id"][0] = 5
    new_row["last_name"][0] = "Jackson"
    new_row["newspaper_name"][0] = "CNN"
    new_row["source_fk"][0] = 1
    new_row["state_fk"][0] = 2
    all_rows.append(new_row)

    with open("manual_articles/jackson_3.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = " ".join(content)
    new_row = pd.DataFrame(columns = df_columns)
    new_row[0] = original_data.iloc[0]
    new_row["article_text"][0] = content
    new_row["articles_date"][0] = "17 5 2016"
    new_row["articles_link"][0] = "https://www.cnn.com/2016/05/17/politics/conservatives-slow-walk-donald-trump-support/index.html"
    new_row["articles_title"][0] = "Conservatives in secretive group 'slow walk' Trump support"
    new_row["candidate_fk"][0] = 10
    new_row["first_name"][0] = "E.W."
    new_row["id"][0] = 6
    new_row["last_name"][0] = "Jackson"
    new_row["newspaper_name"][0] = "CNN"
    new_row["source_fk"][0] = 1
    new_row["state_fk"][0] = 2
    all_rows.append(new_row)
'''

    with open(output_file, 'w') as f:
        f.write(new_table.to_json(orient = "records"))
