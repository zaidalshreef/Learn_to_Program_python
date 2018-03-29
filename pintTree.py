# ---------- PROBLEM : DRAW A PINE TREE ----------
# For this problem I want you to draw a pine tree after asking the user
# for the number of rows. Here is the sample program

'''
How tall is the tree : 5
    #
   ###
  #####
 #######
#########
    #
'''

# You should use a while loop and 3 for loops

# I know that this is the number of spaces and hashes for the tree
# 4 - 1
# 3 - 3
# 2 - 5
# 1 - 7
# 0 - 9
# Spaces before stump = Spaces before top

# So I need to
# 1. Decrement spaces by one each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to the stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spaces and then 1 hash


tree_hi=eval(input("enter height of the tree : "))

spaces=tree_hi-1

hashes=1

spaces_tem=spaces-1

while tree_hi!=0:
#another way to solve the problem
    #for i in range(spaces):
      #  print(" ",end="")
    #for i in range(hashes):
       # print("#",end="")

    print(spaces*" "+hashes*"#", end="")
    print()

    spaces-=1

    hashes+=2

    tree_hi-=1


#another way to solve the problem
# for i in range(spaces_tem):
#     print(" ",end="")
# print("#")
print((spaces_tem+1)*" "+"#",end="")

