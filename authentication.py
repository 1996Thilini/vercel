import pyrebase

# config = {
#     "apiKey": "AIzaSyCkcghScc6rDrgb0x8b8bZ5gUt4s5tihtU",
#     "authDomain": "fir-4-88c8d.firebaseapp.com",
#     "projectId": "fir-4-88c8d",
#     "storageBucket": "fir-4-88c8d.appspot.com",
#     "messagingSenderId": "165675594303",
#     "appId": "1:165675594303:web:27ec60d3d64209643ffe8a",
#     "measurementId": "G-07ZGC1QLYM",
#     "databaseURL":"https://fir-4-88c8d-default-rtdb.asia-southeast1.firebasedatabase.app/"
# }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()


# email = 'thilini.wmf@gmail.com'
# password = '123456'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

# user = auth.sign_in_with_email_and_password(email, password)
# print(user)

# info = auth.get_account_info(user['idToken'])
# print(info)

#auth.send_email_verification(user['idToken'])

#auth.send_password_reset_email(email)


# db = firebase.database()
# data = {"nm":"Thilini Fdo"}
# db.child("post").child("name").set(data)