def temp_sensor(name):
    k=True
    while k==True:    
        import random
        import time
        temperature=random.uniform(35,90)
        print (f"The current temperature is {temperature:.2f}°C")
        humidity=random.randint(30,100)
        print(f"Humidity is {humidity}%")
        if temperature>60:
            print(f" The temperature is above 60°C \n ")
        while temperature>60:
            k=str(input())
            k=k.upper()
            if k=="BREAK" :
                break
            else:
                continue
            break

        if temperature>60:
            print("The alarm has been switched off successfully")
        else:
            print("The temperature is normal")
        time.sleep(7)
        k=True

name=str(input("ENTER YOUR USERNAME: "))
temp_sensor(name)
