a = {1,2,3,4,5}
b = {4,5,6,7,8}
# Union of sets a and b
union_set = a.union(b)
print("Union of sets a and b:", union_set)      

# Intersection of sets a and b
intersection_set = a.intersection(b)
print("Intersection of sets a and b:", intersection_set)

# Difference of sets a and b
difference_set = a.difference(b)
print("Difference of sets a and b (a - b):", difference_set)

# Symmetric difference of sets a and b
symmetric_difference_set = a.symmetric_difference(b)
print("Symmetric difference of sets a and b:", symmetric_difference_set)

# Subset and Superset checks
is_subset = a.issubset(b)
print("Is set a a subset of set b?", is_subset)
is_superset = a.issuperset(b)
print("Is set a a superset of set b?", is_superset)     

# Disjoint check
is_disjoint = a.isdisjoint(b)
print("Are sets a and b disjoint?", is_disjoint)    

# Clear all elements from set a
a.clear()
print(f"Set a after clearing all elements: {a}")  

# Add elements to set a
a.add(10)
a.add(20)
print("Set a after adding elements 10 and 20:", a)

