from time import sleep
import sys
import time


List_ProductID = [] 
List_ProductName = []
List_ProductPrice = []
List_ProductQuantity = []
#-------------------------------------------------ShopMainMenu[Start]-----------------------------------------------------#
def menu():
    Main_Menu =f"--Shop Management System--\n1.Add Product\n2.Update Product\n3.Remove Product\n4.Display Products\n5.Exit"
    print(Main_Menu)

      #--------Error handeling for Menu[start]----------#
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print(f"\nERROR!,Please enter a integer\n")
        return menu()
    
      #--------Error handeling for menu[END]----------#

    

    #Fabricate a directory for every sub menu 
    if choice == 1:
        Add_ProductMenu()
    elif choice == 2:
        UpdateProduct()
       
    elif choice == 3:
       Remove_Product()
    elif choice == 4:
        Displaying_Product()
        
    else:
        if choice == 5:
            print("Exiting....")
            time.sleep(2)
            print("Successfully Exited.")
            sys.exit()
           
    return Main_Menu
#---------------------------------------------------ShopMainMenu[END]-------------------------------------------------------------#


#---------------------------------------------------Add Product Menu[Start]-------------------------------------------------------------#
def Add_ProductMenu():
    while True:
        Product_Menu_Msg = f"\n--Add Product--"
        print(Product_Menu_Msg)

        ProductID = 0
        #-------ProductID Error Handeling[Start]----#
        try:
            ProductID = int(input("Enter Product ID: "))
        except ValueError:
            print("ERROR!,Please enter a number")
            Add_ProductMenu()
         #-------ProductID Error Handeling[END]----#

        List_ProductID.append(ProductID)
        
        ProductID = ProductID + 1

        ProductName = ""
        #---------ProductName Error Handeling[START]----#
        try:
            ProductName = input("Enter Product Name: ")
        except ValueError:
            print("ERROR!,Please Enter a Valid entry")
            Add_ProductMenu()

        if ProductName == "":
            print("Please enter a value")
            Add_ProductMenu()
        #---------ProductName Error Handeling[START]----#

        List_ProductName.append(ProductName)
        # ProductName = ProductName + 1
 
        #---------Product Price Error Handeling[START]-----#
        try:
            ProductPrice = float(input("Enter Product Price: "))
        except ValueError:
            print("ERROR!,Please enter a valid Entry(Integer)")
            Add_ProductMenu()
         #---------Product Price Error Handeling[END]-----#

        List_ProductPrice.append("R" + str(ProductPrice))

        ProductQuantity = 0
        #-------ProductQuantity Error Handeling[START]-------#
        try:
            ProductQuantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Error!,Please enter a Integer Value")
            Add_ProductMenu()
        #-------ProductQuantity Error Handeling[END]-------#


        List_ProductQuantity.append(ProductQuantity)
        ProductQuantity = ProductQuantity + 1

        print("Adding......")
        time.sleep(2)
        print("Product added Successfully")

        

         #-----------------------Product Menu End question[START]--------------#
            #-----Error handeling for it[START]------#
        try:
            terminate = input("Do you want to add another product('y'/'n')? ")
        except ValueError:
            print("Invalid Entry!,Please follow the instructions")
            Add_ProductMenu()
            #-----Error handeling for it[END]------#

        if terminate == 'y' or terminate == 'Y':
            print(f"Directing to 'Add product menu'....\n")
            time.sleep(2)
            Add_ProductMenu()

        if terminate == 'n' or terminate == 'N':
            print(f"Directing back to 'main menu'....\n")
            time.sleep(2)
            menu()
        
        break
        #-----------------------Product Menu End question[END]--------------#
#---------------------------------------------------Add Product Menu[END]-------------------------------------------------------------#



#--------------------------------------------------Update Product Menu[START]---------------------------------------------------------#
def UpdateProduct():
    Product_Update = f"\n--Update Product--"
    print(Product_Update)
    inc = 0
    while inc == 0:
        #----------Update ProductID ERROR Handeling[START]------#
        try:
            pick = int(input("Enter Product ID to Update: "))
        except ValueError:
            print("ERROR!,Please enter a valid input")
            UpdateProduct()
        #----------Update ProductID ERROR Handeling[END]------#

        if pick in List_ProductID and pick != 0:# conditional statement to check if the value exsists in the list
            print(f"Product found with ID:{pick}")

            #---------------Update ProductName ERROR Handeling and Update[START]----------------#
            try:
                update_name = input("Enter updated product name (or leave blank to keep the same): ")
                List_ProductName[pick-1] = update_name
            except ValueError:
                print("ERROR!,Please enter a valid input.")
                UpdateProduct()
            #---------------Update ProductName ERROR Handeling and Update[END]----------------#



            #---------------Update ProductPrice ERROR Handeling and Update[START]----------------#
            try:
                update_price = float(input("Enter updated product price (or leave blank to keep the same): "))
                List_ProductPrice[pick-1] = update_price
            except ValueError:
                print("Invalid Entry!, Please enter a valid value")
                UpdateProduct()
             #---------------Update ProductPrice ERROR Handeling and Update[END]----------------#


            #---------------Update ProductQuantity ERROR Handeling and Update[START]----------------#
            try:
                update_Quantity = int(input("Enter updated quantity (or leave blank to keep the same): "))
                List_ProductQuantity[pick-1] = update_Quantity
            except ValueError:
                print("Invalid Entry!, Please enter a Quantity")
                UpdateProduct()
            #---------------Update ProductQuantity ERROR Handeling and Update[END]----------------#

            print("Updating Products......")
            time.sleep(3)
            print("Product Successfully updated")
            inc += 1

        elif pick == 0:
            inc += 1
        else:
            print("Invalid!,Please try again.")

        
        #-----------------------Product update Menu End question[START]--------------#
            #-----Error handeling for it[START]------#
        try:
            terminate_Update = input("Do you want to update another product('y'/'n')? ")
        except ValueError:
            print("Invalid Entry!,Please follow the instructions")
            UpdateProduct()
            #-----Error handeling for it[END]------#

        if terminate_Update == 'y' or terminate_Update == 'Y':
            print(f"Directing to 'Update product menu'....\n")
            time.sleep(2)
            UpdateProduct()

        if terminate_Update == 'n' or terminate_Update == 'N':
            print(f"Directing back to 'main menu'....\n")
            time.sleep(2)
            menu()
        #-----------------------Product update  Menu End question[END]--------------#

#--------------------------------------------------Update Product Menu[END]---------------------------------------------------------#

#--------------------------------------------------Displaying Product Menu[START]---------------------------------------------------------#
def Displaying_Product():
    
    #---------------------Loop for Displaying Menu[START]------------------#
   
    print(f"\n--Display Menu--")
    for i in List_ProductID:
        index =List_ProductID.index(i)

        if index >= 0:#conditional statement to display the index of 'list_product id' to all list)
            print("ProductID:",List_ProductID[index],
            "\nProductName:",List_ProductName[index],
            "\nProductPrice:",List_ProductPrice[index],
            "\nProductQuantity:",List_ProductQuantity[index],
            "\n---------------\n")
    
    #Conditional Statement for Returning
    try:
        back = int(input("0.Back: "))
    except ValueError:
        print("Invalid Entry!,Please enter a correct value")
        Displaying_Product()

    #Directing user back to main menu   
    if back == 0:
        print("Directing to 'Main Menu'...")
        time.sleep(2)
        menu()

     #-------------------Loop for Displaying Menu[END]-------------------#

#--------------------------------------------------Displaying Product Menu[END]---------------------------------------------------------#

  
#--------------------------------------------------Removing Product[START]--------------------------------------------------------------#


def Remove_Product():
    print("\n--Remove Product Menu--")
    for i in List_ProductID:

        #---------Error handeling for Remove variable[START]--------------#
        try:
            Product_Remove = int(input("Enter the Product ID to 'remove': "))
            ProductID_Index = List_ProductID.index(Product_Remove)

              #----------Conditional Statement to remove product[START]----------------#
            if Product_Remove >= 0:
                    List_ProductID.pop(ProductID_Index) 
                    List_ProductName.pop(ProductID_Index) 
                    List_ProductPrice.pop(ProductID_Index) 
                    List_ProductQuantity.pop(ProductID_Index)

              #----------Conditional Statement to remove product[END]----------------#
          
           
        except ValueError:
            print("Invalid Entry!, Please enter a valid Input.")
            Remove_Product()

        #---------Error handeling for Remove variable[END]--------------#

        print("Removing product....")
        time.sleep(2)
        print("Product successfully removed")

        


        #----------Error Handeling for Resume msg[START]----------------#
        try:
            again = input("Do you wish to 'Remove' another product ('y'/'n')? ")
        except ValueError:
            print("Invalid Entry!,Please enter a valid input.")
            Remove_Product()

        if again == 'y' or again == 'Y':
            print(f"Directing to 'Remove Product Menu'....\n")
            time.sleep(2)
            Remove_Product()

        if again == 'n' or again == 'N':
            print(f"Directing back to 'main menu'....\n")
            time.sleep(2)
            menu()
        

        #----------Error Handeling for Resume msg[END]----------------#
        break



#--------------------------------------------------Removing Product[END]--------------------------------------------------------------#

        
    
            

 

menu()


        
            
    
            
  
