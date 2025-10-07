# import json
# import time

# fd = open('Inventory.txt','r')
# products = fd.read().split('\n')
# fd.close()

# ui_username = input("Enter your Name: ")
# ui_phone    = input("Enter your Phone No: ")
# ui_mail     = input("Enter your Mail: ")
# ui_prod_id  = input("Enter product ID: ")
# ui_prod_qn  = input("Enter product Quantity: ")

# if (int(ui_prod_qn) <= int(prod_details[3])):

#     print("-----------------------------")
#     print("Product Name     : ", prod_details[1])
#     print("Price            : ", prod_details[2]) 
#     print("Quantity         : ", ui_prod_qn)
#     print("-----------------------------")
#     print("Billing Amount   : ", int(ui_prod_qn) * int(prod_details[2]))
#     print("-----------------------------")

#     # Updating Inventory
#     prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))
# else:
#     print("Sorry, We're not having enough quantity.")
#     print("We're having only",prod_details[3],'quantity.')
#     print("Would you like to purchase it?")

#     ch = input("Press Y/N: ")

#     if (ch == 'Y' or ch == 'y'):
#         print("-----------------------------")
#         print("Product Name     : ", prod_details[1])
#         print("Price            : ", prod_details[2])
#         print("Quantity         : ", prod_details[3])
#         print("-----------------------------")
#         print("Billing Amount   : ", int(prod_details[3]) * int(prod_details[2]))
#         print("-----------------------------")

#         # Update Inventory
#         prod_details[3] = '0'

#     else:
#         print("Thanks")
        
# fd = open("Sales.txt",'a')
# sales_detail = ui_username +","+ ui_phone +","+ ui_mail +","+prod_details[1] +","+ ui_prod_id +","+ ui_prod_qn +","+ str(int(ui_prod_qn) * int(prod_details[2]))+","+time.ctime()+ "\n"
# fd.write(sales_detail)
# fd.close()

# fd = open('Inventory.txt','w')

# for i in updated_product_lst:
#     fd.write(i)
# fd.close()

# print("Inventory Updated")






