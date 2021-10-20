username=[""]
password=[""]
while True:

     userinput = int(input("Please enter 1 to Rigister and 2 to Login:> "))

     def CreateAccount():
      newuser_input = input("Enter your Email:> ")
      newpass_input = input("Enter your pasword:> ")
      username[0] = newuser_input 
      password[0] = newpass_input 
      print("Your username is :> ",username[0])
      print("your password is :> ",password[0])
      for i in range(len(username)):
        print("To check in username:>",username[i])
 
     def Login():

      while True:

       l_username = input("Login:Please enter your username:> ")
       l_password = input("Login:Please enter your password:> ")
       for i in range(len(username)):
         print("To check in username:>",username[i])
         if username[i] == l_username:
          for z in range(len(password)):
            if password[z] == l_password:
             print("your successfully login:! ")
         else:
             print("wrong password:>")
            
     if userinput == 1:
      CreateAccount()

     else:
       Login()






    
