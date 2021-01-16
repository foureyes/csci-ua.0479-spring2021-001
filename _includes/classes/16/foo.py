def is_prime(n):
        for i in range(2, n+ 1):
                # check if factor
                if n % i == 0:
                        return False
                return True


        # return True
"""
our n = 9
# i
=======
1 2

"""
2 * recursive_power(2, 3)
    2 * recurisve_power(2, 2)
        2 * recursive_power(2, 1)
            -> 0
        
