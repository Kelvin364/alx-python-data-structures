### START FUNCTION
def create_tractor(model, colour, horsepower, fuel_capacity):
    # Create a dictionary with the given attributes
    tractor = {
        'model': model,
        'colour': colour,
        'horsepower': horsepower,
        'fuel_capacity': fuel_capacity
    }
    return tractor

# Test Cases
print(create_tractor('TX-1300', 'Green', 150, 60)) 
# Expected output: {'model': 'TX-1300', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60}

print(create_tractor('RX-850', 'Red', 120, 45)) 
# Expected output: {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}
