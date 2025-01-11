
# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.

def table(n):
    with open(f"Practice Set Ch 9/Tables/{n}_Table.txt",'a') as f:
        for i in range(1,11,+1):
            f.write(f"{n} × {i} = {n*i}\n")
for i in range(2,21,+1):
    table(i)
        

