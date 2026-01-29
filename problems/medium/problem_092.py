"""
Problem 92: Weight Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_weight(val):
    #    return True

    if val > 10:
        return 'High'
    elif val > 5:
        return 'Medium'
    else:
        return 'Low' 
    
print(check_weight(20))