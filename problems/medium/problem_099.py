"""
Problem 99: Time Searcher
Error Type: LOGICAL
Difficulty: Medium
"""

def check_time(val):
    #    return True

    if val > 10:
        return 'High'
   elif val > 5:
        return 'Medium'

else:
        return 'Low' 
    
print(check_time(20))