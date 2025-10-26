
# 🎈 Ball Levitation PID Simulation

This project is a **PID-controlled DC motor ball levitation simulation** built entirely in Python.  
It visually demonstrates how a PID controller stabilizes a lightweight ball inside a vertical cylinder by adjusting the motor speed (simulating airflow).  

The system **requires no Arduino or physical hardware** — everything is simulated in real-time using `pygame`.

---

## 🧠 Concept Overview

In a real physical setup, a DC motor (fan) blows air upward through a transparent tube, keeping a ping-pong ball floating at a desired height.  
A sensor (e.g., camera or ultrasonic) measures the ball's height, and a **PID controller** adjusts the fan speed to maintain the ball at the target position.

In this **software-only version**, the entire system (motor, ball, and air flow) is simulated mathematically.

---

## ✨ Features

- 🎯 Real-time PID control simulation  
- 🧩 Adjustable target height using keyboard (`↑` and `↓`)  
- ⚙️ Realistic physics model (gravity, air thrust, inertia)  
- 🎨 Visual animation using `pygame`  
- 📊 Live display of error, motor speed, and ball position  

---

## 🧪 How It Works

The simulation models the forces acting on the ball:

\[
F_{up} = k \times \text{motor\_speed}, \quad F_{down} = m \times g
\]

The PID controller calculates the motor speed based on the error:

\[
\text{error} = \text{target\_height} - \text{current\_height}
\]

\[
\text{motor\_speed} = K_p \times \text{error} + K_i \times \text{integral} + K_d \times \text{derivative}
\]

The controller adjusts the airflow (motor speed) so the ball stays near the target height smoothly without oscillations.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Tohidnamdari/ball-levitation-sim
cd ball-levitation-sim
````

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Simulation

Run the main Python script:

```bash
python ball_pid_sim.py
```

Use the **arrow keys** to change the target height:

* `↑` → Increase target height
* `↓` → Decrease target height

The simulation window will display:

* Current height (pixels)
* Target height
* Motor speed
* PID error value

---

## ⚙️ Configuration

You can modify PID constants and physics parameters at the top of the code:

```python
Kp = 2.0     # Proportional gain
Ki = 0.05    # Integral gain
Kd = 1.0     # Derivative gain

m = 0.05     # Ball mass (kg)
k = 0.002    # Airflow coefficient
```

Tuning these values affects the system’s stability and response time.

---

## 📂 Project Structure

```
ball-levitation-sim/
│
├── ball_pid_sim.py         # Main simulation code
├── requirements.txt        # Required dependencies
└── README.md               # Project documentation
```

---

## 📦 Requirements

Make sure you install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 Future Improvements

* Add graphical sliders to tune `Kp`, `Ki`, and `Kd` in real-time
* Plot live PID performance charts (e.g., using `matplotlib`)
* Add random sensor noise for realism
* Save simulation data for analysis



## 👨‍💻 Author

Developed for **educational and control systems learning purposes** 🎓







