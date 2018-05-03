with open("states.csv", "r" ) as source:
    for aLine in source:
      aLine=aLine.strip()
      aLine=aLine.split(',')
      print(aLine)
      for word1, word2, word3 in aLine:
        print(word1)
        print(word2)
        print(word3)
      '''
        for namef, URL_logof, primaries_datef in aLine.split(','):
          print(namef)
          '''