dic = {1:"Mechanical", 2:"Electrical", 3:"Civil"}
cnt = 404
while cnt:
    
    print("1. Add  course")
    print("2. Update  course")
    print("3. Display  course")
    print("4. Find  course")
    print("5. Delete  course")
    print("0. EXIT")
    
    choice = int(input("Enter your choice"))
    
    if choice == 1:
        
        c_name = input("Enter course name to add: ")
        c_no = len(dic) + 1
        dic[c_no]=c_name
        print("Course added successfully.")
    
    elif choice == 2:
        
        c_no = int(input("Enter course no to update: "))
        c_name = input("Enter course updated name: ")
        dic_len = len(dic)
        
        if 1 <= c_no <= dic_len:
            dic.update(c_no, c_name)
            print("Course updated successfully.")
    
    elif choice == 3:
        
        c_no = int(input("Enter course no to display: "))
        print(dic.getkey(c_no))
        
        # print(dic)
        
    elif choice == 4:
         
        #c_no = int(input("Enter course no to update: "))
        c_name = input("Enter course updated name: ")
        for name in dic.values():
            if name == c_name:
                print(name.getkey)
                print("Course Found")
            else:
                print("Bhad me ja")
        
    elif choice == 0:
        cnt = 407