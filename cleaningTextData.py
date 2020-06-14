# Replace the + sign in front of a phone number with 00
# The dataframe is phones
phones['Phone number'] = phones['Phone number'].str.replace("+", "00")
# Replace dashes (-) in phone number column of phones with ""
phones['Phone number'] = phones['Phone number'].str.replace("-", "")
