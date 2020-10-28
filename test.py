from timeit import timeit

# Test 1
test = """
my_list = []
for i in range(50):
    my_list.append(0)
"""
timeit(test)
