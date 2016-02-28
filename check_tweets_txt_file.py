import json
fN = "tweets.json"
data = []
with open(fN,'r') as f:
	for line in f:
		data.append(json.loads(line))
print data[0]['user']['location']
