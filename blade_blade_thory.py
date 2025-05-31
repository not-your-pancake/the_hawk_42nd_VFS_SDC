import numpy as np 

  
# Predefine Parameters:  

rho = 1.225  # air density (kg/m^3) 

  

#  Input Parameters 

print("Enter the following inputs for Blade Element Theory calculation:") 

R = float(input("1. Propeller radius (m): ")) 

Nb = int(input("2. Number of blades: ")) 

omega = float(input("3. Rotational speed (rad/s): ")) 

V_inf = float(input("4. Axial freestream velocity (m/s): ")) 

N = int(input("5. Number of blade elements: ")) 

c_const = float(input("6. Constant chord length (m): ")) 

Cl = float(input("7. Constant lift coefficient Cl: ")) 

Cd = float(input("8. Constant drag coefficient Cd: ")) 

  

#  Geometry & Distribution  

r_0 = 0.2 * R  # hub cutoff 

r = np.linspace(r_0, R, N) 

dr = (R - r_0) / (N - 1) 

  

# Initialize Totals  

T_total = 0.0 

Q_total = 0.0 

v_induced = 0.1  # initial guess 

  

#  Iterative induced velocity loop  

max_iter = 100 

tolerance = 1e-4 

  

for iteration in range(max_iter): 

T_total = 0.0 

Q_total = 0.0 

  
for i in range(N): 
ri = r[i] 
c = c_const 

  

Vt = omega * ri 
Va = V_inf + v_induced 

Vrel = np.sqrt(Va**2 + Vt**2) 

phi = np.arctan2(Va, Vt) 

  

  

# Use user-supplied Cl and Cd directly 

dL = 0.5 * rho * Vrel**2 * c * Cl * dr 

dD = 0.5 * rho * Vrel**2 * c * Cd * dr 

  

dT = dL * np.cos(phi) - dD * np.sin(phi) 

dQ = (dL * np.sin(phi) + dD * np.cos(phi)) * ri 

  

T_total += dT 

Q_total += dQ 

  

T_total *= Nb 

Q_total *= Nb 

  

# Updating induced velocity 

A = np.pi * R**2 

v_new = T_total / (2 * rho * A * (V_inf + v_induced)) 

  

if abs(v_new - v_induced) < tolerance: 

break 

  

v_induced = v_new 

  

P_total = Q_total * omega 

  

#  Output  

print("\n=== Blade Element Theory Results (Fixed Cl, Cd) ===") 

print(f"Iterations for induced velocity: {iteration + 1}") 

print(f"Induced velocity: {v_induced:.3f} m/s") 

print(f"Total Thrust: {T_total:.2f} N") 

print(f"Total Torque: {Q_total:.2f} Nm") 

print(f"Total Power: {P_total:.2f} W") 

        

 
