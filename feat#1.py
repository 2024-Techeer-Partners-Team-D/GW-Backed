def create_m_table(num) :
    try :    
        num = int(num)

        if num < 1 or num > 9 :
            print("Please select one of 1 ~ 9")
            return
            
    except :
        return
            
    else :
        for i in range(1, 10) :
            print(f"{num} * {i} = {num*i}")

if __name__ == "__main__" :
    print("If you want to exit, just input 'q'")
    
    while True:
        print("Please input int type")
        num = input()
        
        if num == "q" :
            break

        create_m_table(num)