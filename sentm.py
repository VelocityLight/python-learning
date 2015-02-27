#!/usr/bin/env  python
#-*- coding: utf-8 -*-

__author__ = "jc"

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

#格式化地址
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, "utf-8").encode(), addr.encode("utf-8") if isinstance(addr, unicode) else addr))

from_addr = raw_input("From: ")
password = raw_input("Password: ")
smtp_server = raw_input("Smtp server: ")
to_addr = raw_input("To: ")
print from_addr, password, smtp_server, to_addr

msg = MIMEText("hello, my email first send by python: ....", "plain", "utf-8")
msg["From"] = _format_addr(u"python lover 我<%s>"%from_addr)
msg["To"] = _format_addr(u"你 <%s>"%to_addr)
msg["Subject"] = Header(u"SMTP...", "utf-8").encode()

server = smtplib.SMTP()
server.connect(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sentmail(from_addr, [to_addr,], msg.as_string())
server.quit()

#Message
#+- MIMEBase
#  +- MIMEMultipart
#  +- MIMENonMultipart
#      +- MIMEMessage
#      +- MIMEText
#      +- MIMEImage