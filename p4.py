from matplotlib import pyplot as p 
us=[12,32,16,45]
la=["asus","dell","lenovo","hp"]
p.pie(us,labels=la,startangle=270,autopct='%1.2f%%')
p.show()