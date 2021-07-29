import sys

values = sys.argv[1:]  # bcz we have file name at 0 index 
print(sum(map(eval, values)))
