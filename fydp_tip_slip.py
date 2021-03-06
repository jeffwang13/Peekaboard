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
w = 0.72 # Width of board (M)
hb = 0.1 # Height of base (M)
wb = 0.6 # Width of base (M)
t = 0.0191 # Thickness of board (M)

mboard = (h * w * t) * rho_plexi
print(mboard)
Gboard = mboard * g
print(Gboard)

mbase = ((Fpush * hb) - (Gboard * 0.5 * wb)) / (0.5 * wb * g)

print(f"The mass of the base needs to be at least {mbase}kg to prevent tipping.")

mfoot = mbase / 2

# if (Fpush > mu_s * Gboard):
# 	print(f"{(Fpush)} > {(mu_s * Gboard)}")
# 	print("The board will slip.")
