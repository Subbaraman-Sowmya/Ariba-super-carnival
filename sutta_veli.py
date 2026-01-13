import json

def sutta_veli_cleaner(data):
    """
    Recursively cleans 'Dark Matter' (empty values/noise) from the data universe.
    """
    if isinstance(data, dict):
        # We filter the dictionary: Keep only if the 'Soul' (value) is not empty
        return {
            k: sutta_veli_cleaner(v) 
            for k, v in data.items() 
            if v not in [None, "", [], {}, "NULL", "DarkMatter"]
        }
    elif isinstance(data, list):
        # We filter the list: Keep only the 'Clear Water' elements
        return [
            sutta_veli_cleaner(item) 
            for item in data 
            if item not in [None, "", [], {}, "NULL", "DarkMatter"]
        ]
    else:
        # If it's a leaf node, we return it to the Light
        return data

# THE "DARK MATTER" UNIVERSE (A messy Ariba-style JSON)
messy_universe = {
    "SupplierID": "10293",
    "Status": "NULL",
    "Financials": {
        "Revenue": "500M",
        "Debt": "",
        "History": []
    },
    "Metadata": "DarkMatter",
    "Tags": ["Active", None, "Verified", {}]
}

# THE CHURNING (Execution)
cleaned_universe = sutta_veli_cleaner(messy_universe)

print("--- BEYOND DARKNESS: SUTTA VELI DATA ---")
print(json.dumps(cleaned_universe, indent=4))
