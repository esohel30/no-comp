"""
An earthling's weight on Mars is 37.8% of their weight on earth.
Write a Python program that prompts the user (an earthling) to
enter their weight on earth and prints their calculated weight on Mars. 
"""

# earth weight * 0.378 = mars weight 

mars_constant = 0.378 

earth_weight_str = input("Enter your weight on Earth: ")

earth_weight_num = float(earth_weight_str)

mars_weight = earth_weight_num * mars_constant

print(mars_weight)
