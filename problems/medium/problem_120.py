"""
Problem 120: Speed Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_speed(val):
    #    return True

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
print(check_speed(20))