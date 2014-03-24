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

#import smtplib

p = os.popen("%s -t" % sendmail, "w")
p.write("To: glevy@hotwire.com\n")
p.write("from: glevy@hotwire.com\n")
p.write("Subject: test\n")
p.write("\n") # blank line separating headers from body
p.write("Some text\n")
p.write("some more text\n")
sts = p.close()
if sts != 0:
   print "Sendmail exit status", sts
