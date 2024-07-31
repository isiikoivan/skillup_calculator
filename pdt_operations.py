import database as db

# on select aproduct 
def on_pdt(n):
    pdts = ''
    if isinstance(n, int):
        if n == 1:
            pdts = 'bread'
        elif n == 2:
            pdts = 'cookies'
        elif n == 3:
            pdts = 'soda'
        elif n == 4:
            pdts = 'cake'
        elif n == 5:
            pdts = 'muffin'
        else:
            print('Invalid item selected:', n)
            return
        print('You chose:', pdts.capitalize())
        return pdts
    else:
        print('Invalid value inserted:', n)
        
  

def all_pdts():
    print("1.Bread (6000)")
    print("2.Cookies(2000)")
    print("3.Soda(1800)")
    print("4.cake (65000)")
    print("5.muffin(1800)")




def process():
    # another function to present proceed , cancel , 
    print("\n - ")
    print("A . Add More Products")
    print("P . proceed (confirm) ")
    print("C . Cancel")

def credentials():
    # another function to present login and register
    print("\n - ")
    print("0.Login  (already have account) ")
    print("00.Register (Have no account)")

# add products 
def pdt(pdts,quantity=1):
    total_price = 0

    print(db.database_cart.append(pdts))
    return
    total_price = total_price + db.database_products.get(pdts)*quantity
    return total_price 

