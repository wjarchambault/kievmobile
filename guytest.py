#! /usr/bin/env python

import os, sys, shutil, time, copy, stat, fnmatch
import os.path
import smtplib
import email.utils

print "Hello World!"
date = time.strftime("%m-%d-%y")
print date

sendmail="/p4/qa/tools/sendEmail/sendEmail"
SERVER = "sfimc01"

import smtplib


sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <glevy@hotwire.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP(SERVER)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"



"""
p = os.popen("%s -t" % sendmail, "w")
p.write("To: glevy@hotwire.com\n")
p.write("Subject: test\n")
p.write("\n") # blank line separating headers from body
p.write("Some text\n")
p.write("some more text\n")
sts = p.close()
if sts != 0:
   print "Sendmail exit status", sts
"""
