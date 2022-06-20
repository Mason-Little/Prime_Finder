import time

how_many_numbers = int(input("How far do you want the code search for primes: "))

# Bad Way
start_time_one = time.time()
prime_number_list = []
for i in range(2, how_many_numbers):  # 1
    not_prime = 0
    for y in range(2, i):  # 2
        if i % y == 0:
            not_prime += 1  # 3
    if not_prime == 0:
        prime_number_list.append(i)
end_time_one = time.time()

# Good Way

start_time_two = time.time()
good_list = []
bad_list = set()

for i in range(2, how_many_numbers):  # 1
    if i not in bad_list:  # 2
        good_list.append(i)
        for y in range(i, how_many_numbers, i):  # 3
            bad_list.add(y)
end_time_two = time.time()

# Proof

print(f"Bad Way {end_time_one - start_time_one}")
print(f'Good Way {end_time_two - start_time_two}')
print(prime_number_list)
print(good_list)
