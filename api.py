# -------------------HOW TO RUN----------------------------


# 1. In "!----- EDIT ME --------! (1)", edit the file so it reads the desired decade. (billboard_[DECADE]s.csv)
# 2. Right click in the Explorer panel to the left and click 'New File'. C
# 3. Create an empty CSV file titled "billboard_[DECADE]_countries.csv".
# 4. # In !----- EDIT ME --------! (2), edit the string to be the name of the CSV file you just made "billboard_[DECADE]_countries.csv".
# 5. Run the program and leave it for like 15-20 minutes. The command prompt will appear again when its done running.
# 6. Open the CSV file you made and manually add a header up at the top called 'country'.
# 7. Merge "billboard_[DECADE]_countries.cs" with "billboard_[DECADE]s.csv". You can either copy and paste it or merge it however. 
# 8. Repeat for other decades.

# You only have to edit the lines mentioned in steps 1 and 4! 

import time
import requests 
import csv 
import pandas as pd
import json
# from urllib import parse

# !----- EDIT ME --------! (1)
billboard_20s = pd.read_csv('billboard_20s.csv')

# extract artist column 
column_name = "artist"
artist_20s = billboard_20s[column_name]

# clean columns 
# 1. ALL LOWER CASE 2. REMOVE PUNCTUATIONS AND ANYTHING THAT ISNT A NUMBER 3. INSERT UNDERSCORES IN WHITESPACES 

artist_20s_lc = artist_20s.str.lower()

pattern = r'[^\w\s]'
artist_20s_np = artist_20s_lc.replace(pattern, '', regex=True)

artist_20s_nws = artist_20s_np.str.replace(' ', '_')

# concatenate with individual values from the column
url = "https://musicbrainz.org/ws/2/artist/?query="
user_agent = "jambothecat/1.2.0 ( https://jambothecat.github.io )"
header = {'User-Agent': user_agent, 'Accept': 'application/json'}

# !----- EDIT ME --------! (2)
file_path = "billboard_20s_countries.csv"


for row in artist_20s_nws:
    response = requests.get(url + row, headers=header)
    response.raise_for_status()

    if response.ok: 
        #artist_json = response.json()
        #final = artist_json['country']

        data = response.json()
        
        attribute = data['count']

        # checking if anything even exists or is returned from the query
        if attribute > 0:

            artist_country = data['artists'][0]

            attribute_name = "country"
            attribute_value = artist_country.get(attribute_name)

            if attribute_value is not None:
                with open(file_path, 'a', newline='') as file:
                    # Create a CSV writer object
                    writer = csv.writer(file)

                    # Write the data rows
                    writer.writerow([attribute_value])
                    time.sleep(1)
                # save to csv file
            elif attribute_value is None:
                with open(file_path, 'a', newline='') as file:
                    # Create a CSV writer object
                    writer = csv.writer(file)

                    # Write the data rows
                    writer.writerow(['XX'])
                    time.sleep(1)

        else:
            with open(file_path, 'a', newline='') as file:
                # Create a CSV writer object
                writer = csv.writer(file)

                # Write the data rows
                writer.writerow(['XX'])
                time.sleep(1)

    else:
        with open(file_path, 'a', newline='') as file:
            # Create a CSV writer object
            writer = csv.writer(file)

            # Write the data rows
            writer.writerow(['XX'])

            time.sleep(1)


# debug time 
"""
response = requests.get(url + "bts", headers=header)
response_json = response.json()
response_artist = response_json['artists'][0]

attribute_name = "country"
attribute_value = response_artist.get(attribute_name)

print(attribute_value)
"""


# ---Program Outline---  
# 1. make api call
# 2. import csv file
# 3. use individual artist columns 
# 4. save all individual information (country code) to the file 
# 5. merge column with final csv file 
# 6. merge 
# 7. repeat with other decades 

