import datetime as dt
product=[]
categorize={}
class Inventory(Exception):
    def add_products(p_name,p_category,p_price,p_quantity,p_expiry):
        product.append([p_name,p_category,(p_price),(p_quantity),p_expiry])
        print("Product added successfully:")
        try:
            f=open("Inventory.txt",'a+')
            f.write(f"{p_name},{p_category},{p_price},{p_quantity},{p_expiry}\n")
            f.close()
        except Exception as e:
            print(e) 
    def remove_product(product_name):
        i1=False
        for i in product:
            if i[0]==product_name:
                product.remove(i)
                i1=True
                print(product)
                break
        if i1==False:
              print("Product not found:")
    def search_product(search):
        i1=False
        for i in product:
            if i[0]==search:
                print(i)
                i1=True
                break
        if i1==False:
            print("Product not found:")
    def list_all_products():
        for i in product:
            print(i)
    def categorize_products():
        categorize={}
        for i in product:
            category = i[1]  
            if category not in categorize:
               categorize[category] = []
            categorize[category].append(i)
        for category,item in categorize.items():
            print(f"Category:{category}")
            for i in item:
               print(f"Items:{i}")
    def expired_product():
        current_date = dt.datetime.now()
        expired_products=[]
        for i in product:
            try:
               p_expiry = dt.datetime.strptime(i[4], '%Y-%m-%d')
               if current_date>p_expiry:
                  expired_products.append(i)
            except Exception as e:
                print(e)
        if expired_products:
            print("Expired products:")
            for i in expired_products:
                print(i)
        else:
            print("No expired products.")  
    def load_file():
        try:
           f=open("Inventory.txt")
           read=f.readlines()
           global product
           for i in read:
               p_name, p_category, p_price, p_quantity, p_expiry = i.strip().split(',')
               product.append([p_name, p_category,p_price,p_quantity, p_expiry])
           print(product)
        except Exception as e:
            print(e)
i1=Inventory      
while True:
      print("1.Add Product\n2.Remove Product\n3.Search for product\n4.List all Product\n5.Catogrize Products\n6.Expired Product\n7.Load File\n8.Exit")
      ch=int(input("Enter your request:"))
    
      if ch==1:
        p_name=input("Enter Product name:")
        p_category=input("Enter Product Category:")
        p_price=input("Enter Product Price:")
        p_quantity=input("Enter Products's Quantity:")
        p_expiry=input("Enter Expiry Date(yyyy-mm-dd):")
        i1.add_products(p_name,p_category,p_price,p_quantity,p_expiry)
      elif ch==2:
          p_name=input(("enter product name"))
          i1.remove_product(p_name)
      elif ch==3:
          p_name=input(("enter product name to be searched"))
          i1.search_product(p_name)
      elif ch==4:
          i1.list_all_products()
      elif ch==5:
          i1.categorize_products()
      elif ch==6:
          i1.expired_product()
      elif ch==7:
          i1.load_file()
      elif ch==8:
          break
          
    
