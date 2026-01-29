"""
Problem 106: Calories Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_calories(val):
    #    return True

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
print(check_calories(20))