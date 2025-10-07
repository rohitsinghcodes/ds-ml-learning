fd = open('inventory.txt', 'r')
products = fd.read().split('\n')
fd.close()

ui_prod_id = input("Enter product ID: ")
ui_prod_qn = input("Enter product Quantity: ")

updated_product_lst = []

for product in products:
    prod_details = product.split(',')
    # print(prod_details)
    if(prod_details[0] == ui_prod_id):
        if(int(ui_prod_qn) <= int(prod_details[3])):
            
            print('-'*30)
            print("Product Name      : ", prod_details[1])
            print("Product Price     : ", prod_details[2])
            print("Product Quantity  : ", ui_prod_qn)
            print('-'*30)
            print('Billing Amount    : ', int(ui_prod_qn) * int(prod_details[2]))
            
            prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))
            print(prod_details[3])
    updated_product_lst.append(prod_details)
    
lst = []

for i in updated_product_lst:
    prod = i[0] + ',' + i[1] + ',' + i[2] + ',' + i[3] + '\n'
    lst.append(prod)
    
lst[-1] = lst[-1][:-1]
fd = open('Inventory.txt', 'w')

for i in lst:
    fd.write(i)

fd.close()

