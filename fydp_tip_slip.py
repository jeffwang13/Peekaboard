'''
Sources for push strength:

https://www.tandfonline.com/doi/pdf/10.1080/10803548.2004.11076594
https://www.humanics-es.com/strength.pdf
https://www.canada.ca/en/health-canada/services/consumer-product-safety/reports-publications/industry-professionals/industry-guide-safety-requirements-children-toys-related-products-summary.html
'''

h = 0.7 # Metres (M)
wb = 0.7 # Metres (M)
g = 9.81 # N/kg
m = 10 # kg
Fpush = 44.5 # Newtons (N)
mu_s = 0.62 # Wood on Concrete Coefficient of Static Friction

G = m * g

if (Fpush * h) > (G * 0.5 * wb):
	print(f"{(Fpush * h)} > {(G * 0.5 * wb)}")
	print("The board will tip.")
elif (Fpush > mu_s * G):
	print(f"{(Fpush)} > {(mu_s * G)}")
	print("The board will slip.")
else:
	print("The board will not tip nor slip.")
