from random import randint

N = 8
p = 0.5

slots = 1000000
successes = 0
actual = 0

for numslots in range(slots):
    sum = 0
    for node in range(N):
        if randint(0,1) == 1:
            sum +=1
    if sum == 1:
        successes +=1
        actual = successes / (numslots + 1)

theoretical = (N*p*(1-p)**(N-1))

print("Theoretical = ", theoretical)
print("Actual = ", actual)

