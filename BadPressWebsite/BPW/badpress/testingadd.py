with open("states.csv", "r" ) as source:
    for aLine in source:
        for namef, URL_logof, primaries_datef in aLine:
          print(namef)