import csv
import json
import os

# Manages the retrieval and storage of CSV data
class DataManager:
    CSVFiles = []

    # Stores all of the csv file names
    def __init__(self):
        for filename in os.listdir("CSV"):
            self.CSVFiles.append("CSV/" + filename)

    # returns the data of a chosen csv (by index) as json
    def csv_json(self, index: int = 0):
        file = self.CSVFiles[index]
        data = {}

        # Reads in data from csv file, stores it in data dictionary
        # JSON and Python dictionaries are functionally the same
        with open(file) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for row in csvReader:
                id = row['sequence']
                data[id] = row
        return data

    # Returns the data of all the local csv's as json
    def csv_json_all(self):
        data = {}
        for file in self.CSVFiles:
            currData = {}
            with open(file) as csvFile:
                csvReader = csv.DictReader(csvFile)
                for row in csvReader:
                    id = row['sequence']
                    currData[id] = row
                data[file] = currData
        return data

    # Writes the given json data to a csv file
    def write_json_csv(self, json_data, data_columns):
        with open('new_example.csv', 'w') as file_output:
            file_output.write("{0},{1},{2}\n".format(data_columns[0], data_columns[1], data_columns[2]))
            for row in json_data:
                file_output.write("{0},{1},{2}\n".format(row.name, row.description, row.index))

                
