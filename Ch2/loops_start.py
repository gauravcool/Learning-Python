#
# Example file for working with loops
#

def main():
  x = 0

  # # define a while loop
  # while (x < 5):
  #   # print(x)
  #   x = x + 1

  # # define a for loop
  # for x in range(5, 10):
  #   print(x)


  # use a for loop over a collection
  # months=['jan','feb','march','april','may']
  # for m in months:
    # print(m)
 
  # use the break and continue statements
  for x in range(10,20):
    if(x == 15): 
      continue
    # print(x)


  #using the enumerate() function to get index 
  months=['jan','feb','march','april','may']
  for i,d in enumerate(months):
    print(i,d)

if __name__ == "__main__":
  main()
