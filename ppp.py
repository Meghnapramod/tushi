from matplotlib import pyplot as  p 
pro_na = ["intel","amg","snapdragon","tensor"]
use=[200,100,250,50]
p.bar(pro_na,use,color='black',width=0.2)
p.xlabel("processors"),p.ylabel("number of users")
p.title("processor users in a community")
p.show()