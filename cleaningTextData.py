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
