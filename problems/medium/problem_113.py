"""
Problem 113: Steps Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_steps(val):
    #    return True

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
print(check_steps(20))