# 🌀 Blade Element Theory (BET) Propeller Performance Calculator

This repository contains a Python implementation of **Blade Element Theory (BET)** to estimate the aerodynamic performance of a propeller. The script computes total **thrust**, **torque**, and **power** by discretizing the blade into elements and iteratively solving for the **induced velocity**.

Designed to be simple yet functional, this tool is ideal for students, researchers, or engineers conducting early-stage propeller analysis.

---

## 📌 Key Features

- ✅ Interactive CLI for entering input parameters  
- ✅ Constant chord length and aerodynamic coefficients (Cl, Cd)  
- ✅ Induced velocity solved iteratively for accuracy  
- ✅ Computes total thrust (N), torque (Nm), and power (W)

---

## 📥 Input Parameters

Upon running the script, the user will be prompted to enter the following:

| Parameter | Description |
|----------|-------------|
| **R** | Propeller radius (meters) |
| **Nb** | Number of blades |
| **ω (omega)** | Rotational speed (rad/s) |
| **V_inf** | Freestream axial velocity (m/s) |
| **N** | Number of blade elements |
| **c** | Constant chord length (m) |
| **Cl** | Constant lift coefficient |
| **Cd** | Constant drag coefficient |

---

## 📤 Output Parameters

After computation, the script displays:

- Number of iterations for convergence  
- Final induced velocity (m/s)  
- Total thrust (N)  
- Total torque (Nm)  
- Total power (W)

---

## ⚙️ How It Works

1. The blade is divided into `N` radial elements, excluding the hub region.
2. The relative velocity and inflow angle for each element are calculated.
3. Lift and drag forces are computed using user-provided `Cl` and `Cd`.
4. Thrust and torque contributions from all elements are summed.
5. An iterative process solves for the induced velocity using momentum theory.
6. Total power is calculated using the final torque and angular speed.

---

## 🧮 Requirements

- Python 3.x  
- NumPy

Install dependencies using:

```bash
pip install numpy
