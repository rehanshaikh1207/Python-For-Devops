def check_os(opsystem):
    if opsystem == "Windows":
        print("Switch to linux")
    elif opsystem == "linux" or opsystem == "mac":
        print("you are good to go")
        

for i in range(0,5):
    check_os("mac")