def insert_details():
    n = int(input("enter the no of account id's"))
    a = []
    for i in range(n):
        ele = int(input("enter acc_id:"))
        a.append(ele)
    print(a)

def linear_search(a,item):
    for i in range(len(a)):
        if a[i] == item:
            print(item,"in found at index",i)
            return True
    print(item,"ins not found")
    return False

def binary_search(b,AC_id):
    left = 0
    right = len(b)-1
    while left <= right:
        mid = (left + right) // 2
        if(b[mid] == AC_id):
            flag = True
            print(AC_id, "is found at index", mid)
            break
        elif(b [mid]> AC_id):
            right = mid -1
        else:
            left = mid + 1
    print(AC_id,"is not found")
    return False

def menu_driven():

    Ac_id = []
    while True:   
        print("/n---Menu---")
        print("1.Insert_Details.")
        print("2.Linear_Search.")
        print("3.Binary_Search.")
        print("4.Program Exit.")

        choice = int(input("enter the choice : "))
        if choice == 1:
            accounts = insert_details()
            print("Ac_ids")
        elif choice == 2:
            if not accounts:
                print("insert account id.")
                continue
            search_item = int(input("enter the account ids for search: "))
            linear_search()
        elif choice == 3:
            binary_search()
        else:
            exit()
            break
    print("invalide choice")  

def exit():
    print("EXIT PROGRAM ,THANK YOU...!")