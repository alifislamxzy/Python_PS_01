s = {1, 5, 7, 8, 9, 2, 6,}


# print(type(s))
# s.remove(5)
# print(len(s))
# s.pop() 
# s.clear()

un_s = s.union({5, 6})
in_s = s.intersection({5, 6})

print("this is set Union :", un_s)
print("this is set Intersection :", in_s)