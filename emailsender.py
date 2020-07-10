import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender:

	def __init__(self, sender, pwd):
		self.mail_host = 'smtp.qq.com'
		self.mail_pass = pwd
		self.sender = sender

	def send(self, receivers, title, content):
		message = MIMEText(content, 'plain', 'utf-8')
		
		message['From'] = Header('Notifier' 'utf-8')
		message['To'] =  Header('Release Receivers', 'utf-8')
		 
		message['Subject'] = Header(title, 'utf-8')
		 
		 
		try:
		    smtpObj = smtplib.SMTP() 
		    smtpObj = smtplib.SMTP_SSL(self.mail_host, 465) 
		    smtpObj.login(self.sender, self.mail_pass)  
		    smtpObj.sendmail(self.sender, receivers, message.as_string())
		    smtpObj.quit()
		    print('邮件发送成功')
		except smtplib.SMTPException:
		    print('Error: 无法发送邮件')