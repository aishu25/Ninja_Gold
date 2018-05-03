from flask import Flask, session, request, render_template, redirect
import random 
from datetime import datetime

ninja = Flask(__name__)
ninja.secret_key = "Thisissecret"

@ninja.route('/')
def update():
	if "gold" not in session:
		session["gold"] = 0
	if "activities" not in session:
		session["activities"] = []

	return render_template('ninjagold.html', gold=session["gold"], activities=session["activities"])

@ninja.route('/process_money', methods=["POST"])
def process():
	
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	
	value = request.form["building"]
	# print value
	earn_farm = random.randrange(10,21)
	earn_cave = random.randrange(5,11)
	earn_house = random.randrange(2,6)
	earn_casino = random.randrange(-50,51)
	# message = ""
	if (value == "Farm"):
		session["gold"] += earn_farm
		session["activities"].append(["earn", "You have won %d gold from the %s! %s" % (earn_farm, value, timestamp)]) 
		print earn_farm
	elif (value == "Cave"):
		session["gold"] += earn_cave
		session["activities"].append(["earn", "You have won %d gold from the %s! %s\n" % (earn_cave, value, timestamp)])
		print earn_farm
	elif (value == "House"):
		session["gold"] += earn_house
		session["activities"].append(["earn", "You have won %d gold from the %s! %s\n" % (earn_house, value, timestamp)])
		print earn_farm
	elif (value == "Casino"):
		session["gold"] += earn_casino

		if(earn_casino > 0):
			session["activities"].append(["earn", "You have won %d gold from the %s! %s\n" % (earn_casino, value, timestamp)])
		elif(earn_casino < 0):
			session["activities"].append(["lost", "You have lost %d gold from the %s! %s\n" % (abs(earn_casino), value, timestamp)])
		else:
			session["activities"].append(["breakeven", "You broke even at the Casino! %s\n" % (timestamp)])
		print earn_farm
	
	return redirect('/')
@ninja.route('/restart', methods=['POST'])
def restart():
	session.clear()
	return redirect('/')
	


ninja.run(debug=True)
