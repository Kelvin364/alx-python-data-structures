### START FUNCTION
def add_vehicle(vehicles, new_vehicle_params):
    # Create a dictionary for the new vehicle using the new_vehicle_params tuple
    new_vehicle = {
        'model': new_vehicle_params[0],
        'colour': new_vehicle_params[1],
        'horsepower': new_vehicle_params[2],
        'fuel_capacity': new_vehicle_params[3]
    }
    # Append the new vehicle to the list of vehicles
    vehicles.append(new_vehicle)
    return vehicles
### END FUNCTION

# Test Cases
existing_vehicles = [
    {'model': 'TX-130', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60},
    {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}
]

new_vehicle = ('SX-750', 'White', 180, 80)
print(add_vehicle(existing_vehicles, new_vehicle)) 
# Expected output: [{'model': 'TX-130', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60}, 
#                   {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45},
#                   {'model': 'SX-750', 'colour': 'White', 'horsepower': 180, 'fuel_capacity': 80}]

new_vehicle_params = ('ZX-500', 'Blue', 130, 55)
print(add_vehicle(existing_vehicles, new_vehicle_params)) 
