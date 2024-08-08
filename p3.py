from matplotlib import pyplot as p 
us=[12,32,16,45]
la=["asus","dell","lenovo","hp"]
e=[0,0,0,0.04]
p.pie(us,labels=la,startangle=270,explode=e,autopct='%1.2f%%')
p.show()
