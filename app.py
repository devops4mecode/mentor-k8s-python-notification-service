from flask import Flask, jsonify, request
app = Flask(__name__)
app.config['SECRET_KEY']='asdwefeqe1232143'

from mailjet_rest import Client

api_key = 'f7d4b98cd2bd603518e1ba92383f2d87'
api_secret = 'fa3eb0d96cb9be8cebe77e493f3ab933'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

@app.route('/service')
def service():
    return 'Notification Service',200

@app.route('/sendEmail',methods=["POST"])
def sendEmail():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json
        name = body["name"]
        email = body["email"]
        data = {
  'Messages': [
    {
      "From": {
        "Email": "najibradzuan@devops4me.com",
        "Name": "Najib Radzuan Mentor"
      },
      "To": [
        {
          "Email":email,
          "Name": name
        }
      ],
      "Subject": "Greetings from Mentor-Najib Radzuan ",
      "TextPart": "Welcome to the K8S-Python Tutorial",
      "HTMLPart": f"<h3>Dear {name} , Hope you have understood the basics of Kubernetes.Thanks for reading!"
    }
  ]
}
        mailjet.send.create(data=data)
        return jsonify({"Accepted":202}),202
    else:
        return jsonify({"Bad Request":400}),400
        
if __name__ == '__main__':
	app.run(debug=True)