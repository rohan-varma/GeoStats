import csv
median_income_list = []
f = open("demographic_data/median_income.csv")
csv_f = csv.reader(f)
x = 0
for r in csv_f:
	if(x!=13):
		median_income_list.append(r[1]) # prints the  and median income (alpha order)
	x = x+1
print median_income_list[5:]

state_list_str = "AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY"


state_list = state_list_str.split()
new_state_list = []
for item in state_list:
	new_state_list.append("US-" + item)
print new_state_list

g = open("demographic_data/race_percent.csv")
race_percent_list = []
csv_g = csv.reader(g)
y = 0
for r in csv_g:
	if (y!=13):
		race_percent_list.append(r[1:5])
	y = y + 1
print race_percent_list[5:]



#compute real lists

real_median_income = median_income_list[5:]
print len(real_median_income)
print len(state_list)
real_race_percent_list = race_percent_list[5:]
non_NA_race_list = []
for r in real_race_percent_list:
	sublist = [] 
	for x in xrange(0,4):
		if r[x]== 'N/A':
			sublist.append(0)
		else:
			sublist.append(r[x])
	non_NA_race_list.append(sublist)

print non_NA_race_list

print '[\'State\', \'Race distrubution\', \'median income \'],'
string_var = ""
for i in xrange(0,49):

	print '[' + '\'' + new_state_list[i] + '\''+ ',' + real_median_income[i] + '],'

print '[' + '\'' + new_state_list[49] + '\''+ ',' + real_median_income[49] + ']'

	# GOAL STRING:

	# ['State', 'Race distrubution', "median income "], 
 #    ['US-IL', 200, 12],
 #    ['US-IN', 300, 22],
 #    ['US-IA', 20,456],
 #    ['US-RI', 150,0], #last one has no comma
