# GEMSEC Web API Demo
### Jackson Frank, Winter 2020

The purpose of this project is to build a small demonstration of a working web API. This service uses the FastAPI framework and has a few endpoints for data downloading and uploading capabilities:
+ "/" (GET)
  + The welcome page of the API, will return a default message.
+ "/csvfiles" (GET)
  + Query: fileIndex (int)
  + Will return the data from the CSV given from the query parameter. If a CSV file doesn't exist at this index or no query parameter is given, this will return the data of all of the CSV stored CSV files.
+ "/uploaddata" (POST)
  + Body: JSON formatted data
  + Will recieve data from the body, and save it as a new CSV file.
