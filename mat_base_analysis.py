'''
Sources for push strength:

https://www.tandfonline.com/doi/pdf/10.1080/10803548.2004.11076594
https://www.humanics-es.com/strength.pdf
https://www.canada.ca/en/health-canada/services/consumer-product-safety/reports-publications/industry-professionals/industry-guide-safety-requirements-children-toys-related-products-summary.html
'''

# Constants
g = 9.81 # (N/kg)
Fpush = 130.96 # (2-5 year old push strength) * 2 for a factor of safety (N)
mu_s = 0.62 # Wood on Concrete Coefficient of Static Friction
rho_plexi = 1180 # Density of plexiglass (kg/m^3)

# User changed variables
h = 0.6096 # Height of board (M)
w = 0.6096 # Width of board (M)
hb = 0.02 # Height of base (M)
wb = 0.962 # Width of base (M)
t = 0.013716 # Thickness of board (M)
db = 0.1 # Distance between bottom of board and bottom of base (M)
kid_mass = 17.5 # Mass of a 5 year old (kg) https://wicworks.fns.usda.gov/sites/default/files/media/document/CDC%20WIC%20Growth%20Charts%202-5yrsBoys.pdf

# Calculated variables
mboard = (h * w * t) * rho_plexi # mass of board (kg)
Gboard = mboard * g # gravitational force of board (N)
Gkid = kid_mass * g # gravitational force of kid on mat (N)

# Base mass calculations
mbase = ((Fpush * h) + (Fpush * hb) - (Gboard * 0.5 * wb) - (Gkid * 0.5 * wb)) / (0.5 * wb * g)

# Slipping calculation
# if (Fpush > mu_s * (Gboard + mbase * g + Gkid)):
# 	print(f"{Fpush} > {mu_s * (Gboard + mbase * g + Gkid)}")
# 	print(f"The board will slip. Base needs to be {Fpush - mu_s * (Gboard + mbase * g + Gkid)}kg heavier.")
if True:
	print(f"The mass of the base needs to be at least {mbase}kg to prevent tipping.")

	# Base dimension calculations
	densities = [("Iron", 7860), ("Water", 997), ("Plexiglass", rho_plexi)] # Densities (kg/m^3)

	for material in densities:
		volume_needed = (mbase / 2) / material[1]
		xz_slot_area = t * (hb - db)
		base_length = volume_needed / (wb * hb - xz_slot_area)
		print(f"The dimensions for a {material[0]} base are:\nWidth: {wb}, Length: {base_length}, Height: {hb}.")

