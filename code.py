import numpy as np

def membership_functions(x):
    cold = max(min((20 - x) / 5, 1), 0)
    warm = max(min((x - 20) / 5, 1), 0)
    hot = max(min((x - 25) / 5, 1), 0)
    return cold, warm, hot

def fuzzy_controller(temperature):
    cold, warm, hot = membership_functions(temperature)
    power = 0.5 * cold + 0.75 * warm + 1.0 * hot
    return power

def simulate_temperature_control(current_temperature, desired_temperature):
    error = desired_temperature - current_temperature
    power = fuzzy_controller(current_temperature)
    return power * error

current_temp = 22
desired_temp = 23

power_output = simulate_temperature_control(current_temp, desired_temp)
print("Power output:", power_output)
