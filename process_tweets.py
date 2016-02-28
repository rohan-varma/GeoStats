from nltk.tokenize import word_tokenize
import re
import json
import collections

#define some things we want to save as single tokens

negative_words = [('socialist', -6.5), ('not', -6.5), ('all', -4.1), ('what', -4.1), ('dont', -4.1), ('who', -4.1), ('we', -4.1), ('people', -4.1), ('about', -4.1), ('democrat', -2.3), ('revolution', -2.3), ('usa', -2.3), ('me', -2.3), ('can', -2.3), ('how', -2.3), ('president', -2.3), ('man', -2.3), ('happen', -2.3), ('reparations', -2.3), ('think', -2.3), ('john', -2.3), ('too', -2.3), ('obama', -2.3), ('america', -2.3), ('lewis', -2.3), ('should', -2.3), ('black', -2.3), ('college', -2.3), ('are', -2.3), ('said', -2.3), ('job', -2.3), ('wants', -2.3), ('those', -2.3), ('socialism', -2.3), ('cant', -2.3), ('off', -2.3), ('money', -2.3), ('yes', -2.3), ('real', -2.3), ('by', -2.3), ('on', -2.3), ('would', -2.3), ('or', -2.3), ('your', -2.3), ('support', -2.3), ('up', -2.3), ('us', -2.3), ('when', -2.3), ('todays', -1), ('lack', -1), ('billhemmer', -1), ('go', -1), ('voter', -1), ('tf', -1), ('sorry', -1), ('billionaire', -1), ('wipe', -1), ('redistribute', -1), ('deficient', -1), ('cause', -1), ('1996', -1), ('minimao', -1), ('creditcarddebt', -1), ('guy', -1), ('capitalist', -1), ('wordstough', -1), ('says', -1), ('street', -1), ('misrepresent', -1), ('depression', -1), ('even', -1), ('constitution', -1), ('chicago', -1), ('new', -1), ('harassing', -1), ('nazis', -1), ('told', -1), ('led', -1), ('stance', -1), ('never', -1), ('let', -1), ('others', -1), ('strong', -1), ('involved', -1), ('study', -1), ('economics', -1), ('allows', -1), ('social', -1), ('patriotic', -1), ('love', -1), ('put', -1), ('from', -1), ('wealth', -1), ('bush', -1), ('live', -1), ('call', -1), ('he\xe2\x80\x99s', -1), ('until', -1), ('today', -1), ('more', -1), ('separated', -1), ('successful', -1), ('hmmmthis', -1), ('phone', -1), ('reallyreallyreally', -1), ('hold', -1), ('keeping', -1), ('word', -1), ('deserved', -1), ('f', -1), ('work', -1), ('learn', -1), ('didnt', -1), ('heart', -1), ('trump', -1), ('process', -1), ('tax', -1), ('numbers', -1), ('want', -1), ('times', -1), ('aging', -1), ('needs', -1), ('rather', -1), ('chops', -1), ('endorsement', -1), ('interview', -1), ('reestablish', -1), ('economy', -1), ('fascist', -1), ('after', -1), ('guys', -1), ('remember', -1), ('lines', -1), ('sickening', -1), ('so', -1), ('agenda', -1), ('pay', -1), ('sc', -1), ('democratic', -1), ('over', -1), ('giveme', -1), ('isnt', -1), ('unite', -1), ('wud', -1), ('hell', -1), ('still', -1), ('interesting', -1), ('masses', -1), ('late', -1), ('willing', -1), ('policy', -1), ('dolls', -1), ('then', -1), ('non', -1), ('someone', -1), ('yo', -1), ('safe', -1), ('educating', -1), ('they', -1), ('hands', -1), ('yr', -1), ('rhetoric', -1), ('grammar', -1), ('name', -1), ('slavery', -1), ('inequality', -1), ('truth', -1), ('went', -1), ('mean', -1), ('financial', -1), ('house', -1), ('hard', -1), ('manifesto', -1), ('event', -1), ('out', -1), ('blacks', -1), ('activism', -1), ('looking', -1), ('bailout', -1), ('issue', -1), ('working', -1), ('payroll', -1), ('free', -1), ('completely', -1), ('ask', -1), ('teach', -1), ('wanted', -1), ('benefits', -1), ('starts', -1), ('could', -1), ('keep', -1), ('american', -1), ('massive', -1), ('first', -1), ('embraces', -1), ('already', -1), ('primary', -1), ('one', -1), ('done', -1), ('another', -1), ('vote', -1), ('sounds', -1), ('millions', -1), ('olds', -1), ('deceptive', -1), ('jew', -1), ('system', -1), ('anyone', -1), ('2', -1), ('rates', -1), ('listed', -1), ('just', -1), ('white', -1), ('really', -1), ('wblood', -1), ('took', -1), ('part', -1), ('believe', -1), ('b', -1), ('14', -1), ('brady', -1), ('r', -1), ('uncanny', -1), ('derailing', -1), ('were', -1), ('hawkins-capitalism', -1), ('mind', -1), ('tonight', -1), ('talking', -1), ('say', -1), ('need', -1), ('my', -1), ('apparently', -1), ('any', -1), ('responsible', -1), ('-', -1), ('ideas', -1), ('note', -1), ('take', -1), ('which', -1), ('destroy', -1), ('middleclass', -1), ('play', -1), ('worldhardball', -1), ('banks', -1), ('74', -1), ('plan', -1), ('why', -1), ('hypocrite', -1), ('socialistlike', -1), ('socialistic', -1), ('face', -1), ('voting', -1), ('away', -1), ('supported', -1), ('defended', -1), ('imagined', -1), ('knowledge', -1), ('ruin', -1), ('enough', -1), ('only', -1), ('communist', -1), ('dontvote', -1), ('get', -1), ('stop', -1), ('sensanders', -1), ('truly', -1), ('made', -1), ('him', -1), ('taxes', -1), ('usaprotect', -1), ('bad', -1), ('stupid', -1), ('where', -1), ('vision', -1), ('nut', -1), ('elected', -1), ('computer', -1), ('fail', -1), ('hero', -1), ('wonder', -1), ('lots', -1), ('wow', -1), ('behind', -1), ('amen', -1), ('killing', -1), ('democratsocialist', -1), ('come', -1), ('protect', -1), ('last', -1), ('many', -1), ('against', -1), ('foreign', -1), ('became', -1), ('planned', -1), ('forgotten', -1), ('requests', -1), ('wall', -1), ('period', -1), ('cranium', -1), ('unelectable', -1), ('46k', -1), ('worthless', -1), ('beef', -1), ('family-yep', -1), ('sanderss', -1), ('political', -1), ('much', -1), ('damn', -1), ('life', -1), ('these', -1), ('straight', -1), ('bill', -1), ('near', -1), ('country', -1), ('property', -1), ('ive', -1), ('them', -1), ('id', -1), ('things', -1), ('same', -1), ('gamejedi', -1), ('wakeup', -1), ('stepped', -1), ('finish', -1), ('running', -1), ('totally', -1), ('vermont', -1), ('thought', -1), ('40yrs', -1), ('spend', -1), ('venezuelans', -1), ('proposed', -1), ('talkwheres', -1), ('elect', -1), ('yet', -1), ('letting', -1), ('similarities', -1), ('reasons', -1), ('add', -1), ('prison', -1), ('2seize', -1), ('government', -1), ('big', -1), ('five', -1), ('know', -1), ('govt', -1), ('like', -1), ('loser', -1), ('loses', -1), ('audience', -1), ('50-90', -1), ('jews', -1), ('deal', -1), ('senate', -1), ('creation', -1), ('library', -1), ('socialists', -1), ('economic', -1), ('scares', -1), ('lead', -1), ('literally', -1), ('everything', -1), ('denied', -1), ('screwed', -1), ('leader', -1), ('knew', -1), ('extraordinaire', -1), ('peer', -1), ('takes', -1), ('wouldnt', -1), ('most', -1), ('freedom', -1), ('ussenator', -1), ('ideology', -1), ('keeps', -1), ('civil', -1), ('into', -1), ('nobernie', -1), ('raises', -1), ('electorate', -1), ('couldnt', -1), ('impressed', -1), ('her', -1), ('hes', -1), ('ameica', -1), ('specifically', -1), ('utopian', -1), ('lot', -1), ('ago', -1), ('but', -1), ('reminds', -1), ('repeated', -1), ('bum', -1), ('trying', -1), ('with', -1), ('count', -1), ('fraud', -1), ('wish', -1), ('distract', -1), ('tell', -1), ('planet', -1), ('record', -1), ('aa', -1), ('gone', -1), ('proven', -1), ('divisive', -1), ('again', -1), ('marxist', -1), ('no', -1), ('40', -1), ('started', -1), ('setting', -1), ('trash', -1), ('nice', -1), ('explaining', -1), ('everybodys', -1), ('students', -1), ('visits', -1), ('stay', -1), ('tackle', -1), ('rights', -1), ('assets', -1), ('tricks', -1), ('holes', -1), ('attacking', -1), ('greathe', -1), ('time', -1), ('once', -1)]
positive_words = [('represent', 1), ('all', 1), ('todays', 1), ('httpstco4lliklpzkc', 1), ('stops', 1), ('welfare', 1), ('chair', 1), ('young', 1), ('finally', 1), ('voted', 1), ('under', 1), ('women', 1), ('httpstcosbyibesxcu', 1), ('tulsi', 1), ('sc4sanders', 1), ('fall', 1), ('httpstcogwln9hcauy', 1), ('join', 1), ('difference', 1), ('httpstcoxv8tezjimv', 1), ('did', 1), ('ceecee', 1), ('try', 1), ('guy', 1), ('enjoy', 1), ('httpstco69j6jh3lvl', 1), ('ted', 1), ('sign', 1), ('mmflint', 1), ('hardballchris', 1), ('mrchuckd', 1), ('new', 1), ('marching', 1), ('movement', 1), ('httpstcobwcfq8agwu', 1), ('here', 1), ('httpstcoyuxwsepsg9', 1), ('beck', 1), ('healing', 1), ('others', 1), ('grforsanders', 1), ('great', 1), ('httpstcohs0h9ezxhm', 1), ('calets', 1), ('stressed', 1), ('ctl', 1), ('httpstcolzf2zwg2gh', 1), ('love', 1), ('campaign', 1), ('carolinians', 1), ('httpstcomkfiob6i\xe2\x80\xa6', 1), ('from', 1), ('httpstcoxuhjc1edam', 1), ('httpstco0w4vawvfge', 1), ('opposed', 1), ('iacaucus', 1), ('httpstcox8uxlvyvce', 1), ('craig19eighty8', 1), ('fellow', 1), ('supporters', 1), ('faith', 1), ('glad', 1), ('town', 1), ('teamblack', 1), ('wtin', 1), ('rights', 1), ('pursue', 1), ('challenge', 1), ('nina', 1), ('obvious', 1), ('demdebate', 1), ('jjmccabe2', 1), ('mmx324', 1), ('trump', 1), ('figure', 1), ('httpstcoochz92uwuo', 1), ('imwithher', 1), ('energizedaccepting', 1), ('jeanette607', 1), ('bern\xe2\x80\xa6', 1), ('democracy', 1), ('cheering', 1), ('httpstcolqsbmvpuxd', 1), ('httpstco45geodwrf5', 1), ('httpstcotuixf35hpz', 1), ('amazing', 1), ('endorsement', 1), ('instead', 1), ('resignation', 1), ('time\xe2\x80\x94just', 1), ('plans', 1), ('fascist', 1), ('after', 1), ('sweateryams', 1), ('jbspharmd', 1), ('ethics', 1), ('man', 1), ('short', 1), ('cnnpolitics', 1), ('so', 1), ('allow', 1), ('democratic', 1), ('beck-fast', 1), ('httpstconssgw4gfdi', 1), ('breaking', 1), ('over', 1), ('whoisagentzero', 1), ('years', 1), ('isnt', 1), ('looks', 1), ('feeltheb\xe2\x80\xa6', 1), ('whats', 1), ('still', 1), ('group', 1), ('thank', 1), ('amounted', 1), ('labor', 1), ('better', 1), ('yesterdays', 1), ('msnbc', 1), ('catspaws', 1), ('httpstco6wsk457tgk', 1), ('then', 1), ('them', 1), ('someone', 1), ('timbartender', 1), ('httpstc\xe2\x80\xa6', 1), ('republican', 1), ('\xf0\x9f\x91\x8f\xf0\x9f\x8f\xbd\xf0\x9f\x91\x8f\xf0\x9f\x8f\xbd\xf0\x9f\x91\x8f\xf0\x9f\x8f\xbd\xf0\x9f\x91\x8f\xf0\x9f\x8f\xbd', 1), ('establishment', 1), ('friendship', 1), ('38magpie', 1), ('httpstcor4ksdt7rzd', 1), ('feelt\xe2\x80\xa6', 1), ('yeah', 1), ('relates', 1), ('emerges', 1), ('may', 1), ('terray16', 1), ('internet', 1), ('got', 1), ('announced', 1), ('free', 1), ('wanted', 1), ('care', 1), ('opps', 1), ('exposing', 1), ('could', 1), ('turn', 1), ('raleigh', 1), ('w', 1), ('austin', 1), ('think', 1), ('first', 1), ('chimchiminee', 1), ('feel', 1), ('self-promo', 1), ('powerful', 1), ('primary', 1), ('one', 1), ('twat', 1), ('corporations', 1), ('sounds', 1), ('quality', 1), ('httpstcomtj1flsukw', 1), ('swarm', 1), ('too', 1), ('bernies', 1), ('stomach', 1), ('luncheon', 1), ('nobody', 1), ('missenji', 1), ('believe', 1), ('representing', 1), ('than', 1), ('obama', 1), ('hs4bernie', 1), ('12', 1), ('moveon', 1), ('httpstco5485\xe2\x80\xa6', 1), ('onmiemtp', 1), ('failing', 1), ('well', 1), ('talking', 1), ('ambitious', 1), ('weirdaunt', 1), ('any', 1), ('bellacoconut', 1), ('-', 1), ('potential', 1), ('which', 1), ('scprimary', 1), ('httpstcoujbx3qy5s1', 1), ('who', 1), ('httpstcomx1aerz50y', 1), ('hillary2016', 1), ('sandersonhardball', 1), ('tpp', 1), ('voting', 1), ('painting', 1), ('dailydiscord', 1), ('bigotries', 1), ('httpstcomcrvwww65b', 1), ('httpstcofmdu2adrsj', 1), ('dsdradio', 1), ('sharks', 1), ('httpstcovs7zdsrram', 1), ('justice', 1), ('should', 1), ('only', 1), ('going', 1), ('candidates', 1), ('thousands', 1), ('election2016', 1), ('carolina', 1), ('stop', 1), ('pocket', 1), ('cannot', 1), ('nearly', 1), ('cdhill9', 1), ('trade', 1), ('davidsirota', 1), ('chained', 1), ('stuff', 1), ('she', 1), ('hype', 1), ('westandtogether', 1), ('supertuesday', 1), ('secretary', 1), ('httpstcomzs9lwlagz', 1), ('btw', 1), ('aheadhes', 1), ('httpstco3x35yfxe\xe2\x80\xa6', 1), ('see', 1), ('are', 1), ('hall', 1), ('nailed', 1), ('away', 1), ('genius', 1), ('enough', 1), ('won', 1), ('bernievshillary', 1), ('httpstco8iggutmup6', 1), ('importance', 1), ('attention', 1), ('job', 1), ('news', 1), ('come', 1), ('wcgirl1', 1), ('many', 1), ('supportersdont', 1), ('against', 1), ('s', 1), ('trumps', 1), ('workers', 1), ('texastribune', 1), ('can', 1), ('2nd', 1), ('learning', 1), ('diff', 1), ('winning', 1), ('targeting', 1), ('political', 1), ('mikehersh', 1), ('life', 1), ('champion', 1), ('httpstcov7opfmcosy', 1), ('offered', 1), ('republicans', 1), ('longgame', 1), ('standup', 1), ('atlanta', 1), ('evidence', 1), ('former', 1), ('volunteer', 1), ('sound', 1), ('advocating', 1), ('these', 1), ('crowds', 1), ('bill', 1), ('slc', 1), ('httpstcoc41npjloq7', 1), ('cynagedt', 1), ('jeanettejing', 1), ('wearjustice', 1), ('httpstcovgkccc2iax', 1), ('watched', 1), ('followback', 1), ('turner', 1), ('httpstcockgqfholti', 1), ('anymore', 1), ('-yvettedc', 1), ('peterdaou', 1), ('1246', 1), ('yesterday', 1), ('fasting', 1), ('httpstcor2pe3op3nd', 1), ('youre', 1), ('buffalo339', 1), ('claims', 1), ('corporate', 1), ('grandkids', 1), ('nc', 1), ('less', 1), ('seekermail', 1), ('criticism', 1), ('jimharris', 1), ('human', 1), ('notyourfirewall', 1), ('newhitler', 1), ('cut', 1), ('troysnoize', 1), ('candidate', 1), ('thinking', 1), ('httpstco7mho010jwz', 1), ('wethepeople', 1), ('had', 1), ('except', 1), ('httpstcoacps5vgzna', 1), ('southcarolinaprimary', 1), ('loss', 1), ('big', 1), ('cruz', 1), ('gabbard', 1), ('feelthe\xe2\x80\xa6', 1), ('like', 1), ('lost', 1), ('impunityregulation', 1), ('standwithbernie', 1), ('either', 1), ('endorsed', 1), ('sanders2016', 1), ('deal', 1), ('fucking', 1), ('election', 1), ('wallstreet', 1), ('httpstconunwzhsqwn', 1), ('scandals', 1), ('newthatcher', 1), ('httpstcop7lmpz6zgn', 1), ('literally', 1), ('everything', 1), ('httpstcozqlq5\xe2\x80\xa6', 1), ('httpstcou7w0vx9rk1', 1), ('bc', 1), ('votetogether', 1), ('bs', 1), ('mondaymotivation', 1), ('about', 1), ('mm4bernie', 1), ('httpstcobmgnhn4poz', 1), ('whichhillary', 1), ('mean', 1), ('block', 1), ('clinton', 1), ('glenn', 1), ('civil', 1), ('two', 1), ('down', 1), ('lies', 1), ('doesnt', 1), ('actually', 1), ('her', 1), ('there', 1), ('long', 1), ('start', 1), ('low', 1), ('way', 1), ('hq', 1), ('but', 1), ('goals', 1), ('line', 1), ('trying', 1), ('follow-thank', 1), ('kellinquinn', 1), ('ut', 1), ('mtp', 1), ('official', 1), ('today', 1), ('piece', 1), ('ad', 1), ('general', 1), ('picbernie2016', 1), ('rally', 1), ('vets4bernie', 1), ('again', 1), ('compared', 1), ('peace', 1), ('httpstcoogasr5racr', 1), ('sick', 1), ('nationalnurses', 1), ('10', 1), ('markruffalo', 1), ('seyah203', 1), ('cpi', 1), ('wife', 1), ('invest', 1), ('vigorously', 1), ('youtube', 1), ('whatfirewall', 2.3), ('go', 2.3), ('consider', 2.3), ('voter', 2.3), ('choice', 2.3), ('delegate', 2.3), ('supporting', 2.3), ('involved', 2.3), ('theres', 2.3), ('httpstcogueuoz5rop', 2.3), ('dnc', 2.3), ('baillieginnifer', 2.3), ('phone', 2.3), ('connie', 2.3), ('must', 2.3), ('hope', 2.3), ('my', 2.3), ('huge', 2.3), ('needs', 2.3), ('johnson', 2.3), ('courage', 2.3), ('sc', 2.3), ('httpstco87lmoxd2a3', 2.3), ('before', 2.3), ('bernieorbust', 2.3), ('mail', 2.3), ('\xe2\x80\x9988', 2.3), ('day', 2.3), ('bank', 2.3), ('superdelegate', 2.3), ('phonebank', 2.3), ('jackson', 2.3), ('hillaryclinton', 2.3), ('out\xe2\x80\xa6', 2.3), ('turnout', 2.3), ('httpstcohkiuejk5ex', 2.3), ('south', 2.3), ('dont', 2.3), ('black2016', 2.3), ('2', 2.3), ('gear', 2.3), ('came', 2.3), ('find', 2.3), ('partisan2016', 2.3), ('nbex9', 2.3), ('sensanders', 2.3), ('him', 2.3), ('rutger211', 2.3), ('slapped', 2.3), ('donate', 2.3), ('httpstcowiggajcnmf', 2.3), ('wear', 2.3), ('look', 2.3), ('socialsecurity', 2.3), ('berniestrong', 2.3), ('media', 2.3), ('okpol', 2.3), ('deltoscano', 2.3), ('more', 2.3), ('they', 2.3), ('just', 2.3), ('family', 2.3), ('bernie\xe2\x80\xa6', 2.3), ('march', 2.3), ('virginia', 2.3), ('httpstcogw\xe2\x80\xa6', 2.3), ('bit', 2.3), ('people', 2.3), ('dear', 2.3), ('httpstco\xe2\x80\xa6', 2.3), ('endorsing', 2.3), ('on', 2.3), ('area', 2.3), ('was', 2.3), ('httpstcofu3lhuouqt', 2.3), ('count', 2.3), ('up', 2.3), ('ur', 2.3), ('convince', 2.3), ('at', 2.3), ('jesse', 2.3), ('want', 2.3), ('other', 2.3), ('really', 2.3), ('friends', 2.3), ('perspective', 4.1), ('canvass', 4.1), ('what', 4.1), ('change', 4.1), ('via', 4.1), ('win', 4.1), ('vote4truth', 4.1), ('cant', 4.1), ('help', 4.1), ('not', 4.1), ('event', 4.1), ('out', 4.1), ('system', 4.1), ('need', 4.1), ('hillary', 4.1), ('with', 4.1), ('get', 4.1), ('corrupt', 4.1), ('please', 4.1), ('taking', 4.1), ('senator', 4.1), ('colleges4bernie', 4.1), ('tulsigabbard', 4.1), ('money', 4.1), ('endorses', 4.1), ('ok', 4.1), ('or', 4.1), ('support', 4.1), ('https\xe2\x80\xa6', 4.1), ('httpst\xe2\x80\xa6', 6.5), ('its', 6.5), ('vote', 6.5), ('feelthebern', 6.5), ('endorsebernie', 6.5), ('we', 6.5), ('bernie2016', 6.5), ('notmeus', 6.5), ('amp', 6.5), ('ncforbernie', 6.5), ('by', 6.5), ('your', 6.5), ('us', 6.5)]


#print negative_words[3][0] 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

#take out commonly used words
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

# def count_occurences(list):
# #list is a list of the tokens for each tweet
# count = collections.Counter()
# for all_tweet_tokens in li:
# 	i = 0
# 		if(all_tweet_tokens[i] == 'RT'):
#  			#start iteration at 2...
# 			i = 2
#  		for individual_token in all_tweet_tokens:
#  			count[]
 
#call preprocess(tweet)
#generate a list of tokens..
def parseToString(token):
	i = 0
	if token[0]=='RT':
		i = 3
	str = ''
	while i < len(token):
		str+= token[i] + ' '
		i = i+1
	return str

def get_weight(occurence):
	if x<=2:
		return 1
	if x>=2 and x<=4:
		return 2.3
	if x>4 and x<=6:
		return 4.1
	return 6.5

li = []
count = 0
with open('tweets.json','r') as f, open('web_tweets.json','w') as g:
	for l in f:
		score = 0
		t = json.loads(l)
		tokens = preprocess(t['text'])
		li.append(tokens)
		str = parseToString(tokens)
		b = str.split()
		for word in b:
			for item in negative_words:
				if(unicode(item[0], encoding='utf-8')== word):
					score+=item[1]
			for item in positive_words:
				if(unicode(item[0], encoding='utf-8') == word):
					score+=item[1]
		count = count + 1
		
		# if (score > 2):
		# 	tweet_json = t
		if(score > 2):
			json.dump(json.loads(l),g)
			g.write("\n")
			print "write successful!"

		if(count >= 5000):
			break
		


		# for word in str:
		# 	if word in negative_words:
		# 		negative_words.get(word)
		# 		score += negative_words(value of that word)
		# 	if word in positive words:
		# 		positive_words.get(word)
		# 		score += positive_words(value of that word)

		# 	if score > 2 
		# 		append to a file 


		#call a method that takes in tokens and returns a string with spaces,
		#accounting for the possibiility that token0 can be RT
		#print tokens
print li[0] #li[i] contains tokens for the ith tweet with no punc/non needed things




# li is a list where l[i] contains the tokens for the ith tweet with no punc/non needed things
#TODO
#perform the sentiment analysis 
#figure out how to return write to a json, the tweets...




#data dump
#after processing, tweets should still be in JSON
#write these tweets to web_tweets, i think
# format and be written to in json (as in search tweets.py) to a file
#called web_tweets.json = f

with open('web_tweets.json', 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if tweet['user']['location']:
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['user']['location'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']

                }
            }
            geo_data['features'].append(geo_json_feature)
        #TODO - we need A LOT MORE TWEETS!

 
# Save geo data
with open('geo_data.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))






