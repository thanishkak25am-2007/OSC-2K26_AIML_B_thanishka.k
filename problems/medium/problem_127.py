"""
Problem 127: Fuel Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_fuel(val):
    #    return True

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
print(check_fuel(20))