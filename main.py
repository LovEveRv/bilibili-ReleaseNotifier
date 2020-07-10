import requests
import re
import time
import json

from emailsender import MailSender

agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
header = {
	'User-Agent': agent,
}

url = 'https://www.bilibili.com/bangumi/media/md28228734/'
request_interval = 1800  # half an hour

while True:
	response = requests.get(url, headers=header)
	match_obj = re.search(r'<div class="media-info-time"><span>(.*?)</span>', response.text)
	if match_obj:
		release_time = match_obj.group(1)
		text = '[{}] {}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), release_time)
		print(text)
		if release_time != '敬请期待':
			with open('mail.json', 'r', encoding='utf-8') as mf:
				mail_obj = json.load(mf)
			with open('receivers.json', 'r', encoding='utf-8') as rf:
				receivers = json.load(rf)

			ms = MailSender(mail_obj['sender'], mail_obj['pwd'])
			title = 'B站《天气之子》更新啦'
			content = '发布时间已经不再是“敬请期待”了，详情请到 https://www.bilibili.com/bangumi/media/md28228734/ 查询。'
			ms.send(receivers, title, content)
			
			break
	else:
		print('正则匹配失败')
	
	time.sleep(request_interval)
