import os

dir = os.path.join(os.path.dirname(__file__), 'textcontent')
def importFile(textpath):
    return open(os.path.join(dir, textpath), 'r', encoding="utf-8").read()

content = [
#indexPL
importFile('indexPL.txt'),
#indexEN
importFile('indexEN.txt'),
#surveyPL
importFile('surveyPL.txt'),
#surveyEN
importFile('surveyEN.txt'),
#thanksPL
importFile('thanksPL.txt'),
#thanksEN
importFile('thanksEN.txt'),
#resultsPL
importFile('resultsPL.txt'),
#resultsEN
importFile('resultsEN.txt')
]
