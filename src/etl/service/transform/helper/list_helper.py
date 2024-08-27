import re

def remove_anomalies(text_list):
    anomalies = ["Bisa COD", "PreOrder"]
    regex_anomalies = [r"^(Cashback|Diskon|Disc)? [\d.,]+(ribu|rb|%)?$" , r"\+\d+ lain"]
    
    return [
        data for data in text_list
        if data not in anomalies and not any(re.match(regex, data, re.IGNORECASE) for regex in regex_anomalies)
        ]
    



