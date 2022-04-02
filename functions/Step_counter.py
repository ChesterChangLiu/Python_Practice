def feet_to_steps(user_feet):
    steps = user_feet/2.5
    return int(steps) # Use floating-point arithmetic to perform the conversion.
    
if __name__ == '__main__':
    user_input = float(input())
    print(feet_to_steps(user_input))
