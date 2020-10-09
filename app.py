from flask import Flask, request, jsonify
import requests
import os
import json
import traceback
import wikipedia
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello_world():
	return("Hello!")
@app.route('/youtube', methods=['POST','GET'])
def predictyt():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		search_result=incoming
		search_result=search_result.replace(" ","+")
		URL="https://www.youtube.com/results?search_query="+search_result
		r = requests.get(URL) 
		soup = BeautifulSoup(r.content, 'html.parser') 
		count=0
		links=[]
		c=0
		for row in soup.findAll('a',attrs={'class':"yt-uix-sessionlink spf-link"}):
			count=count+1
			url=row['href']
			if(count%2==1):
				c+=1
				url='https://www.youtube.com/'+url
				links.append(url)
				if c==2:
					break
		message="here are some Youtube suggestions from me ... have a look \n"
		for i in links:
			message+="[video]"+i+"[/video]\n "
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/youtube/French', methods=['POST','GET'])
def predictytfre():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		search_result=incoming
		search_result=search_result.replace(" ","+")
		URL="https://www.youtube.com/results?search_query="+search_result
		r = requests.get(URL) 
		soup = BeautifulSoup(r.content, 'html.parser') 
		count=0
		links=[]
		c=0
		for row in soup.findAll('a',attrs={'class':"yt-uix-sessionlink spf-link"}):
			count=count+1
			url=row['href']
			if(count%2==1):
				c+=1
				url='https://www.youtube.com/'+url
				links.append(url)
				if c==2:
					break
		message="voici quelques suggestions Youtube de moi ... jetez un oeil \n"
		for i in links:
			message+="[video]"+i+"[/video]\n "
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/ask/English', methods=['POST','GET'])
def predictytask():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		search_result=incoming
		search_result=search_result.replace(" ","+")
		URL="https://www.ask.com/web?o=34851&l=dir&qo=serpSearchTopBox&q="+search_result
		r = requests.get(URL) 
		soup = BeautifulSoup(r.content, 'html.parser') 
		count=0
		links=[]
		c=0
		for row in soup.findAll('a',attrs={'class':"PartialSearchResults-item-title-link result-link"}):
			count=count+1
			url=row['href']
			if(count%2==1):
				c+=1
				if c==1:
					continue
				links.append(url)
				if c==4:
					break
		message="[img]https://cdn.pixabay.com/photo/2015/10/30/12/24/questions-1014060_1280.jpg[/img]\nhere are some suggestions from me ... have a look \n"
		ct=1
		for i in links:
			message+="[url="+i+"]suggestion link-"+str(ct)+"[/url]\n "
			ct+=1
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/ask/French', methods=['POST','GET'])
def predictytsa():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		search_result=incoming
		search_result=search_result.replace(" ","+")
		URL="https://www.ask.com/web?o=34851&l=dir&qo=serpSearchTopBox&q="+search_result
		r = requests.get(URL) 
		soup = BeautifulSoup(r.content, 'html.parser') 
		count=0
		links=[]
		c=0
		for row in soup.findAll('a',attrs={'class':"PartialSearchResults-item-title-link result-link"}):
			count=count+1
			url=row['href']
			if(count%2==1):
				c+=1
				if c==1:
					continue
				links.append(url)
				if c==4:
					break
		ct=1
		message="[img]https://cdn.pixabay.com/photo/2015/10/30/12/24/questions-1014060_1280.jpg[/img]\nvoici quelques suggestions de ma part ... jetez un oeil \n"
		for i in links:
			message+="[url="+i+"]lien de suggestion-"+str(ct)+"[/url] \n "
			ct+=1
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/jobs', methods=['POST','GET'])
def desc():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		url="https://jobs.github.com/positions.json"
		PARAMS={'description':incoming}
		r=requests.get(url=url,data=PARAMS)
		message="[img]https://lh3.googleusercontent.com/6wXeJrI2mCvLDGlMzZVlcUkAecoopJYVoOeci3LOoWRuW_unD0XY-hblMZSgqpZ62Q[/img] \n"
		data=r.json()
		response={
		 'message':message+"Here are the job links: "+"\n[url="+data[0]["url"]+"]Nila Suggested job-1[/url]\n[url="+data[1]["url"]+"]Nila Suggested job-2[/url]\n[url="+data[2]["url"]+"]Nila Suggested job-3[/url]",
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})		
@app.route('/wiki/English', methods=['POST','GET'])
def predict():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		search=wikipedia.search(incoming)
		message="[img]https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/225px-Wikipedia-logo-v2.svg.png[/img]"+"here are some wiki suggestions \n"
		for i in range(0,3):
			ny = wikipedia.page(search[i])
			se=ny.url.split('/')[-1]
			message+="[url="+ny.url+"]"+ny.title+"[/url]\n"
		header = {"content-type": "application/json"}
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/wiki/French', methods=['POST','GET'])
def predict1():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		wikipedia.set_lang("fr")
		search=wikipedia.search(incoming)
		message="[img]https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/225px-Wikipedia-logo-v2.svg.png[/img]"+"here are some wiki suggestions \n"
		for i in range(0,3):
			ny = wikipedia.page(search[i])
			se=ny.url.split('/')[-1]
			message+="[url="+ny.url+"]"+ny.title+"[/url]\n"
		header = {"content-type": "application/json"}
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/jobs/Hindi', methods=['POST','GET'])
def deschi():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		url="https://jobs.github.com/positions.json"
		PARAMS={'description':incoming}
		r=requests.get(url=url,data=PARAMS)
		message="[img]https://lh3.googleusercontent.com/6wXeJrI2mCvLDGlMzZVlcUkAecoopJYVoOeci3LOoWRuW_unD0XY-hblMZSgqpZ62Q[/img] \n"
		data=r.json()
		response={
		 'message':message+"यहाँ नौकरी लिंक हैं: "+"\n[url="+data[0]["url"]+"]नीला सुझाव नौकरी -1[/url]\n[url="+data[1]["url"]+"]नीला सुझाव नौकरी -2[/url]\n[url="+data[2]["url"]+"]नीला सुझाव नौकरी -3[/url]",
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/news/policies', methods=['POST','GET'])
def deschinews():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming_country=header['country'].lower()
		incoming_city=header['city'].title()
		URL = "http://99.79.153.217:2221/"
		PARAMS = {
   			'country': incoming_country,
    		'city':incoming_city,
    		'category':"policies"
		}
		r = requests.post(url = URL,json=PARAMS)
		print(r)
		data=r.json()
		print(data)
		message=''
		j=0
		for i in data[incoming_country]:
			message+="[img]"+i["image_url"]+"[/img]\n[b]"+i["title"]+"[/b]\n"+i["description"]+"\n[url="+i["url"]+"]read more..[/url]\n"
			if j<2:
				message+="::next-1::\n"
			j+=1
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/news/vaccine', methods=['POST','GET'])
def deschinewsvaxc():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming_country=header['country'].lower()
		incoming_city=header['city'].title()
		URL = "http://99.79.153.217:2221/"
		PARAMS = {
   			'country': incoming_country,
    		'city':incoming_city,
    		'category':"vaccine"
		}
		r = requests.post(url = URL,json=PARAMS)
		print(r)
		data=r.json()
		print(data)
		message=''
		j=0
		for i in data[incoming_country]:
			message+="[img]"+i["image_url"]+"[/img]\n[b]"+i["title"]+"[/b]\n"+i["description"]+"\n[url="+i["url"]+"]read more..[/url]\n"
			if j<2:
				message+="::next-1::\n"
			j+=1
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/news/cases', methods=['POST','GET'])
def deschinewscases():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming_country=header['country'].lower()
		incoming_city=header['city'].title()
		URL = "http://99.79.153.217:2221/"
		PARAMS = {
   			'country': incoming_country,
    		'city':incoming_city,
    		'category':"cases"
		}
		r = requests.post(url = URL,json=PARAMS)
		print(r)
		data=r.json()
		print(data)
		message=''
		j=0
		for i in data[incoming_country]:
			message+="[img]"+i["image_url"]+"[/img]\n[b]"+i["title"]+"[/b]\n"+i["description"]+"\n[url="+i["url"]+"]read more..[/url]\n"
			if j<2:
				message+="::next-1::\n"
			j+=1
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})	
@app.route('/wiki/French1', methods=['POST'])
def predict1french():
	try:
		bot_id=request.form['bot_id']
		user_id=request.form['user_id']
		module_id=request.form['module_id']
		channel=request.form['channel']
		incoming=request.form['incoming_message']
		wikipedia.set_lang("fr")
		search=wikipedia.search(incoming)
		message="here are some wiki suggestions "
		for i in range(0,3):
			ny = wikipedia.page(search[i])
			message+=ny.url+" \n "
		response={
		'user_id':user_id,
		'bot_id':bot_id,
		'module_id':module_id,
		 'message':message,
		 'suggested_replies':["Menu","Faqs"],
		 'blocked_input':False,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/ask/Kids', methods=['POST','GET'])
def predictytask12():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		search_result=incoming+"top kids courses"
		search_result=search_result.replace(" ","+")
		URL="https://www.ask.com/web?o=34851&l=dir&qo=serpSearchTopBox&q="+search_result
		r = requests.get(URL) 
		soup = BeautifulSoup(r.content, 'html.parser') 
		count=0
		links=[]
		c=0
		for row in soup.findAll('a',attrs={'class':"PartialSearchResults-item-title-link result-link"}):
			count=count+1
			url=row['href']
			if(count%2==1):
				c+=1
				if c==1:
					continue
				links.append(url)
				if c==4:
					break
		message="[img]https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRfJZtSLWlYNHoDwJGEXdFmapCBG_xtJWObsA&usqp=CAU[/img]\nhere are some suggestions from me ... have a look \n"
		ct=1
		for i in links:
			message+="[url="+i+"]suggestion link-"+str(ct)+"[/url]\n "
			ct+=1
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})	
@app.route('/ask/college', methods=['POST','GET'])
def predictytask34():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming=header['incoming_message']
		search_result=incoming+"top college courses"
		search_result=search_result.replace(" ","+")
		URL="https://www.ask.com/web?o=34851&l=dir&qo=serpSearchTopBox&q="+search_result
		r = requests.get(URL) 
		soup = BeautifulSoup(r.content, 'html.parser') 
		count=0
		links=[]
		c=0
		for row in soup.findAll('a',attrs={'class':"PartialSearchResults-item-title-link result-link"}):
			count=count+1
			url=row['href']
			if(count%2==1):
				c+=1
				if c==1:
					continue
				links.append(url)
				if c==4:
					break
		message="[img]https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTl_4x5HoriCKoBAE9Vjv6WsDX2B_ilXG2Zzg&usqp=CAU[/img]\nhere are some suggestions from me ... have a look \n"
		ct=1
		for i in links:
			message+="[url="+i+"]suggestion link-"+str(ct)+"[/url]\n "
			ct+=1
		response={
		 'message':message,
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})	
@app.route('/cases', methods=['POST','GET'])
def deschicasescountry():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		incoming_country=header['country'].lower()
		URL = "http://99.79.153.217:2221/count"
		PARAMS = {
   			'country': incoming_country
		}
		r = requests.post(url = URL,json=PARAMS)
		print(r)
		data=r.json()
		print(data)
		message=message="[img]https://www.fda.gov/files/styles/featured_content_background_image/public/covid19-1600x900.jpg?itok=ZvOhgrde[/img]\nhere are the Covid insights ... have a look \n"
		message+="Number of cases per milion: "+str(data['data']['cases']['1M_pop'])
		message+="\nNumber of Active cases: "+str(data['data']['cases']['active'])
		message+="\nNumber of Critical cases: "+str(data['data']['cases']['critical'])
		if data['data']['cases']['new']!=None:
			message+="\nNumber of New cases: "+str(data['data']['cases']['new'])
		message+="\nNumber of recovered cases: "+str(data['data']['cases']['recovered'])
		message+="\nTotal Number of cases: "+str(data['data']['cases']['total'])
		message+="\nNumber of deaths per million: "+str(data['data']['deaths']['1M_pop'])
		message+="\nTotal Deaths: "+str(data['data']['deaths']['total'])
		message+="\nTests per million: "+str(data['data']['tests']['1M_pop'])
		message+="\nTotal Number of tests: "+str(data['data']['tests']['total'])
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/covid/pattern1', methods=['POST','GET'])
def despattern1():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		evidence=[]
		que3dic={'1':'p_18','2':'p_19','3':'p_24','4':'p_22'}
		que4dic={'1':'p_23','2':'p_17','3':'p_16','4':'p_20','5':'p_21'}
		quelassym={'1':'s_15','2':'s_16','3':'s_17','4':'s_18','5':'s_19','6':'s_20','7':'s_21','8':'s_24'}
		quefevdic={'1':'p_25','2':'p_26','3':'p_27','4':'p_11','5':'p_15'}
		queyesdic={'yes':'present','no':'absent'}
		que1=header['que1'].lower()
		que2=int(header['que2'])
		que3=header['que3'].split(' ')
		if '5' in que3:
			for i in que3dic.keys():
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		else:
			for i in que3dic.keys():
				if i in que3:
					evidence.append({"id":que3dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		que4=header['que4'].split(' ')
		if '6' in que4:
			for i in que4dic.keys():
					evidence.append({"id":que4dic[i],"choice_id":"absent"})	
		else:		
			for i in que4dic.keys():
				if i in que4:
					evidence.append({"id":que4dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que4dic[i],"choice_id":"absent"})
		evidence.append({"id":"s_0","choice_id":"absent"})
		evidence.append({"id":"s_1","choice_id":"absent"})
		evidence.append({"id":"s_2","choice_id":"absent"})
		que9=header['que8'].split(' ')
		if '9' in que9:
			for i in quelassym.keys():
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		else:
			for i in quelassym.keys():
				if i in que9:
					evidence.append({"id":quelassym[i],"choice_id":"present"})
				else:
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		que10=header['que9'].split(' ')
		for i in quefevdic.keys():
			if i in que10:
				evidence.append({"id":quefevdic[i],"choice_id":"present"})
			else:
				evidence.append({"id":quefevdic[i],"choice_id":"absent"})
		url = 'https://api.infermedica.com/covid19/triage'
		payload = {
   			"sex":que1,
   			 "age":que2,
   			 "evidence":evidence
		}
		print(payload)
		headers = {'App-Id':'70e4261c','App-Key':'0cba344e8edc716155d8dce3393fcf52'}
		r = requests.post(url,json=payload,headers=headers)
		data=r.json()
		print(data)
		if data["triage_level"]=="quarantine":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/3-1.png[/img]"
			message+="[b]Quarantine[/b]"
		elif data["triage_level"]=="no_risk":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/1-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif  data["triage_level"]=="self_monitoring":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/2-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif data["triage_level"]=="isolation_call":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/4-1.png[/img]"
			message+="[b] Consult health care provider. Avoid all contact.[/b]"			
		elif data["triage_level"]=="call_doctor":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/5-1.png[/img]"
			message+="[b]Call a doctor, symptoms might not be directly linked to COVID-19.[/b]"	
		else:
			message="[img]https://50hands.org/wp-content/uploads/2020/06/6-1.png[/img]"
			message+="[b]Call the emergency number. Avoid all contact[/b]"
		message+=data['description']+"\n"
		if len(data['serious'])>0:
			message+='[b]Alarming Symptoms[/b]'
		for i in data['serious']:
			message+="\n"+i["common_name"]
		message+="::next-1::"
		if data["triage_level"]=="quarantine":
			message+="[b]Quarantine[/b]"
			message+="\nChoose a well-ventilated separate room, or if a single separate room is not possible, please maintain a distance of at least 2 meters (6 feet) from other household members and minimize the usage of shared spaces like a kitchen or bathroom. Remember to stock adequate provisions and medication for the quarantine period. For your comfort, ensure that you have access to the Internet, news, and entertainment. While under quarantine, communication with family and friends on the outside is important in maintaining good mental health during what can be for some a difficult time. Quarantine usually is for 14 days, starting from the last day of exposure to the virus."
			message+="::next-1::"
			message+="[b]Cough and sneeze properly[/b]"
			message+="\nCover your mouth and nose with a tissue when you are about to cough or sneeze.\n"
			message+="Throw the used tissue out into a bin lined with a trash bag.\n"
			message+="Disinfect your hands afterward with an alcohol-based rub containing a minimum of 60percent of alcohol, or wash your hands with soap and water for a minimum of 20 seconds."
			message+="::next-1::"
			message+="[b]Wash your hands often[/b]"
			message+="\nYour hands are a carrier for the coronavirus. Every time you touch your face area, cough into your palms, or go to the toilet, your hands become contaminated and spread the virus to everything you come into contact with. It is crucial, for the safety of your household members, that you clean your hands regularly with soap and water or an alcohol-based rub."
			message+="::next-1::"
			message+="[b]Monitor Your Symptoms[/b]"
			message+="\nPlease monitor your health several times a day. If it is possible, keep a thermometer in your isolation place and monitor your temperature every couple of hours. Repeat this checkup, if you notice any new symptoms."
			message+="\nWhen should you call 112 or your local emergency number?\n"
			message+="You have trouble breathing.\nYour fever climbs over high (over 40°C, 104°F).\nYour health is getting worse.\nTell health personnel that you are being evaluated for COVID-19. Put on a surgical face mask prior to their arrival."
		elif data["triage_level"]=="no_risk" or data["triage_level"]=="self_monitoring" or data["triage_level"]=="isolation_call" or data["triage_level"]=="call_doctor":
			message+="::next-1::"
			message+="[b]Maintain strict hygiene[/b]\n"
			message+="It is strongly recommended for you to take simple precautions that can reduce your chances of becoming infected in the future or of spreading the virus: \n• Regularly and thoroughly clean your hands with an alcohol-based hand sanitizer or wash them with soap and water for at least 20 seconds. \n • Avoid touching your eyes, nose and mouth. • Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. • Disinfect your hands after sneezing. \n • Do not share your cups, plates, cutlery and other household utensils with family members. "
			message+="::next-1::"
			message+="[b]Maintain social distancing [/b]\n"
			message+="• Maintain a distance of at least 1 meter (3 feet) between yourself and others, even if they are not exhibiting symptoms of COVID-19. \n• Avoid traveling — especially if you are an older person or have a condition such as diabetes, heart or lung disease. "
			message+="::next-1::"
			message+="[b]Monitor your health [/b]\n"
			message+="ou are strongly advised to regularly use this diagnostic tool, particularly should your circumstances change, such as the occurrence of new symptoms or contact with an infected person. "
		else:
			message+="::next-1::"
			message+="[b]Immediately separate yourself from people and pets in your house [/b]\n"
			message+="If possible, isolate yourself in a separate room, away from other members of your household. If this is not possible, keep a distance of at least 1 meter from others and wear a protective surgical mask. Avoid all interaction with household pets. "
			message+="::next-1::"
			message+="[b]Call the emergency number [/b]\n"
			message+="Call the emergency number of your country. Your symptoms are severe and you may need to be transported to a medical facility. "
			message+="::next-1::"
			message+="[b]Wear a surgical face mask[/b]\n"
			message+="Put on a surgical face mask whenever somebody is about to enter the same room or vehicle as you. Put on a surgical face mask before entering an ambulance or medical facility. People interacting with you should wear face masks as well, particularly if you have difficulty breathing. "
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/covid/pattern2', methods=['POST','GET'])
def despattern2():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		evidence=[]
		que3dic={'1':'p_18','2':'p_19','3':'p_24','4':'p_22'}
		que4dic={'1':'p_23','2':'p_17','3':'p_16','4':'p_20','5':'p_21'}
		quelassym={'1':'s_15','2':'s_16','3':'s_17','4':'s_18','5':'s_19','6':'s_20','7':'s_21','8':'s_24'}
		quefevdic={'1':'p_25','2':'p_26','3':'p_27','4':'p_11','5':'p_15'}
		queyesdic={'yes':'present','no':'absent'}
		que1=header['que1'].lower()
		que2=int(header['que2'])
		que3=header['que3'].split(' ')
		if '5' in que3:
			for i in que3dic.keys():
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		else:
			for i in que3dic.keys():
				if i in que3:
					evidence.append({"id":que3dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		que4=header['que4'].split(' ')
		if '6' in que4:
			for i in que4dic.keys():
					evidence.append({"id":que4dic[i],"choice_id":"absent"})	
		else:		
			for i in que4dic.keys():
				if i in que4:
					evidence.append({"id":que4dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que4dic[i],"choice_id":"absent"})
		evidence.append({"id":"s_0","choice_id":"present"})
		evidence.append({"id":"s_1","choice_id":queyesdic[header['que6']]})
		evidence.append({"id":"s_2","choice_id":queyesdic[header['que7']]})
		que8=header['que8']
		if que8=="Between 37.5°C and 38°C (99.5°F and 100.4°F)":
			evidence.append({"id":"s_22","choice_id":"present"})
		elif que8=="Between 38°C and 40°C (100.4°F and 104°F)":
			evidence.append({"id":"s_23","choice_id":"present"})
		elif que8=="Over 40°C (104°F)":
			evidence.append({"id":"s_4","choice_id":"present"})
		else:
			evidence.append({"id":"s_5","choice_id":"present"})
		que9=header['que9']
		if que9=='yes':
			evidence.append({"id":"s_12","choice_id":"present"})
		else:
			evidence.append({"id":"s_12","choice_id":"absent"})
		que10=header['que10']
		if que10=='yes':
			evidence.append({"id":"s_13","choice_id":"present"})
		else:
			evidence.append({"id":"s_13","choice_id":"absent"})
		que11=header['que11']
		if que11=='yes':
			evidence.append({"id":"s_14","choice_id":"present"})
		else:
			evidence.append({"id":"s_14","choice_id":"absent"})
		que12=header['que12'].split(' ')
		if '9' in que12:
			for i in quelassym.keys():
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		else:
			for i in quelassym.keys():
				if i in que12:
					evidence.append({"id":quelassym[i],"choice_id":"present"})
				else:
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		que13=header['que13'].split(' ')
		for i in quefevdic.keys():
			if i in que13:
				evidence.append({"id":quefevdic[i],"choice_id":"present"})
			else:
				evidence.append({"id":quefevdic[i],"choice_id":"absent"})
		url = 'https://api.infermedica.com/covid19/triage'
		payload = {
   			"sex":que1,
   			 "age":que2,
   			 "evidence":evidence
		}
		print(payload)
		headers = {'App-Id':'70e4261c','App-Key':'0cba344e8edc716155d8dce3393fcf52'}
		r = requests.post(url,json=payload,headers=headers)
		data=r.json()
		print(data)
		if data["triage_level"]=="quarantine":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/3-1.png[/img]"
			message+="[b]Quarantine[/b]"
		elif data["triage_level"]=="no_risk":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/1-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif  data["triage_level"]=="self_monitoring":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/2-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif data["triage_level"]=="isolation_call":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/4-1.png[/img]"
			message+="[b] Consult health care provider. Avoid all contact.[/b]"			
		elif data["triage_level"]=="call_doctor":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/5-1.png[/img]"
			message+="[b]Call a doctor, symptoms might not be directly linked to COVID-19.[/b]"	
		else:
			message="[img]https://50hands.org/wp-content/uploads/2020/06/6-1.png[/img]"
			message+="[b]Call the emergency number. Avoid all contact[/b]"
		message+=data['description']+"\n"
		if len(data['serious'])>0:
			message+='[b]Alarming Symptoms[/b]'
		for i in data['serious']:
			message+="\n"+i["common_name"]
		message+="::next-1::"
		if data["triage_level"]=="quarantine":
			message+="[b]Quarantine[/b]"
			message+="\nChoose a well-ventilated separate room, or if a single separate room is not possible, please maintain a distance of at least 2 meters (6 feet) from other household members and minimize the usage of shared spaces like a kitchen or bathroom. Remember to stock adequate provisions and medication for the quarantine period. For your comfort, ensure that you have access to the Internet, news, and entertainment. While under quarantine, communication with family and friends on the outside is important in maintaining good mental health during what can be for some a difficult time. Quarantine usually is for 14 days, starting from the last day of exposure to the virus."
			message+="::next-1::"
			message+="[b]Cough and sneeze properly[/b]"
			message+="\nCover your mouth and nose with a tissue when you are about to cough or sneeze.\n"
			message+="Throw the used tissue out into a bin lined with a trash bag.\n"
			message+="Disinfect your hands afterward with an alcohol-based rub containing a minimum of 60percent of alcohol, or wash your hands with soap and water for a minimum of 20 seconds."
			message+="::next-1::"
			message+="[b]Wash your hands often[/b]"
			message+="\nYour hands are a carrier for the coronavirus. Every time you touch your face area, cough into your palms, or go to the toilet, your hands become contaminated and spread the virus to everything you come into contact with. It is crucial, for the safety of your household members, that you clean your hands regularly with soap and water or an alcohol-based rub."
			message+="::next-1::"
			message+="[b]Monitor Your Symptoms[/b]"
			message+="\nPlease monitor your health several times a day. If it is possible, keep a thermometer in your isolation place and monitor your temperature every couple of hours. Repeat this checkup, if you notice any new symptoms."
			message+="\nWhen should you call 112 or your local emergency number?\n"
			message+="You have trouble breathing.\nYour fever climbs over high (over 40°C, 104°F).\nYour health is getting worse.\nTell health personnel that you are being evaluated for COVID-19. Put on a surgical face mask prior to their arrival."
		elif data["triage_level"]=="no_risk" or data["triage_level"]=="self_monitoring" or data["triage_level"]=="isolation_call" or data["triage_level"]=="call_doctor":
			message+="::next-1::"
			message+="[b]Maintain strict hygiene[/b]\n"
			message+="It is strongly recommended for you to take simple precautions that can reduce your chances of becoming infected in the future or of spreading the virus: \n• Regularly and thoroughly clean your hands with an alcohol-based hand sanitizer or wash them with soap and water for at least 20 seconds. \n • Avoid touching your eyes, nose and mouth. • Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. • Disinfect your hands after sneezing. \n • Do not share your cups, plates, cutlery and other household utensils with family members. "
			message+="::next-1::"
			message+="[b]Maintain social distancing [/b]\n"
			message+="• Maintain a distance of at least 1 meter (3 feet) between yourself and others, even if they are not exhibiting symptoms of COVID-19. \n• Avoid traveling — especially if you are an older person or have a condition such as diabetes, heart or lung disease. "
			message+="::next-1::"
			message+="[b]Monitor your health [/b]\n"
			message+="ou are strongly advised to regularly use this diagnostic tool, particularly should your circumstances change, such as the occurrence of new symptoms or contact with an infected person. "
		else:
			message+="::next-1::"
			message+="[b]Immediately separate yourself from people and pets in your house [/b]\n"
			message+="If possible, isolate yourself in a separate room, away from other members of your household. If this is not possible, keep a distance of at least 1 meter from others and wear a protective surgical mask. Avoid all interaction with household pets. "
			message+="::next-1::"
			message+="[b]Call the emergency number [/b]\n"
			message+="Call the emergency number of your country. Your symptoms are severe and you may need to be transported to a medical facility. "
			message+="::next-1::"
			message+="[b]Wear a surgical face mask[/b]\n"
			message+="Put on a surgical face mask whenever somebody is about to enter the same room or vehicle as you. Put on a surgical face mask before entering an ambulance or medical facility. People interacting with you should wear face masks as well, particularly if you have difficulty breathing. "
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})
@app.route('/covid/pattern3', methods=['POST','GET'])
def despattern3():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		evidence=[]
		que3dic={'1':'p_18','2':'p_19','3':'p_24','4':'p_22'}
		que4dic={'1':'p_23','2':'p_17','3':'p_16','4':'p_20','5':'p_21'}
		quelassym={'1':'s_15','2':'s_16','3':'s_17','4':'s_18','5':'s_19','6':'s_20','7':'s_21','8':'s_24'}
		quefevdic={'1':'p_25','2':'p_26','3':'p_27','4':'p_11','5':'p_15'}
		queyesdic={'yes':'present','no':'absent'}
		que1=header['que1'].lower()
		que2=int(header['que2'])
		que3=header['que3'].split(' ')
		if '5' in que3:
			for i in que3dic.keys():
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		else:
			for i in que3dic.keys():
				if i in que3:
					evidence.append({"id":que3dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		que4=header['que4'].split(' ')
		if '6' in que4:
			for i in que4dic.keys():
					evidence.append({"id":que4dic[i],"choice_id":"absent"})	
		else:		
			for i in que4dic.keys():
				if i in que4:
					evidence.append({"id":que4dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que4dic[i],"choice_id":"absent"})
		evidence.append({"id":"s_0","choice_id":"absent"})
		evidence.append({"id":"s_1","choice_id":"present"})
		evidence.append({"id":"s_2","choice_id":queyesdic[header['que7']]})
		que9=header['que8']
		if que9=='yes':
			evidence.append({"id":"s_12","choice_id":"present"})
		else:
			evidence.append({"id":"s_12","choice_id":"absent"})
		que10=header['que9']
		if que10=='yes':
			evidence.append({"id":"s_13","choice_id":"present"})
		else:
			evidence.append({"id":"s_13","choice_id":"absent"})
		que11=header['que10']
		if que11=='yes':
			evidence.append({"id":"s_14","choice_id":"present"})
		else:
			evidence.append({"id":"s_14","choice_id":"absent"})
		que12=header['que11'].split(' ')
		if '9' in que12:
			for i in quelassym.keys():
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		else:
			for i in quelassym.keys():
				if i in que12:
					evidence.append({"id":quelassym[i],"choice_id":"present"})
				else:
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		que13=header['que12'].split(' ')
		for i in quefevdic.keys():
			if i in que13:
				evidence.append({"id":quefevdic[i],"choice_id":"present"})
			else:
				evidence.append({"id":quefevdic[i],"choice_id":"absent"})
		url = 'https://api.infermedica.com/covid19/triage'
		payload = {
   			"sex":que1,
   			 "age":que2,
   			 "evidence":evidence
		}
		print(payload)
		headers = {'App-Id':'70e4261c','App-Key':'0cba344e8edc716155d8dce3393fcf52'}
		r = requests.post(url,json=payload,headers=headers)
		data=r.json()
		print(data)
		if data["triage_level"]=="quarantine":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/3-1.png[/img]"
			message+="[b]Quarantine[/b]"
		elif data["triage_level"]=="no_risk":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/1-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif  data["triage_level"]=="self_monitoring":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/2-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif data["triage_level"]=="isolation_call":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/4-1.png[/img]"
			message+="[b] Consult health care provider. Avoid all contact.[/b]"			
		elif data["triage_level"]=="call_doctor":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/5-1.png[/img]"
			message+="[b]Call a doctor, symptoms might not be directly linked to COVID-19.[/b]"	
		else:
			message="[img]https://50hands.org/wp-content/uploads/2020/06/6-1.png[/img]"
			message+="[b]Call the emergency number. Avoid all contact[/b]"
		message+=data['description']+"\n"
		if len(data['serious'])>0:
			message+='[b]Alarming Symptoms[/b]'
		for i in data['serious']:
			message+="\n"+i["common_name"]
		message+="::next-1::"
		if data["triage_level"]=="quarantine":
			message+="[b]Quarantine[/b]"
			message+="\nChoose a well-ventilated separate room, or if a single separate room is not possible, please maintain a distance of at least 2 meters (6 feet) from other household members and minimize the usage of shared spaces like a kitchen or bathroom. Remember to stock adequate provisions and medication for the quarantine period. For your comfort, ensure that you have access to the Internet, news, and entertainment. While under quarantine, communication with family and friends on the outside is important in maintaining good mental health during what can be for some a difficult time. Quarantine usually is for 14 days, starting from the last day of exposure to the virus."
			message+="::next-1::"
			message+="[b]Cough and sneeze properly[/b]"
			message+="\nCover your mouth and nose with a tissue when you are about to cough or sneeze.\n"
			message+="Throw the used tissue out into a bin lined with a trash bag.\n"
			message+="Disinfect your hands afterward with an alcohol-based rub containing a minimum of 60percent of alcohol, or wash your hands with soap and water for a minimum of 20 seconds."
			message+="::next-1::"
			message+="[b]Wash your hands often[/b]"
			message+="\nYour hands are a carrier for the coronavirus. Every time you touch your face area, cough into your palms, or go to the toilet, your hands become contaminated and spread the virus to everything you come into contact with. It is crucial, for the safety of your household members, that you clean your hands regularly with soap and water or an alcohol-based rub."
			message+="::next-1::"
			message+="[b]Monitor Your Symptoms[/b]"
			message+="\nPlease monitor your health several times a day. If it is possible, keep a thermometer in your isolation place and monitor your temperature every couple of hours. Repeat this checkup, if you notice any new symptoms."
			message+="\nWhen should you call 112 or your local emergency number?\n"
			message+="You have trouble breathing.\nYour fever climbs over high (over 40°C, 104°F).\nYour health is getting worse.\nTell health personnel that you are being evaluated for COVID-19. Put on a surgical face mask prior to their arrival."
		elif data["triage_level"]=="no_risk" or data["triage_level"]=="self_monitoring" or data["triage_level"]=="isolation_call" or data["triage_level"]=="call_doctor":
			message+="::next-1::"
			message+="[b]Maintain strict hygiene[/b]\n"
			message+="It is strongly recommended for you to take simple precautions that can reduce your chances of becoming infected in the future or of spreading the virus: \n• Regularly and thoroughly clean your hands with an alcohol-based hand sanitizer or wash them with soap and water for at least 20 seconds. \n • Avoid touching your eyes, nose and mouth. • Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. • Disinfect your hands after sneezing. \n • Do not share your cups, plates, cutlery and other household utensils with family members. "
			message+="::next-1::"
			message+="[b]Maintain social distancing [/b]\n"
			message+="• Maintain a distance of at least 1 meter (3 feet) between yourself and others, even if they are not exhibiting symptoms of COVID-19. \n• Avoid traveling — especially if you are an older person or have a condition such as diabetes, heart or lung disease. "
			message+="::next-1::"
			message+="[b]Monitor your health [/b]\n"
			message+="ou are strongly advised to regularly use this diagnostic tool, particularly should your circumstances change, such as the occurrence of new symptoms or contact with an infected person. "
		else:
			message+="::next-1::"
			message+="[b]Immediately separate yourself from people and pets in your house [/b]\n"
			message+="If possible, isolate yourself in a separate room, away from other members of your household. If this is not possible, keep a distance of at least 1 meter from others and wear a protective surgical mask. Avoid all interaction with household pets. "
			message+="::next-1::"
			message+="[b]Call the emergency number [/b]\n"
			message+="Call the emergency number of your country. Your symptoms are severe and you may need to be transported to a medical facility. "
			message+="::next-1::"
			message+="[b]Wear a surgical face mask[/b]\n"
			message+="Put on a surgical face mask whenever somebody is about to enter the same room or vehicle as you. Put on a surgical face mask before entering an ambulance or medical facility. People interacting with you should wear face masks as well, particularly if you have difficulty breathing. "
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})	
@app.route('/covid/pattern4', methods=['POST','GET'])
def despattern4():
	try:
		json_ = request.args
		header=request.headers
		print(header)
		evidence=[]
		que3dic={'1':'p_18','2':'p_19','3':'p_24','4':'p_22'}
		que4dic={'1':'p_23','2':'p_17','3':'p_16','4':'p_20','5':'p_21'}
		quelassym={'1':'s_15','2':'s_16','3':'s_17','4':'s_18','5':'s_19','6':'s_20','7':'s_21','8':'s_24'}
		quefevdic={'1':'p_25','2':'p_26','3':'p_27','4':'p_11','5':'p_15'}
		queyesdic={'yes':'present','no':'absent'}
		que1=header['que1'].lower()
		que2=int(header['que2'])
		que3=header['que3'].split(' ')
		if '5' in que3:
			for i in que3dic.keys():
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		else:
			for i in que3dic.keys():
				if i in que3:
					evidence.append({"id":que3dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que3dic[i],"choice_id":"absent"})
		que4=header['que4'].split(' ')
		if '6' in que4:
			for i in que4dic.keys():
					evidence.append({"id":que4dic[i],"choice_id":"absent"})	
		else:		
			for i in que4dic.keys():
				if i in que4:
					evidence.append({"id":que4dic[i],"choice_id":"present"})
				else:
					evidence.append({"id":que4dic[i],"choice_id":"absent"})
		evidence.append({"id":"s_0","choice_id":"absent"})
		evidence.append({"id":"s_1","choice_id":"absent"})
		evidence.append({"id":"s_2","choice_id":queyesdic[header['que7']]})
		que9=header['que8']
		if que9=='yes':
			evidence.append({"id":"s_12","choice_id":"present"})
		else:
			evidence.append({"id":"s_12","choice_id":"absent"})
		que10=header['que9']
		if que10=='yes':
			evidence.append({"id":"s_13","choice_id":"present"})
		else:
			evidence.append({"id":"s_13","choice_id":"absent"})
		que11=header['que10']
		if que11=='yes':
			evidence.append({"id":"s_14","choice_id":"present"})
		else:
			evidence.append({"id":"s_14","choice_id":"absent"})
		que12=header['que11'].split(' ')
		if '9' in que12:
			for i in quelassym.keys():
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		else:
			for i in quelassym.keys():
				if i in que12:
					evidence.append({"id":quelassym[i],"choice_id":"present"})
				else:
					evidence.append({"id":quelassym[i],"choice_id":"absent"})
		que13=header['que12'].split(' ')
		for i in quefevdic.keys():
			if i in que13:
				evidence.append({"id":quefevdic[i],"choice_id":"present"})
			else:
				evidence.append({"id":quefevdic[i],"choice_id":"absent"})
		url = 'https://api.infermedica.com/covid19/triage'
		payload = {
   			"sex":que1,
   			 "age":que2,
   			 "evidence":evidence
		}
		print(payload)
		headers = {'App-Id':'70e4261c','App-Key':'0cba344e8edc716155d8dce3393fcf52'}
		r = requests.post(url,json=payload,headers=headers)
		data=r.json()
		print(data)
		if data["triage_level"]=="quarantine":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/3-1.png[/img]"
			message+="[b]Quarantine[/b]"
		elif data["triage_level"]=="no_risk":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/1-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif  data["triage_level"]=="self_monitoring":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/2-1.png[/img]"
			message+="[b]Follow preventive measures.[/b]"
		elif data["triage_level"]=="isolation_call":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/4-1.png[/img]"
			message+="[b] Consult health care provider. Avoid all contact.[/b]"			
		elif data["triage_level"]=="call_doctor":
			message="[img]https://50hands.org/wp-content/uploads/2020/06/5-1.png[/img]"
			message+="[b]Call a doctor, symptoms might not be directly linked to COVID-19.[/b]"	
		else:
			message="[img]https://50hands.org/wp-content/uploads/2020/06/6-1.png[/img]"
			message+="[b]Call the emergency number. Avoid all contact[/b]"
		message+=data['description']+"\n"
		if len(data['serious'])>0:
			message+='[b]Alarming Symptoms[/b]'
		for i in data['serious']:
			message+="\n"+i["common_name"]
		message+="::next-1::"
		if data["triage_level"]=="quarantine":
			message+="[b]Quarantine[/b]"
			message+="\nChoose a well-ventilated separate room, or if a single separate room is not possible, please maintain a distance of at least 2 meters (6 feet) from other household members and minimize the usage of shared spaces like a kitchen or bathroom. Remember to stock adequate provisions and medication for the quarantine period. For your comfort, ensure that you have access to the Internet, news, and entertainment. While under quarantine, communication with family and friends on the outside is important in maintaining good mental health during what can be for some a difficult time. Quarantine usually is for 14 days, starting from the last day of exposure to the virus."
			message+="::next-1::"
			message+="[b]Cough and sneeze properly[/b]"
			message+="\nCover your mouth and nose with a tissue when you are about to cough or sneeze.\n"
			message+="Throw the used tissue out into a bin lined with a trash bag.\n"
			message+="Disinfect your hands afterward with an alcohol-based rub containing a minimum of 60percent of alcohol, or wash your hands with soap and water for a minimum of 20 seconds."
			message+="::next-1::"
			message+="[b]Wash your hands often[/b]"
			message+="\nYour hands are a carrier for the coronavirus. Every time you touch your face area, cough into your palms, or go to the toilet, your hands become contaminated and spread the virus to everything you come into contact with. It is crucial, for the safety of your household members, that you clean your hands regularly with soap and water or an alcohol-based rub."
			message+="::next-1::"
			message+="[b]Monitor Your Symptoms[/b]"
			message+="\nPlease monitor your health several times a day. If it is possible, keep a thermometer in your isolation place and monitor your temperature every couple of hours. Repeat this checkup, if you notice any new symptoms."
			message+="\nWhen should you call 112 or your local emergency number?\n"
			message+="You have trouble breathing.\nYour fever climbs over high (over 40°C, 104°F).\nYour health is getting worse.\nTell health personnel that you are being evaluated for COVID-19. Put on a surgical face mask prior to their arrival."
		elif data["triage_level"]=="no_risk" or data["triage_level"]=="self_monitoring" or data["triage_level"]=="isolation_call" or data["triage_level"]=="call_doctor":
			message+="::next-1::"
			message+="[b]Maintain strict hygiene[/b]\n"
			message+="It is strongly recommended for you to take simple precautions that can reduce your chances of becoming infected in the future or of spreading the virus: \n• Regularly and thoroughly clean your hands with an alcohol-based hand sanitizer or wash them with soap and water for at least 20 seconds. \n • Avoid touching your eyes, nose and mouth. • Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze. • Disinfect your hands after sneezing. \n • Do not share your cups, plates, cutlery and other household utensils with family members. "
			message+="::next-1::"
			message+="[b]Maintain social distancing [/b]\n"
			message+="• Maintain a distance of at least 1 meter (3 feet) between yourself and others, even if they are not exhibiting symptoms of COVID-19. \n• Avoid traveling — especially if you are an older person or have a condition such as diabetes, heart or lung disease. "
			message+="::next-1::"
			message+="[b]Monitor your health [/b]\n"
			message+="ou are strongly advised to regularly use this diagnostic tool, particularly should your circumstances change, such as the occurrence of new symptoms or contact with an infected person. "
		else:
			message+="::next-1::"
			message+="[b]Immediately separate yourself from people and pets in your house [/b]\n"
			message+="If possible, isolate yourself in a separate room, away from other members of your household. If this is not possible, keep a distance of at least 1 meter from others and wear a protective surgical mask. Avoid all interaction with household pets. "
			message+="::next-1::"
			message+="[b]Call the emergency number [/b]\n"
			message+="Call the emergency number of your country. Your symptoms are severe and you may need to be transported to a medical facility. "
			message+="::next-1::"
			message+="[b]Wear a surgical face mask[/b]\n"
			message+="Put on a surgical face mask whenever somebody is about to enter the same room or vehicle as you. Put on a surgical face mask before entering an ambulance or medical facility. People interacting with you should wear face masks as well, particularly if you have difficulty breathing. "
		response={
		 'message':message
		}
		python2json = json.dumps(response)
		return python2json
	except:
		return jsonify({'trace': traceback.format_exc()})			
if __name__=='__main__':
    app.run(debug=True)
