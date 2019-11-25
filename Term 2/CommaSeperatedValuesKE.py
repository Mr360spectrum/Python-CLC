# Karter Ence
# Comma-Seperated Values
# 11/24/19

address = input("Please enter an address in CSV format: ")
 
# split address using comma
fields = address.split(",")
 
# for loop iterating over each field index
for i in range(0, len(fields)):
    # read the list element at index "i", strip whitespace from it, and store in field variable
    field = fields.pop(i)
    field = field.strip()
    # store the field value back in the list at index "i"
    fields.insert(i, field)
 
# Print the final, clean list of fields
print(fields)