from data_wrangler import DataManager
import csv
import os
from typing import List


manager = DataManager()

data = manager.csv_json(0)



manager.write_json_csv(list, ['name', 'description', 'index'])