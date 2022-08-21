import pickle
l = []

with open("xyz.dat" , "wb") as X:
    c = 'y'

    while c == 'y' :
        print("******************************************")
        print("Enter the choice give below : ")
        print("1. Create Records ")
        print("2. Add Records ")
        print("3. Search Record ")
        print("4. Update Record ")
        print("5. Delete Record ")
        print("6. Display Record ")
        print("******************************************")
        
        a = int(input("Enter your choice :  "))
        
        if a==1:
            def create():

                rec = int(input("How many records you want to enter:  "))
            
                for i in range(rec):
                    roll = int(input("Enter Roll no. :  "))
                    name = input("Enter Name :  ")
                    clas = int(input("Enter Class :  "))
                    l_data = [roll , name , clas]
                    l.append(l_data)
                    pickle.dump(l , X)
            create()       
                    
                
        elif a==2:
            def add():

                rec = int(input("How many records you want to add:  "))
                for i in range(rec):
                    roll = int(input("Enter Roll no. :  "))
                    name = input("Enter Name :  ")
                    clas = int(input("Enter Class :  "))
                    l_data = [roll , name , clas]
                    l.append(l_data)
                    pickle.dump(l , X)
                    
            add()
            
            
        elif a==3:
            def search():
                 
                 sear = int(input("Enter roll no. whose record you are looking for :   "))
                 for i in range(len(l)):
                     if l[i][0]==sear:
                         
                         print("Roll number : ", l[i][0])
                         print("Name : ", l[i][1])
                         print("Percentage : ", l[i][2])
                          
                         
            search()
            
        elif a==4:
            def update():
                
                up = int(input("Enter roll no. whose record you are looking for :   "))
                for i in range(len(l)):
                    if l[i][0]==up:
                        print("Record Found")
                        print("Roll number : ", l[i][0])
                        print("Name : ", l[i][1])
                        print("Percentage : ", l[i][2])
                        print("1. Roll No. ")
                        print("2. Name ")
                        print("3. Class ")
                        
                        up = int(input("Enter choice you want to update :  "))
                        
                        if up==1:
                            nroll = int(input("Enter your new roll no. :  "))
                            l[i][0] = nroll
                            print("Rollno: " , l[i][0])
                            print("Name:   " , l[i][1])
                            print("Per:    " , l[i][2])
                            print("****record is updated*******")
                            
                        elif up==2:
                            nname = input("Enter your new name no. :  ")
                            l[i][1] = nname
                            print("Rollno: " , l[i][0])
                            print("Name:   " , l[i][1])
                            print("Per:    " , l[i][2])
                            print("****record is updated*******")
                         
                        elif up==3:
                            nclas = int(input("Enter your new class no. :  "))
                            l[i][2] = nclas
                            print("Rollno: " , l[i][0])
                            print("Name:   " , l[i][1])
                            print("Per:    " , l[i][2])
                            print("****record is updated*******")
                    
                    else:
                        print("Record not found")
                
            update()                
                         
        elif a==5:
            def delete():
                
                droll = int(input("Enter the roll no. to be deleted :  "))
                for i in range(len(l)):
                    if l[i][0]==droll:
                        print("Roll number : ", l[i][0])
                        print("Name : ", l[i][1])
                        print("Percentage : ", l[i][2])
                        
                        a = input("Are you sure about that 'y' or 'n' :  ")
                        if a=='y':
                            l.pop(i)
                            print("Record has been deleted ")
                            
                                
            delete()
            
        elif a==6:
            def display():
                
                dis = int(input("Select the choice  1. All Records 2. Individual Records : "))
                if dis==1:
                    for i in range (len(l)):
                        print("Roll number : ", l[i][0])
                        print("Name : ", l[i][1])
                        print("Percentage : ", l[i][2])
                    
                elif dis==2:
                    sear = int(input("Enter roll no. whose record you are looking for :   "))
                    for i in range(len(l)):
                        if l[i][0]==sear:
                            print("Roll number : ", l[i][0])
                            print("Name : ", l[i][1])
                            print("Percentage : ", l[i][2])
                    
            display()                   
                         
                                 
            
            
                 
                
             
             
             
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                