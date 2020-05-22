from flask import Flask, request, jsonify
import os
import traceback
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
	return("Hello !"))
@app.route('/predict', methods=['POST'])
def predict():
	try:
		json_ = request.get_json()
		bot_id=json_['bot_id']
		user_id=json_['user_id']
		module_id=json_['module_id']
		channel=json_['channel']
		incoming=json_['incoming_message']
		print(json_)
		response=[{
		'user_id':user_id,
		'bot_id':bot_id,
		'module_id':module_id,
		 'message':"hello nibba",
		 'suggested_replies':["Menu","Faqs"],
		 'blocked_input':False,
		}]
		return jsonify(response),200
	except:
		return jsonify({'trace': traceback.format_exc()})
if __name__=='__main__':
    app.run( debug=True)
