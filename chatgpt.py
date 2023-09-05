import numpy as np
from scipy.optimize import minimize

def calcola_posizione(positions, field_length, field_width):
    # Calculate the distance between all pairs of player positions
    
    # Calculate the total distance that needs to be minimized
    total_distance = np.sum(distances)
    
    # Calculate the penalty for players going out of bounds
    out_of_bounds_penalty = np.sum(np.maximum(positions - field_length / 2, 0))
    
    # Minimize the total distance with a penalty for out-of-bounds positions
    return total_distance + out_of_bounds_penalty

def optimize_player_positions(num_players, field_length, field_width):
    # Initial guess: randomly distribute players within the field
    initial_positions = np.random.rand(num_players, 2) * np.array([field_length, field_width])
    
    # Constraints: ensure that player positions stay within the field
    constraints = (
        {'type': 'ineq', 'fun': lambda x: x - [field_length / 2, field_width / 2]},
        {'type': 'ineq', 'fun': lambda x: [field_length / 2, field_width / 2] - x}
    )
    
    # Optimization
    result = minimize(evaluate_positions, initial_positions, args=(field_length, field_width),
                      constraints=constraints, method='COBYLA')
    
    return result.x

# Define field dimensions
field_length = 105.0  # meters
field_width = 68.0    # meters

# Number of players you want to position
num_players = 11

# Optimize player positions
optimal_positions = optimize_player_positions(num_players, field_length, field_width)

# Print the optimal player positions
print("Optimal Player Positions:")
for i, position in enumerate(optimal_positions):
    print(f"Player {i+1}: ({position[0]:.2f}, {position[1]:.2f}) meters")
