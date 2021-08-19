import os

# change of passed arguments here
def serviceLane(cases, width):
        
        # get the minimum of each sliced width element
        return [min(width[cases[i][0]:cases[i][1]+1]) for i in range(len(cases))]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    # had to change arguments passed in, given code took n
    result = serviceLane(cases, width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()