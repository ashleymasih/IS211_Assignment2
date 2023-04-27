import urllib.request
import csv
import datetime
import logging
import argparse

def downloadData(url):
    csvData = urllib.request.urlopen(url)
    return csvData

def processData(data):
    dictonary = {}
    data = data.read().decode('utf-8')
    logging.basicConfig(filename='assignment2.log', filemode='w', level=logging.ERROR)

    count = 0
    data_items = data.splitlines()
    for line in data_items[1:]:
        data_pieces = line
        data_pieces = data_pieces.split(',')
        count = count + 1
        try:
            dictonary[data_pieces[0]] = (data_pieces[1]), datetime.datetime.strptime((data_pieces[2]), '%d/%m/%Y')
        except ValueError:
            logging.error("Error processing line #: " + str(count) + " for ID #: " + str(data_pieces[0]))
    return dictonary

def displayPerson(id, personData):
    try:
        id = input("ID:")
        print("Person #" + id + " is " + personData[id][0] + " with a birthday of " + personData[id][1].strftime('%d/%m/%Y'))
    except:
        print("No user ID found")


arg = argparse.ArgumentParser()
arg.add_argument('--url',type=str, help="enter the website url you use here")
urlarg = arg.parse_args()

if urlarg.url:
    urlDownload = downloadData(urlarg.url)
    urlData = (processData(urlDownload))
    displayPerson(1, urlData)
else:
    print("No url was given, please use --url ")
    





