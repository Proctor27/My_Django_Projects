#lists

Beach = ["House","You", "Hello", 1,2,5,6,"Topic",["Dance","With","Me"]]
#print(Beach)

Beach[2] ="HelloYou"
#print(Beach)

Beach[-3] = "Underwood"
#print(Beach)

print(Beach[-1][-2])

Melody =["House","You", "Hello", 1,2,5,6,"Topic",["Dance","With","Me"]]
Melody.append("Unchained")

Just = ["once",1,3.4]
Melody.extend(Just)
#print(Melody)

time = Melody.pop() 
#print(Melody)
#print(time)

 
#print(Melody)

#LIST COMPREHENSION
Angel_Face = [[1,2,3,4],['Angel','Face','Wolves','3'],['List',45,'Meet','Hope']]

Kill = [row[3] for row in Angel_Face]
print(Kill)


x = [3,5,11,33]

wind =[num**2  for num in x]
print(wind)
         