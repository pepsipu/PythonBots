class PlatinAuth():

    username = None
    password = None
    plan = None

    def createLogin(self):
        global username
        global password
        global plan
        username = input("Please input your PlatinBot username.\n")
        password = input("Please input your PlatinBot password.\n")
        plan = input("Please input your plan.\n")
        file = open("Auth.txt","a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write(" ")
        file.write(plan)
        file.close()

