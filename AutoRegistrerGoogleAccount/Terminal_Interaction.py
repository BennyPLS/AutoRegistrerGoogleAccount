import AutoChrome
if __name__ =="__main__":
    print(""" 
        - Programa de iniciado y cerrado de sesion automatico - 
                - Y otras funciones automaticas -
        """)
    if ((input("Quiere poner las credenciales por defecto? (S/N) :").lower() == "s")):
        if ((input("Quiere iniciar sesion? (S/N) :")).lower() == "s"):
            AutoChrome.Init()
            AutoChrome.Sign_in(3)
    else:
        if ((input("Quiere iniciar sesion? (S/N) :")).lower() == "s"):
            Email = input("Email :")
            Password = input("Contraseña :")
            AutoChrome.Init()
            AutoChrome.Sign_in(4,Email,Password)
    if (AutoChrome.isSignIn):
        if ((input("Quiere ir a Class Room? (S/N) :")).lower() == "s"):
            AutoChrome.Go_ClassRoom()
