itemAvailableDict={}
shoppingDict={}
dct_rate_soup=float(50.0)                              #discount rate for soup offer
dct_rate_apples=float(10.0)                            # 10% off apples


#welcome User
userName=input("Please enter your name: ")
welcomeMessage=f"Welcome to my shop {userName}!"
lenWCMsg=len(welcomeMessage)
print("*"*lenWCMsg)
print(welcomeMessage)
print("*"*lenWCMsg)

#read data from text file
my_file=open("products_price.txt")
file_line=my_file.readline()
itemsAvailable=my_file.readlines()
# print(itemsAvailable)
my_file.close()

#fetch items from list and add to a dictionary
print("***********Select Items Available in Our Shop****************")
for item in itemsAvailable:
   item_name=item.split()[0]
   item_price=item.split()[1]
   item_discount=item.split()[2]
   print(f"{item_name}: {item_price}: {item_discount}")
   itemAvailableDict.update({item_name: float(item_price)})
print("*"*20)
print("OFFER: Buy 2 tins of soup and get a loaf of bread for half price.")
print("*"*20)
print(itemAvailableDict)


#prompt user to add items
proceedShopping=input("Do you wish to add items to your basket?  (yes/no): ")
while proceedShopping.lower()=="yes":
  item_added=input("Add an item: ")
  if item_added.title() in itemAvailableDict:
    item_qty=int(input("Add quantity: "))
    shoppingDict.update({item_added:{"quantity":item_qty,"subtotal":itemAvailableDict[item_added.title()]*item_qty}})
    print(shoppingDict)

  else:
    print("unable to add unavailable item")
  proceedShopping=input("Do you wish to add more items (yes/no): ")
else:
  print("\n")
  print("****Bill Summary***** ")
  print("\n")
  print("Item    Quantity    SubTotal")
  total = 0.0
  for key in shoppingDict:
    dct_applied_apples = float(shoppingDict[key]['subtotal']* dct_rate_apples / 100.0)
    dct_applied_soup = float(shoppingDict[key]['subtotal']* dct_rate_soup / 100.0)

# add 10% discount
    if key == "apples":
      dct_applied_apples
    else:
      dct_applied_apples = 0.0

    if key== "bread":
      dct_applied_soup
    else:
      dct_applied_soup = 0.0


#print receipt
    print(f"{key}    {shoppingDict[key]['quantity']}        {shoppingDict[key]['subtotal']}")
    total=shoppingDict[key]['subtotal']+total
    final_disc = dct_applied_apples+dct_applied_soup
    final_total = total - final_disc
    print(f"Total Price: {total}   Final Price: {final_total}   Discount Applied: {final_disc}")
  print("***********Thank You********")
  print("Hope to see you soon!")


