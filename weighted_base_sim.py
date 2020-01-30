'''
Sources for push strength:

https://www.tandfonline.com/doi/pdf/10.1080/10803548.2004.11076594
https://www.humanics-es.com/strength.pdf
https://www.canada.ca/en/health-canada/services/consumer-product-safety/reports-publications/industry-professionals/industry-guide-safety-requirements-children-toys-related-products-summary.html
'''

# Constants
g = 9.81 # (N/kg)
Fpush = 149.06 # (2-5 year old push strength) * 2 for a factor of safety (N)
mu_s = 0.62 # Wood on Concrete Coefficient of Static Friction
rho_plexi = 1180 # Density of plexiglass (kg/m^3)

# User changed variables
h = 0.6 # Height of board (M)
w = 0.6 # Width of board (M)
hb = 0.15 # Height of base (M)
wb = 0.6 # Width of base (M)
t = 0.0191 # Thickness of board (M)
db = 0.1 # Distance between bottom of board and bottom of base (M)

# Calculated variables
mboard = (h * w * t) * rho_plexi # mass of board (kg)
Gboard = mboard * g # gravitational force of board (N)

# Base mass calculations
mbase = ((Fpush * h) + (Fpush * hb) - (Gboard * 0.5 * wb)) / (0.5 * wb * g)

# Slipping calculation
if (Fpush > mu_s * (Gboard + mbase * g)):
	print("The board will slip. Revisit design.")
else:
	print(f"The mass of the base needs to be at least {mbase}kg to prevent tipping.")

	# Base dimension calculations
	densities = [("Iron", 7860), ("Water", 997), ("Plexiglass", rho_plexi)] # Densities (kg/m^3)

	for material in densities:
		volume_needed = (mbase / 2) / material[1]
		xz_slot_area = t * (hb - db)
		base_length = volume_needed / (wb * hb - xz_slot_area)
		print(f"The dimensions for a {material[0]} base are:\nWidth: {wb}, Length: {base_length}, Height: {hb}.")

