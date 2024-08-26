def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
    for x in range(2,num):
        if num % x == 0:
            return False
    return True   
  
is_prime(10)