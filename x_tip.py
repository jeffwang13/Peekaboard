wb = 1
h = 0.6
thickness = 0.009525
rho_plexi = 1180
g = 9.81
m = 2 * wb * h * thickness * rho_plexi
G = m * g
Fpush = (G * (0.5 * wb)) / h

print(f"Can withstand {Fpush}N. Is {m}kg.")
