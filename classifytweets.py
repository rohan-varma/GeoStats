#dictionary: key is string, value is weight
import re
import collections
#dict = { "sanders": 5, "bad": 3} something like this
unimportant = ["berniesanders","for","will","is","be","this","a","the","very","bernie","sanders",
			"an","he","it","our","some","few","i","in","and", "you","that","to","of","Bernie", "Sanders"
			"we","has","his","if","as","do","have", "rt"]
def clean_punc(str):
	cleaned = ""
	punctuation = ''':;[]{}\,'"<>./?~!@#$%^&*()_''' #possible punctuation chars
	for x in xrange(len(str)):
		if str[x] not in punctuation or str[x]==" ":
			cleaned = cleaned + str[x]
	return cleaned.lower() #string without punctuation

def clean(str):
	if str[0]=="@":
		str = str[str.find(" ")+1:]
	str = clean_punc(str)
	words = str.split()
	li = []
	for word in words:

		word = word.lower()
		if word in unimportant:
			li.append(word)
	new_str = ""
	for word in words:
		if word not in li:
			new_str+=word
			new_str+=" "
	return new_str

#Gets rid of @user_name in the tweet
def clean_handle(str):

	while(str[0] != ' '):

		str = str[1:]
	
	return str

def count_occurences(arr):

	#counts the occurences of all words in this array of string, after cleaning them
	count = collections.Counter()
	for str in arr:
		str = clean(str)
		for word in str.split():
			count[word] = count[word] + 1
	return dict(count)

#Gets the weight(popularity) of positive words 
def get_weight_pos(x):
	if x<=2:
		return 1
	if x>=2 and x<=4:
		return 2.3
	if x>4 and x<=6:
		return 4.1
	else:
		return 6.5

#Gets the weight(popularity) of negative words
# def get_weight_neg(x):
# 	if x<=2:
# 		return -1
# 	if x>=2 and x<=4:
# 		return -2.3
# 	if x>4 and x<=6:
# 		return -4.1
# 	else:
# 		return -6.5

if __name__ == '__main__':
	#init it
	str1 = "a bernie sanders presidency will be very bad for our country"
	str2 = "a sanders presidency will be good for the nation"
	arr = open('bad_tweets.txt').readlines()
	#to do - tweets it now a json file, so figure out how to parse that
	new_arr = []
	for item in arr:
		if item!="\n":
			new_arr.append(item)
	#print len(new_arr)
	for x in new_arr:
		x = clean(x)
	import operator
	d = count_occurences(new_arr)
	list = []
	for num in d.values():
		list.append( (get_weight_pos(num)))
	new_dict = dict(zip(d.keys(),list))
	sorted_x = sorted(new_dict.items(),key=operator.itemgetter(1))
	print sorted_x
	# str1 = clean(str1)
	# str2 = clean(str2)
	# print str1
	# print str2










