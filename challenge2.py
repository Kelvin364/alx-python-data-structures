### START FUNCTION
def plant_row(field, row_to_plant):
    # Replace the specified row with 1's to indicate planting
    field[row_to_plant] = [1] * len(field[row_to_plant])
    return field
### END FUNCTION

# Test Cases
print(plant_row([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], 1)) 


print(plant_row([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], 0)) 

