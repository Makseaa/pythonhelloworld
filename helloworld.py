#print('Hello World') #This is the first script created by me: Mac Cea
messages= ['HelloWorld','Hi Mac','This is a wonderful World']
def ShowingMessage(message, number) :
    return_message=""
    return_number=number
    for x in messages:
        if message in x:
           return_message= x
    return return_message+" &&n number: "+str(return_number)
#modified
print(ShowingMessage('Hi Mac', 10))
