
import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("www.datos.gov.co", None)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(www.datos.gov.co,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.

# Variables
# Rain: s54a-sgyg

varname = "s54a-sgyg"
results = client.get(varname, limit=231619587)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Save into an external .csv file
results_df.to_csv('c:/temp/'+varname+'.csv', index=False)
