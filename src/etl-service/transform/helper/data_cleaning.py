from fuzzywuzzy import process
import re

def get_best_match(query, text_List):
    best_match, score = process.extractOne(query, text_List)
    return best_match, score

def remove_anomalies(data_list):
    anomalies = ["Ad", "Bisa COD", "PreOrder"]
    regex_anomalies = [r"^(Cashback|Diskon|Disc)? [\d.,]+(ribu|rb|%)?$" , r"\+\d+ lain$"]

    return [
        data for data in data_list
        if data not in anomalies and not any(re.match(regex, data, re.IGNORECASE) for regex in regex_anomalies)
        ]
    
def percentage_to_float(percentage_str):
    return float(percentage_str.strip('%')) / 100