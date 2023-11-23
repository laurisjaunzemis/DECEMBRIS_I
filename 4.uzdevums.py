skaitlis=int(input("Ievadiet skaitli:"))
sum=1
for iznakums in range(1,skaitlis+1):
    sum *= iznakums

print("Faktoriāls skaitlim",skaitlis,"ir",sum)