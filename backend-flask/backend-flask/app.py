from flask import Flask, request
from flask_cors import CORS

from services.home_activities import HomeActivities
from services.user_activities import UserActivities
from services.create_activity import CreateActivity
from services.create_reply import CreateReply
from services.search_activities import SearchActivities
from services.message_groups import MessageGroups
from services.messages import Messages
from services.create_message import CreateMessage
from services.show_activity import ShowActivity


app = Flask(__name__)

frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
origins = [frontend, backend]

cors = CORS(app, resources={
    r"/api/*": {
        "origins": origins
    }
}, expose_headers="location,link", allow_headers="content-type,if-modified-since", methods="OPTIONS,GET,HEAD,POST")


@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
    user_handle = 'andrewbrown'
    model = MessageGroups.run(user_handle=user_handle)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200


@app.route("/api/messages/@<string:handle>", methods=['GET'])
def data_messages(handle):
    user_sender_handle = 'andrewbrown'
    user_receiver_handle = request.args.get('user_receiver_handle')

    model = Messages.run(user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data'], 200


@app.route("/api/messages", methods=['POST', 'OPTIONS'])
@cross_origin()
def data_create_message():
    user_sender_handle = 'andrewbrown'
    user_receiver_handle = request.json['user_receiver_handle']
    message = request.json['message']

    model = CreateMessage.run(message=message, user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
    if model['errors'] is not None:
        return model['errors'], 422
    else:
        return model['data
