# Here we turn our results.json to a csv through pandas
# This is in order to view and evaluate the data better on a human level.
# Origin File = results.json, Destination File = master_courses.csv
# Author: Emmett Lawlor

import pandas as pd
from json import load

def definedf(dataset={}):
    aggkeys = []
    
    for course in dataset:
        keys = list(course.keys())
        aggkeys+=(keys)
    
    dataset_keys = set(aggkeys)
    columns = list(dataset_keys)
    df = pd.DataFrame({}, columns=columns)
    
    return df

def sortResults(read_from: str, destination_file: str):
    with open(read_from, 'r') as coursesjson:
        courses = load(coursesjson)
    
    masterdf = definedf(dataset=courses)
    
    for course in courses:
        df = pd.json_normalize(course)
        masterdf = masterdf.append(df)
    
    masterdf.to_csv(destination_file, encoding='utf8', index=0)
