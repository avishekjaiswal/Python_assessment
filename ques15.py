def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

a=input("Enter a list of tuples:")
print(sort_list_last(a))