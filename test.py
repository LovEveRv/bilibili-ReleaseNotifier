from emailsender import MailSender

with open('mail.json', 'r', encoding='utf-8') as mf:
	mail_obj = json.load(mf)
with open('receivers.json', 'r', encoding='utf-8') as rf:
	receivers = json.load(rf)

ms = MailSender(mail_obj['sender'], mail_obj['pwd'])
title = 'Test Mail 2'
content = 'This is a mail sent by lyw, through python on Tencent Cloud.'
ms.send(receivers, title, content)