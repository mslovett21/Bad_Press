
from models import State

with open("states.csv", "r" ) as source:
    for aLine in source:
        for namef, URL_logof, primaries_datef in aLine:
            object= State.objects.create( name=namef, primaries_date=primaries_datef, URL_logo=URL_logof )
            object.save()
