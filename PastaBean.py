#!/usr/bin/python

import re, requests, json, time, datetime, smtplib

while True:
	### Read in last N posts and get the key and put in array
	now = datetime.datetime.now()
	print 'Loop Check  = ' + str(now.strftime("%H:%M:%S%p"))
	post_limit = '100'
	last_n_posts = requests.get('https://scrape.pastebin.com/api_scraping.php?limit=' + post_limit).text
	json_posts = json.loads(last_n_posts)

	for post in json_posts:
			raw_post_text = requests.get('https://scrape.pastebin.com/api_scrape_item.php?i='+ post['key'])
		
			if re.match('(password|leak|dump)', raw_post_text.text, re.IGNORECASE) is not None :
				a = open('{0}-{1}.txt'.format(post['key'], 'Common'), 'w')
				a.write(raw_post_text.text.encode('utf-8').strip())
				a.close()
			elif re.match('TV(oA|pB|pQ|qA|qQ|ro)', raw_post_text.text) is not None :
				b = open('{0}-{1}.txt'.format(post['key'], 'PE64'), 'w')
				b.write(raw_post_text.text.encode('utf-8').strip())
				b.close()
			elif re.match('sdcard', raw_post_text.text, re.IGNORECASE) is not None :
				c = open('{0}-{1}.txt'.format(post['key'], 'sdcard'), 'w')
				c.write(raw_post_text.text.encode('utf-8').strip())
				c.close()
			elif re.match('.*.\.onion', raw_post_text.text, re.IGNORECASE) is not None :
				d = open('{0}-{1}.txt'.format(post['key'], 'onion'), 'w')
				d.write(raw_post_text.text.encode('utf-8').strip())
				d.close()
			elif re.match('(STRING|ENTER|DELAY)',  raw_post_text.text, re.IGNORECASE) is not None :
				e = open('{0}-{1}.txt'.format(post['key'], 'Ducky'), 'w')
				e.write(raw_post_text.text.encode('utf-8').strip())
				e.close()
			elif re.match('aHR0cDovLw', raw_post_text.text) is not None :
				f = open('{0}-{1}.txt'.format(post['key'], 'httpB64'), 'w')
				f.write(raw_post_text.text.encode('utf-8').strip())
				f.close()
			elif re.match('QUACK.*.|(powershell|bash)|(LED.*.)|(ATTACKMODE.*.)', raw_post_text.text, re.IGNORECASE) is not None :
				g = open('{0}-{1}.txt'.format(post['key'], 'BASH-BUNNY'), 'w')
				g.write(raw_post_text.text.encode('utf-8').strip())
				g.close()
			elif re.match('(IEX|iex|SUVY|aWV4)', raw_post_text.text) is not None :
				h = open('{0}-{1}.txt'.format(post['key'], 'PS-IEX'), 'w')
				h.write(raw_post_text.text.encode('utf-8').strip())
				h.close()
			elif re.match('powershell', raw_post_text.text, re.IGNORECASE) is not None :
				i = open ('{0}-{1}.txt'.format(post['key'], 'PS-NOR'), 'w')
				i.write(raw_post_text.text.encode('utf-8').strip())
				i.close()
			
       			
			 
	time.sleep(60)

 
 





