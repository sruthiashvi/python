def func(year):
 if year%400==0:
    return "true"
 elif year%100==0:
    return "false"
 elif year%4==0:
    return "true"
 else:
    return "false"
year=int(input("Enter year:"))
res=func(year)
print(res)
