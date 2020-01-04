item = input('Item (enter "done" when finished): ')
items =[]
totalprice =0.0
while item != "done":
	price = float(input("Price: "))
	quantity = int(input("Quantity: "))
	d = {"name":item,"price":price,"quantity":quantity}
	items.append(d)
	item = input('Item (enter "done" when finished): ')
print("-------------\nreceipt\n-------------\n")
for i in range(len(items)):
	print (str(items[i]["quantity"])+" "+str(items[i]["name"])+" "+str(items[i]["price"]))
	totalprice += (items[i]["quantity"])*(items[i]["price"])
print("-------------")
print("Total Price: "+str(totalprice))
