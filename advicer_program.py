import pdt_operations as pdt_fun
import header as hd
import database as db

# total price 
total_price = 0
# imported header
hd.header_title()

# function to present these products 
print("BUYING SECTION \n")
print("Products vailable \n")

# applying methods
pdt_fun.all_pdts()

print("\n - ")
component = int(input("choose commodity from 1 -5 "))
pdt_content = pdt_fun.on_pdt(component)
print(pdt_content)

quantity = input("Enter product quantity ")
pdt_fun.pdt(pdt_content,quantity)
print('Your bought quantity is' ,quantity ,'of',component)

# print(" you bought ",db.database_products, 'total amount', total_price )
          
print(total_price)
hd.footer()