import streamlit as st
import json
import pandas as pd

filepath = './data/courses-full.json'

with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)
    pd_courses = pd.DataFrame.from_dict(dict_of_courses)
    pd_courses = pd_courses.transpose()
    pd_courses.index = range(len(pd_courses))
    

pd_courses