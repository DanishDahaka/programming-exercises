# https://www.hackerrank.com/challenges/angry-professor/problem

""" A Discrete Mathematics professor has a class of students. 
Frustrated with their lack of discipline, the professor decides 
to cancel class if fewer than some number of students are present 
when class starts. Arrival times go from on time (`arrivalTime <= 0`) 
to arrived late (`arrivalTime>0`).

Complete the angryProfessor function in the editor below. 
It must return YES if class is cancelled, or NO otherwise.
"""

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # keep only values which are smaller than 0
    no_on_time = len(list(filter(lambda x: x <= 0, a)))
    
    # return target string depending on condition
    if no_on_time < k:
        return 'YES'
    else:
        return 'NO'