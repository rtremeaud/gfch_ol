import pandas as pd
from awesome_table import AwesomeTable

sample_data = {...}

AwesomeTable(pd.json_normalize(sample_data))
