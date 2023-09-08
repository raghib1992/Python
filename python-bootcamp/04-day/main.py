import random

print(random.randint(3,13))

## Head tails game
rand_num = random.randint(0,1)

if rand_num == 0:
    print("Head")
else:
    print("Tail")
