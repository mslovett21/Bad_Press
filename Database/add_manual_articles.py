import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import string


    ## ADD OTHER TO NEWSPAPER CATEGORY & fk search
    ## add tags for 8 as election data
    ## past 12 month data: now its starting from may

copley = [["2 17 2017", "http://thehill.com/homenews/campaign/331589-coal-worker-takes-aim-at-manchins-senate-seat", "Coal worker takes aim at Manchin’s Senate seat", 2, "Bo", 1, "Copley", "Other", 4, 1, 8],
          ["26 6 2017","http://www.wsaz.com/content/news/Bo-Copley-to-challenge-Manchin-in-2018-Senate-race-430990093.html" , "Bo Copley to challenge Manchin in 2018 Senate race", 2, "Bo", 1, "Copley", "Other", 4, 1, 8],
          ["5 1 2018","http://www.williamsondailynews.com/news/bo-copley-talks-about-his-senate-campaign/article_d0e31758-6866-50b5-93bb-8b70de1c3e71.html" ,"Bo Copley talks about his Senate campaign" , 2, "Bo", 1, "Copley", "Other", 4, 1,1 ],
          ["3 5 2017" ,"http://wvmetronews.com/2017/05/03/laid-off-miner-running-for-u-s-senate-says-he-is-exact-opposite-of-sen-manchin/" ,"Laid-off miner running for U.S. Senate says he is “exact opposite” of Sen. Manchin", 2, "Bo", 1, "Copley", "Other", 4, 1,6 ],
          ["10 10 2017","http://insider.foxnews.com/2017/10/10/laid-coal-miner-senate-candidate-bo-copley-trump-ending-war-coal" ,"Laid-Off Coal Miner Sees Evidence on the Ground of Coal Industry Making a Turnaround" , 2, "Bo", 1, "Copley", "Other", 4, 1,8 ],
          ["2 5 2017" ,"https://www.washingtonexaminer.com/west-virginia-coal-miner-announces-senate-bid" ,"West Virginia coal miner announces Senate bid" , 2, "Bo", 1, "Copley", "Other", 4, 1,2 ]]


newbrough = [["5 5 2018" ,"https://www.wvgazettemail.com/election_2018/congress_2018/lesser-known-wv-candidates-in-us-senate-race-make-their/article_9d6c0499-6d25-5754-9ef7-75b06061cfce.html" ,"Lesser-known WV candidates in US Senate race make their case" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,3 ],
             ["23 4 2018" ,"http://thehill.com/homenews/campaign/384525-west-virginia-gop-senate-candidate-says-hed-like-to-waterboard-opioid" ,"West Virginia GOP Senate candidate says he’d like to waterboard opioid dealers" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,7 ],
             ["7 5 2018" ,"http://nbcmontana.com/news/nation-world/trump-tweet-endorses-jenkins-morrisey-says-blankenship-cant-win" ,"Trump tweet: Blankenship 'can't win' general election in West Virginia" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,8 ],
             ["28 4 2018" ,"http://www.theintelligencer.net/news/top-headlines/2018/04/u-s-senate-candidate-jack-newbrough-recovers-from-heart-attack/" ,"U.S. Senate Candidate Jack Newbrough Recovers From Heart Attack" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,8 ],
             ["1 5 2018" ,"http://www.register-herald.com/news/newbrough-wants-to-make-west-virginia-first/article_42e432d1-2618-5110-a4df-6a64cf13be3c.html" ,"Newbrough wants 'to make West Virginia first'" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,2 ],
             ["8 5 2018","https://therecorddelta.com/article/candidates-running-for-federal-office-questioned-at-forum" ,"Candidates running for federal office questioned at forum" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,2 ],
             ["24 9 2017" ,"http://www.weirtondailytimes.com/news/local-news/2017/09/weirton-resident-seeking-senate-seat/" ,"Weirton resident seeking Senate seat" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,6 ],
             ["13 3 2018" ,"http://wtov9.com/news/local/weirton-native-sets-eyes-on-gop-race-for-senate" ,"Weirton native sets eyes on GOP race for Senate" , 6, "Jack", 6, "Newbrough", "Other", 4, 1,2 ],
             ["3 12 2017" ,"http://wtov9.com/news/local/west-virginia-us-senate-candidate-holds-meet-and-greet" ,"West Virginia U.S. senate candidate holds meet-and-greet" , 6, "Jack", 6, "Newbrough", "Other", 4,1,6 ],
             ["30 9 2017" ,"http://www.theintelligencer.net/news/top-headlines/2017/09/weirton-resident-seeks-u-s-senate-seat/" , "Weirton Resident Seeks U.S. Senate Seat", 6, "Jack", 6, "Newbrough", "Other", 4, 1,2 ]]




swearengin = [["7 5 2018" ,"http://www.montgomery-herald.com/news/who-is-paula-jean-swearengin/article_07c0858e-5229-11e8-9102-03ef3d3a5b0d.html" ,"Who is Paula Jean Swearengin?" , 7, "Paula Jean", 6, "Swearengin", "Other", 4, 1,8 ],
              ["3 5 2018" ,"http://www.wtrf.com/news/politics/paula-jean-swearengin-makes-campaign-stop-in-glen-dale/1157945649" ,"Paula Jean Swearengin makes campaign stop in Glen Dale" , 7, "Paula Jean", 6, "Swearengin", "Other", 4, 1,8 ],
              ["30 8 2018" ,"https://www.rollingstone.com/politics/news/revolt-in-west-virginias-coal-country-w519647" ,"Revolt in West Virginia's Coal Country" , 7, "Paula Jean", 6, "Swearengin", "Other", 4, 1,8 ],
              ["3 5 2018" ,"http://wvpublic.org/post/outmatched-experience-and-funds-swearengin-remains-undeterred-primary-against-manchin#stream/0" ,"Outmatched in Experience and Funds, Swearengin Remains Undeterred in Primary Against Manchin" , 7, "Paula Jean", 6, "Swearengin", "Other", 4, 1,8 ],
              ["8 5 2018" ,"https://www.vox.com/policy-and-politics/2018/4/24/17261876/don-blankenship-2018-west-virginia-senate-race-joe-manchin-evan-jenkins-patrick-morrisey" ,"Don Blankenship’s surge in the West Virginia Senate race, explained" , 7, "Paula Jean", 6, "Swearengin", "Other", 4, 1,8 ],
              ["16 4 2018" ,"http://wvmetronews.com/2018/04/16/survey-shows-increasing-challenge-to-manchins-re-election/" ,"Survey shows increasing challenge to Manchin’s re-election" , 7, "Paula Jean", 6, "Swearengin", "Other", 4, 1,8 ],
              ["28 4 2018" ,"http://www.herald-dispatch.com/elections/manchin-swearengin-face-off-in-democrat-primary-for-us-senate/article_ee77d763-05ab-5053-a34f-f2c865a56587.html" ,"Manchin, Swearengin face off in Democrat primary for US Senate" , 7, "Paula Jean", 6, "Swearengin", "Other", 4, 1,8 ]]




freitas = [["16 3 2018","http://www.foxnews.com/opinion/2018/03/16/gop-legislator-calls-out-democratic-hate-speech-on-second-amendment.html","A GOP legislator calls out Democratic hate speech on the Second Amendment",9,"Nicholas",1,"Freitas","foxnews",2,2,6],
           ["11 4 2018","http://insider.foxnews.com/2018/04/11/corey-stewart-illegal-immigration-ms-13-election-against-tim-kaine-nick-freitas","GOP Kaine Opponent Rips VA Gov for Vetoing Bill Banning Sanctuary Cities",9,"Nicholas",2,"Freitas","foxnews",2,2,5],
           ["6 3 2018","http://insider.foxnews.com/2018/03/06/virginia-senate-candidate-nick-freitas-goes-viral-fiery-defense-gun-rights","'I Won't Accept a False Narrative': VA Lawmaker's Defense of Gun Rights Goes Viral",9,"Nicholas",3,"Freitas","foxnews",2,2,3],
           ["28 3 2018" ,"https://bearingdrift.com/2018/03/28/road-u-s-senate-freitas-jackson-stewart-square-off-uva/" ,"Road to the U.S. Senate: Freitas, Jackson, Stewart Square Off at UVA" ,9,"Nicholas",1,"Freitas","Other",4,2,8],
           ["23 4 2018" ,"https://www.washingtonpost.com/local/virginia-politics/freitas-raises-more-than-rivals-in-virginias-gop-primary-for-us-senate/2018/04/23/050fb456-4714-11e8-9072-f6d4bc32f223_story.html?noredirect=on&utm_term=.72ae85dfe993" ,"Freitas raises more than rivals in Virginia’s GOP primary for U.S. Senate" ,9,"Nicholas",1,"Freitas","Other",4,2,8],
           ["6 5 2018" ,"https://www.insidenova.com/news/politics/dozens-of-children-fatally-shot-in-virginia-each-year/article_7fdfee30-511e-11e8-9050-4b5d36ef1019.html" ,"Dozens of children fatally shot in Virginia each year",9,"Nicholas",1,"Freitas","Other",4,2,3],
           ["9 3 2018" ,"https://www.washingtonpost.com/local/virginia-politics/a-state-lawmaker-gives-corey-stewart-competition-for-gop-senate-nomination/2018/03/09/4be56714-222e-11e8-86f6-54bfff693d2b_story.html?utm_term=.048274918dc4" ,"A state lawmaker gives Corey Stewart competition for GOP Senate nomination" ,9,"Nicholas",1,"Freitas","Other",4,2,8],
           ["12 3 2018" ,"https://wtop.com/virginia/2018/03/va-del-freitas-speech-drew-attention-votes/" ,"Va. Del. Freitas’ speech drew attention — what about votes?" ,9,"Nicholas",1,"Freitas","Other",4,2,8],
           ["2 3 2018" ,"https://www.washingtonpost.com/local/virginia-politics/gun-control-issue-boils-over-in-virginia-house-after-fiery-speech-from-delegate/2018/03/02/991938d4-1e42-11e8-ae5a-16e60e4605f3_story.html?utm_term=.2e858199d921" ,"Gun-control issue boils over in Virginia House after fiery speech from delegate" ,9,"Nicholas",1,"Freitas","Other",4,2,3],
           ["9 12 2017" ,"https://www.washingtonpost.com/local/virginia-politics/del-nick-freitas-jumps-into-gop-field-to-challenge-sen-tim-kaine-in-2018/2017/12/09/af6f240a-dc6a-11e7-b859-fb0995360725_story.html?utm_term=.f12d4069b711" ,"Del. Nick Freitas jumps into GOP field to challenge Sen. Tim Kaine in 2018" ,9,"Nicholas",1,"Freitas","Other",4,2,8],
           ["27 11 2017" ,"http://www.richmond.com/news/virginia/government-politics/virginia-republicans-anticipating-state-del-nick-freitas-to-announce-run/article_ff75e381-eb0a-5483-b8ac-40cde38fec2d.html" ,"Virginia Republicans anticipating state Del. Nick Freitas to announce run for U.S. Senate" ,9,"Nicholas",1,"Freitas","Other",4,2,8],
           ["2 3 2018" ,"http://www.richmond.com/news/virginia/government-politics/general-assembly/sparking-chaos-on-house-floor-virginia-republican-suggests-abortion-industry/article_a974c162-ce20-5cc4-9d36-82e5140a1f3b.html" ,"Sparking chaos on House floor, Virginia Republican suggests 'abortion industry' and 'broken homes' contribute to mass shootings" ,9,"Nicholas",1,"Freitas","Other",4,2,3]]



jackson = [ ["28 3 2018" ,"https://bearingdrift.com/2018/03/28/road-u-s-senate-freitas-jackson-stewart-square-off-uva/" ,"Road to the U.S. Senate: Freitas, Jackson, Stewart Square Off at UVA" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["5 5 2018" ,"https://bearingdrift.com/2018/05/05/score-nick-freitas-e-w-jackson-rob-bell-infinity-war/" ,"The Score: Nick Freitas, E.W. Jackson, Rob Bell, Infinity War" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["19 4 2018" ,"https://bluevirginia.us/2018/04/what-do-nick-freitas-corey-stewart-and-ew-jackson-have-to-hide-from-virginia-gop-voters" ,"What Do Nick Freitas, Corey Stewart and EW Jackson Have to Hide from Virginia GOP Voters?" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["4 5 2018" ,"http://www.dailyprogress.com/news/virginia_politics/corey-stewart-accuses-gop-leaders-of-favoring-his-rival-in/article_556c8690-4fd4-11e8-b103-535adec1ef43.html" ,"Corey Stewart accuses GOP leaders of favoring his rival in Republican primary for US Senate" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["3 5 2018" ,"http://www.richmond.com/news/virginia/government-politics/corey-stewart-says-gop-establishment-wants-to-stop-him-from/article_2a732d2e-dfa4-5ed8-9f50-0c98609fc074.html" ,"Corey Stewart says GOP establishment wants to stop him from winning Senate nomination" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["4 5 2018" ,"http://www.citypages.com/news/duluths-confederate-yankee-corey-stewart-rides-again-in-virginia-senate-race/481653241" ,"Corey Stewart rides again in Virginia Senate race" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["1 5 2018" ,"https://pilotonline.com/news/government/politics/article_9ae48616-4a06-5f81-acf5-e1ee7501bbc5.html" ,"Virginia Republican Senate candidates repeatedly attack Obama, barely mention Kaine" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["5 12 2017" ,"https://www.washingtonpost.com/local/virginia-politics/ew-jackson-conservative-firebrand-preparing-us-senate-bid-in-virginia/2017/12/05/ddccfdc6-d9e1-11e7-b859-fb0995360725_story.html?utm_term=.f0baea99c11d" ,"E.W. Jackson, conservative firebrand, preparing U.S. Senate bid in Virginia" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["19 4 2018" ,"https://www.washingtonpost.com/local/virginia-politics/va-legislator-freitas-raises-nearly-350000-in-bid-to-take-on-tim-kaine/2018/04/19/dafec5ce-4373-11e8-bba2-0976a82b05a2_story.html?utm_term=.dcf1fecfe6c3" ,"Virginia legislator Freitas raises nearly $350,000 in bid to take on Tim Kaine" ,10,"E.W.",5,"Jackson","Other",4,2,8],
            ["1 5 2018" ,"https://bluevirginia.us/2018/05/ew-jackson-claims-video-it-was-not-europeans-who-came-up-with-racial-ideology-it-was-arab-muslims" ,"Video: EW Jackson Claims 'It was NOT Europeans who came up with racial ideology, it was Arab Muslims'" ,10,"E.W.",5,"Jackson","Other",4,2,6]]


waters = [["4 5 2018" ,"http://standardnewswire.com/news/430813910.html" ,"'Wall of Separation' Virginians Need Not Apply" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ],
          ["27 4 2018" ,"http://wtvr.com/2018/04/27/meet-the-candidates-matt-waters/" ,"Meet the Candidates: Matt Waters" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ],
          ["13 4 2018" ,"http://www.wsjm.com/2018/04/13/state-police-watching-out-for-texters/" ,"State Police Watching Out For Texters" , 13, "Matt", 6, "Waters", "Other", 4, 2,6 ],
          ["21 2 2018" ,"http://www.standardnewswire.com/news/9244213619.html" ,"Waters to Seek Nomination for US Senate" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ],
          ["11 3 2018" ,"https://bearingdrift.com/2018/03/11/virginia-libertarians-nominate-candidate-u-s-senate/" ,"Virginia Libertarians Nominate Candidate for U.S. Senate" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ],
          ["12 3 2018" ,"https://baconsrebellion.com/42374-2/" ,"Yes, Virginia, There Still Is a Libertarian Party" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ],
          ["28 3 2018" ,"https://bearingdrift.com/2018/03/28/road-u-s-senate-freitas-jackson-stewart-square-off-uva/" ,"Road to the U.S. Senate: Freitas, Jackson, Stewart Square Off at UVA" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ],
          ["22 3 2018" ,"https://wfirnews.com/news/59769" ,"Libertarian promises strong campaign to deliver less-government message" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ],
          ["5 4 2018" ,"http://www.newsadvance.com/news/local/kaine-stops-by-cvcc-as-part-of-campaign-kickoff/article_f408c554-393e-11e8-a7a4-b7a2f31af1f5.html" ,"Kaine stops by CVCC as part of campaign kickoff" , 13, "Matt", 6, "Waters", "Other", 4, 2,8 ]]

willis = [["3 5 2018","https://taskandpurpose.com/tom-willis-west-virginia-senate/","The Operator: A Green Beret Turned Senate Candidate Wages An ‘Ideological’ Battle On The Homefront",8,"Tom", 6, "Willis", "Other", 4, 1, 3],
          ["1 5 2018","http://www.williamsondailynews.com/news/six-republican-candidates-running-for-us-senate-in-west-virginia/article_4d6a2e62-af4e-53e9-a6af-42c2c415f31d.html","Six Republican candidates running for US Senate in West Virginia",8,"Tom", 6, "Willis", "Other", 4, 1, 3],
          ["7 5 2018","http://www.fayettetribune.com/news/willis-bid-for-u-s-senate-was-inevitable/article_2af39a04-522f-11e8-9a25-0b5d86d254c1.html","Willis’ bid for U.S. Senate was “inevitable”",8,"Tom", 6, "Willis", "Other", 4, 1, 1],
          ["16 4 2018","http://wvmetronews.com/2018/04/16/willis-momentum-growing-as-primary-draws-closer/","Willis: Momentum growing as primary draws closer",8,"Tom", 6, "Willis", "Other", 4, 1, 5],
          ["6 5 2018","http://www.register-herald.com/opinion/editorials/study-up-and-go-vote-options-exist/article_dc8e8e0b-9e7a-51fd-ad93-d4b51fc8d6be.html","Study up and go vote; options exist",8,"Tom", 6, "Willis", "Other", 4, 1, 7],
          ["18 4 2018","http://www.williamsondailynews.com/news/morrisey-willis-receive-endorsements/article_41809a1c-ef5a-5c01-86aa-75a37f422714.html","Morrisey, Willis receive endorsements",8,"Tom", 6, "Willis", "Other", 4, 1, 3],
          ["23 4 2018","http://wvah.com/news/election/raw-news-gop-senate-debate","Six GOP Senate candidates debate weeks away from primary election",8,"Tom", 6, "Willis", "Other", 4, 1, 8],
          ["22 4 2018","http://www.thedaonline.com/news/republican-u-s-senate-candidate-urges-wvu-students-to-take/article_3bed32ee-4662-11e8-9350-4789cbb47e21.html","Republican U.S. Senate candidate urges WVU students to take action",8,"Tom", 6, "Willis", "Other", 4, 1, 6],
          ["13 4 2018","http://www.journal-news.net/news/local-news/2018/04/republicans-honor-overington-allow-candidates-to-speak/","Republicans honor Overington, allow candidates to speak",8,"Tom", 6, "Willis", "Other", 4, 1, 6],
          ["12 4 2018","http://www.weirtondailytimes.com/news/local-news/2018/04/willis-sees-momentum-on-his-side/","Willis sees momentum on his side",8,"Tom", 6, "Willis", "Other", 4, 1, 6]]

all_articles = [copley,newbrough,swearengin, freitas, jackson,waters,willis]
names = ["copley", "newbrough", "swearengin", "freitas", "jackson", "waters","willis"]

def add_manual(output_file):
    all_rows = []
    original_data = pd.read_json("set_2_data/ALL_DATA.json")
    df_columns = list(original_data.columns.values)
    df_columns.append("issue")

    new_table = pd.DataFrame(columns = df_columns)
    '''
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

    for i in range(len(all_articles)):
        for j in range(len(all_articles[i])):
            file_name = "manual_articles/"+names[i] + "_" + str(j+1) + ".txt"
            with open(file_name) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            content = " ".join(content)
            all_articles[i][j].insert(0,content)
            new_table = new_table.append(pd.DataFrame([all_articles[i][j]],columns= df_columns), ignore_index=True)


    with open(output_file, 'w') as f:
        f.write(new_table.to_json(orient = "records"))
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
