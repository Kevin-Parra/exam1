from flask import Flask, request
app = Flask ('__main__')

device = {
"code" : "1204520",
"descrip": "Mobile device",
"value" : 120
}

@app.route('/devices', methods=['GET'])
def go_home():
    return device
    #save an user
@app.route('/users' , methods=['POST'])
def save_user():
        user = request.json
        print(user)
        return user

#save a device
@app.route('/devices' , methods=['POST'])
def save_device():
    device = request.json
    return device

if __name__ == '__main__':
        app.run(debug= True, port=5000)


{
    "matricula":"6520150010",
    "first_name": "Kevin",
    "last_name":"Parra",
    "phone": "6141209092"
}
