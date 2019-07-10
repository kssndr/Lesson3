vector = []
a = input("input vector = ")
vector = [int(s) for s in a.split(",")]
len_vector = 0
for i in vector:
    len_vector = len_vector + i**2
len_vector = len_vector**0.5
print(f"the length of the vector{vector} is  {len_vector:.3f}")

