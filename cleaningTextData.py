# Replace the + sign in front of a phone number with 00
# The dataframe is phones
phones['Phone number'] = phones['Phone number'].str.replace("+", "00")
# Replace dashes (-) in phone number column of phones with ""
phones['Phone number'] = phones['Phone number'].str.replace("-", "")

# Clean honorifics
# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.", "")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.", "")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss", "")
# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.", "")
# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])

# Isolate temperatures in farenheit,

temp_fahrenheit = temperatures.loc[temperatures['Temperature']
                                   > 40, 'Temperature']

#  When you want to convert dates in a column into a single format

birthdays['Birthday'] = pd.to_datetime[birthdays['Birthday'], infer_datetime_format = True, errors = 'coerce']
# OR
birthdays['Birthday'] = birthdays['Birthday'].dt.strftime("%d-%m-%Y")

# Treatment of missing data
missing = banking[banking['acct_no'].isna()]
complete = banking[~banking['acct_no'].isna()]
