import requests
import csv
from xml.dom.minidom import parseString
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]        



# if I want to store the xml in a file. You can comment this out later
## with open("trainxml.xml","w") as xmlfp:
##    doc.writexml(xmlfp)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
    traincode = traincodenode.firstChild.nodeValue.strip()
    #print (traincode)

objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
for objTrainPositionsNode in objTrainPositionsNodes:
    trainLatitudeNode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    trainLatitude = trainLatitudeNode.firstChild.nodeValue.strip()
    #print(trainLatitude)


# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-r# adding the newline= '' parameter
with open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    dataList = []
    for retrieveTag in retrieveTags:
        datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
        dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
# Specify the CSV file name
csv_file_name = "train_codes.csv"

# Write the dataList to a CSV file
with open(csv_file_name, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Write the data from dataList to the CSV file
    for traincode in dataList:
        writer.writerow([traincode])

print(f"Data has been written to {csv_file_name}")