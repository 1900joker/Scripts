from flask import Flask, request, Response , jsonify
from pprint import pprint
import json

app = Flask(__name__)

#Models
class Product:
	def __init__(self,productId,price,url):
		self.productId = productId
		self.price = price
		self.url = url
		self.ALWAYS = []            # sets can be used here
		self.ALL_TIME_LOW = []      # sets can be used here
		self.MORE_THAN_10 = []      # sets can be used here
		self.MINIMUM = price

	def getListforReson(self,users,r):
		reason = ['ALWAYS','MORE_THAN_10','ALL_TIME_LOW']
		notifications = []
		for d in users:
			notification = Notification(self.productId,self.price,self.url,reason[r])
			notifications.append(notification)
		return notifications

	def getNotificationsList(self,nPrice):
		always_notify = []
		all_time_low_notify = []
		more_then_10_notify = []
		notifications = []
		
		if self.price > nPrice:
			always_notify = set(self.ALWAYS)
		if 0.90 * self.price > nPrice:
			more_then_10_notify = set(self.MORE_THAN_10)
		if nPrice < self.MINIMUM:
			all_time_low_notify = set(self.ALL_TIME_LOW)

		always_notify = set(always_notify) - set(more_then_10_notify) - set(all_time_low_notify)
		more_then_10_notify = set(more_then_10_notify) - set(all_time_low_notify)

		self.price = nPrice 

		notifications.extend(self.getListforReson(always_notify,0))
		notifications.extend(self.getListforReson(more_then_10_notify,1))
		notifications.extend(self.getListforReson(all_time_low_notify,2))

	

		return notifications

class Notification:
	def __init__(self,productId,price,url,reason):
		self.productId = productId
		self.price = price
		self.url = url
		self.reason = reason 

#Controller

products = {}

def updateProduct(product):
	notifications = {}
	if product.productId in products.keys():
		oldproduct = products[product.productId]
		notifications = oldproduct.getNotificationsList(product.price)
	else:
		products[product.productId] = product
	return notifications

def subscribeUser(userJson):
	user_id = int(userJson.get('user_id'))
	subscribe = userJson.get('subscribe')
	for data in subscribe:
		productId = int(data.get('product_id'))
		when = data.get('when')
		if when == "ALWAYS":
			products[productId].ALWAYS.append(user_id)
		elif when == "ALL_TIME_LOW":
			products[productId].ALL_TIME_LOW.append(user_id)
		else:
			products[productId].MORE_THAN_10.append(user_id)

def unsubscribeUser(userJson):
	user_id = int(userJson.get('user_id'))
	unsubscribe = userJson.get('unsubscribe')
	for data in unsubscribe:
		productId = int(data.get('product_id'))
		try:
			products[productId].ALWAYS.remove(user_id)
			products[productId].ALL_TIME_LOW.remove(user_id)
			products[productId].MORE_THAN_10.remove(user_id)
		except ValueError:
			pass 

#API
@app.route("/subscribe", methods=['POST'])
def subscribe():
	if request.json:
		subscribeUser(request.json)
		return jsonify(**request.json)
	else:
		return ""

@app.route("/unsubscribe", methods=['POST'])
def unsubscribe():
	if request.json:
		unsubscribeUser(request.json)
		return jsonify(**request.json)
	else:
		return ""

@app.route("/priceDataPoint", methods=['POST'])
def priceDataPoint():
	if request.json:
		productId = int(request.json.get('product_id'))
		price = float(request.json.get('price'))
		url = request.json.get('url')
		product = Product(productId,price,url)
		notifications = updateProduct(product)
		return json.dumps([notification.__dict__ for notification in notifications])
	else:
		return ""

if __name__ == "__main__":
	app.debug = True
	app.run()