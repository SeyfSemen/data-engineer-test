from distutils.log import error
import pandas as pd
import json

""" Om het JSON bestand tot bruikbaar formaat te maken, moet je eerst het JSON bestand normaliseren.
    Wat hiervan het doel is, is dat alle informatie uit het JSON bestand bruikbaar wordt gemaakt. Je hebt namelijk datavelden die zich bevinden 
    in een array of in een JSON object. Door de functie json_normalize kan je ervoor zorgen dat datavelden worden genormaliseerd zodat ze uit de 
    array worden gehaald en netjes onder elkaar worden geplaatst.
 """
with open(r'./eenvandaag_page_metrics.json') as data_file:    
    d= json.load(data_file) 

""" de parameter errors, wordt gevuld met ignore. Dit betekent dat alles wat een null waarde heeft alsnog wordt meegenomen. 
    Op heel veel plekken waren waardes niet ingevuld.
    de parameter record_prefix wordt gevuld met '.'. Hiermee zorg je ervoor dat alles dat uit de array 'values' komt, wordt gescheiden met een '.'
    value.Search is een goed voorbeeld uit het CSV bestand. 
"""
flatten_data = pd.json_normalize(d['data'], "values",[["period"],["name"],"value","end_time"], errors='ignore',record_prefix='.')

# Met pandas kan je de dataframe omzetten naar een csv
csv = flatten_data.to_csv(r'./eenvandaag_page.csv')

