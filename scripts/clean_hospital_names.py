from pyspark.sql.functions import regexp_replace, col, trim

# Define a function to clean hospital names
def clean_hospital_name(hospital_name):
    # List of common suffixes to remove
    suffixes = ['LLC', 'Ltd', 'PLC', 'Inc', 'Group', 'and']
    # Remove suffixes
    for suffix in suffixes:
        hospital_name = regexp_replace(hospital_name, r'\b' + suffix + r'\b', '')
    # Remove extra spaces and trim
    hospital_name = trim(regexp_replace(hospital_name, r'\s+', ' '))
    return hospital_name
