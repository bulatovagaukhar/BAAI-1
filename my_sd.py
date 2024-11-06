
# Gaukhar
# 2024/11/06
# stardard deviation


import statistics
import math

def my_sd (input):
    print (f'input: {input}')
    length = len(input)
    sum = 0
    output = 0
    mean = statistics.mean(input)
    print (f'Mean: {mean}')
    for x in input:
        sum+= (int(x) - mean)**2
    sum = sum / length
    output = math.sqrt (sum)
    return output

answer = my_sd([1,2,3])
answer = round (answer, 2S)
print(f'Answer: {answer}')