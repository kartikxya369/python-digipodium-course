name = input("enter ur Name: ")
email = input("enter ur Email: ")
mobile = input("enter ur Mobile: ")
city = input('Enter City: ')

# nested if-else
if len(name) > 1:
    if '@' in email and len(email) > 11:
        if len(mobile) == 10 and mobile.isnumeric():
            if city in ['lucknow','delhi','noida']:
                print("Your data is saved, Thankyou")
            else:
                print('we are not available in ur city')
        else:
            print('Invalid mobile number⚠️')
    else:
        print('Invalid email address⚠️')
else:
    print('Ye kaisa naam h❓')

