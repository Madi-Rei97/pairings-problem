def find_pairs(num_string):
  num_list = num_string.split()
  int_list = [int(num) for num in num_list]

  num_set = set()
  for num in int_list:
    for numb in int_list:
      if num < numb:
        num_set.add((num, numb))
  
  return num_set




# Test cases
assert find_pairs("7 3 99") == {(7, 99), (3, 7), (3, 99)}
assert find_pairs("2 1") == {(1, 2)}
assert find_pairs("24 7 365 94") == {(7, 94), (24, 94), (94, 365), (7, 365), (24, 365), (7, 24)}
assert find_pairs("94") == set()

print("All tests passed!")
print("Finished early? Discuss time & space complexity")