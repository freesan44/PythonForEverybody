import re
import socket
import requests
import urllib.request,urllib.parse
from bs4 import BeautifulSoup, ResultSet
import ssl
import xml.etree.ElementTree as ET
import json
import sqlite3
# import urllib3.request

# def computepay(h,e):
#     if h > 40:
#         pay = 40 * e + (h - 40) * 1.5 * e
#     else:
#         pay = h * e
#     return pay
#
#
# hrs = input("Enter Hours:")
# h = float(hrs)
# echp = input("Enter Rate Per Hour:")
# e = float(echp)
# print(computepay(h,e))

# score = input("Enter Score: ")
# try:
#     s = float(score)
#     if s>1.0 or s<0.0:
#         print("value error")
#     else:
#         if s>=0.9:
#             print("A")
#         elif s>=0.8:
#             print("B")
#         elif s>=0.7:
#             print("C")
#         elif s>= 0.6:
#             print("D")
#         else:
#             print("E")
# except:
#     print("value error")
#     exit()


# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#
#     try:
#         noNum = int(num)
#
#         if  largest == None:
#             largest = noNum
#         elif largest<noNum :
#             largest = noNum
#
#         if smallest == None:
#             smallest = noNum
#         elif smallest>noNum:
#             smallest = noNum
#
#     except:
#         print("Invalid input")
#
#
# print("Maximum is",largest)
# print("Minimum is",smallest)


# text = "X-DSPAM-Confidence:    0.8475"
# res = text[text.find(':')+1:].strip()
# res = float(res)
# print(res)
# print('Hello World!')
# print('I','Love','Python')


# # Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# fh = fh.read().upper()
# fh = fh.strip()
# print(fh)

# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# # fh = open('mbox-short.txt')
# count = 0
# numRes = 0.0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:") : continue
#     line = line.strip()
#     num = line[line.find(' ')+1:]
#     numRes += float(num)
#     count = count + 1
#
# res = numRes/count
# print('Average spam confidence: '+str(res))

# x = range(5)
# print(type(x))

# fname = input("Enter file name: ")
# fh = open(fname)
# # fh = open('romeo.txt')
# lst = list()
# letterList = list()
# for line in fh:
#     # print(line.rstrip())
#     letterEachList = line.rstrip().split()
#     for eachLetter in letterEachList:
#         if eachLetter not in letterList:
#             letterList.append(eachLetter)
# letterList.sort()
# print(letterList)


# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
# fh = open(fname)
# # fh = open('mbox-short.txt')
# count = 0
# res = list()
# # print(fh.read())
# for eachLine in fh:
#     # print(eachLine)
#     if eachLine.startswith('From'):
#         if eachLine.startswith('From:'):continue
#         lines = eachLine.split()
#         print(lines[1])
#         res.append(lines[1])
#         count = count +1
# print("There were", count, "lines in the file with From as the first word")

# stuff = dict()
# print(stuff.get('candy',-1))


# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# nameList = list()
# nameDic = dict()
# for each in handle:
#     if each.startswith('From') and not each.startswith('From:'):
#         words = each.split()
#         # name = words[1].split('@')
#         nameList.append(words[1])
#         # print(words[1])
#         nameDic[words[1]] = nameDic.get(words[1],0)+1
# # print(nameDic)
# maxKey = None
# maxValue = None
# for key,value in nameDic.items():
#     if maxValue is None or value > maxValue:
#         maxKey = key
#         maxValue = value
# print(maxKey,maxValue)

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# timeList = list()
# nameDic = dict()
# for eachLine in handle:
#     if eachLine.startswith('From') and not eachLine.startswith('From:'):
#         words = eachLine.split()
#         time = words[-2]
#         # print(time)
#         hours = time.split(':')[0]
#         nameDic[hours] = nameDic.get(hours,0)+1
# # print(nameDic)
# timeList = sorted([(v,k) for v,k in nameDic.items()])
# for v,k in timeList:
#     print(v,k)

# print("I Love Python")

# str = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# s = re.findall('@(\S+)',str)
# print(s)

# filehandle = open('regex_sum_167844.txt')
# numForRand = 0
# for eachLine in filehandle:
#     numList = re.findall('[0-9]+', eachLine)
#     if len(numList) > 0:
#         for eachNum in numList:
#             # print(eachNum)
#             numForRand += int(eachNum)
# print(numForRand)

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()
## type: list[bytes]

# fileHand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#
# lines: bytes
# for lines in fileHand:
#     print(lines.decode())


# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE


# # url = "http://py4e-data.dr-chuck.net/comments_42.html"
# url = "http://py4e-data.dr-chuck.net/comments_167846.html"
# html = urllib.request.urlopen(url, context=ctx).read()
# soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
# # print(soup)
# sum = 0
# tags: ResultSet = soup('span')
# tag: BeautifulSoup
# for tag in tags:
#     # print(tag.contents[0])
#     sum = sum + int(tag.contents[0])
#
# print(sum)


# # url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# url = "http://py4e-data.dr-chuck.net/known_by_Sahaib.html"
# html = urllib.request.urlopen(url, context=ctx).read()
# soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
# # print(soup)
# num = 17
# for i in range(7):
#     link_list = soup('a') #type: list[BeautifulSoup]
#     link_str = link_list[num].get('href',None)
#     print(link_str)
#     url = link_str
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup: BeautifulSoup = BeautifulSoup(html, "html.parser")
#
# # link_tag: BeautifulSoup
# # for link_tag in link_list:
# #     print(link_tag.get('href',None))


# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
#
# # address = input('Enter location: ')
#
# # url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
# url = 'http://py4e-data.dr-chuck.net/comments_167848.xml'
# print('Retrieving', url)
# uh = urllib.request.urlopen(url, context=ctx)
#
# data = uh.read()
# print('Retrieved', len(data), 'characters')
# print(data.decode())
# tree = ET.fromstring(data)
#
# # results = tree.findall('result')
# # lat = results[0].find('geometry').find('location').find('lat').text
# # lng = results[0].find('geometry').find('location').find('lng').text
# # location = results[0].find('formatted_address').text
#
# # print('lat', lat, 'lng', lng)
# # print(location)
#
# # results = tree.find('comments').findall('comment')
# results = tree.findall('.//count')
# sum = 0
# # print(results)
# for res in results:
#     # print(res.find('count').text)
#     # sum = sum + int(res.find('count').text)
#     sum = sum + int(res.text)
# print(sum)


# url = 'http://py4e-data.dr-chuck.net/comments_167849.json'
#
# handle: urllib = urllib.request.urlopen(url)
# data = handle.read().decode()
# json_info = json.loads(data)
# info_list = json_info['comments'] #type: list[dict]
# print(info_list)
# sum = 0
# for each in info_list:
#     sum = sum + int(each['count'])
# print(sum)


# url = 'http://py4e-data.dr-chuck.net/json?'
#
# parms = dict()
# parms['key'] = 42
# parms['address'] = 'City of Westminster College'
#
# url = url + urllib.parse.urlencode(parms)
# print(url)
# handle: urllib = urllib.request.urlopen(url)
# info = handle.read().decode()
# print(info)
# print(len(info))

# conn = sqlite3.connect('emaildb.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('''
# CREATE TABLE Counts (org TEXT, count INTEGER)''')
#
# # fname = input('Enter file name: ')
# fname = 'mbox.txt'
# # if (len(fname) < 1): fname = 'mbox-short.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From: ') or not line.startswith('From'): continue
#     pieces = line.split()
#     email = pieces[1]
#     print('email', email)
#     emails = email.split('@')
#     org = emails[1]
#     print('org',org)
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES (?, 1)''', (org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                     (org,))
#     conn.commit()
#
# # https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
#
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])
#
# cur.close()



# conn = sqlite3.connect('rosterdb.sqlite')
# cur = conn.cursor()
#
# # Do some setup
# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;
#
# CREATE TABLE User (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name   TEXT UNIQUE
# );
#
# CREATE TABLE Course (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title  TEXT UNIQUE
# );
#
# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')
#
#
# # fname = input('Enter file name: ')
# # if len(fname) < 1:
# #     fname = 'roster_data_sample.json'
# fname = 'roster_data.json'
#
# # [
# #   [ "Charley", "si110", 1 ],
# #   [ "Mea", "si110", 0 ],
#
# str_data = open(fname).read()
# json_data = json.loads(str_data)
#
# for entry in json_data:
#
#     name = entry[0];
#     title = entry[1];
#     role = entry[2];
#
#     print((name, title, role))
#
#     cur.execute('''INSERT OR IGNORE INTO User (name)
#         VALUES ( ? )''', ( name, ) )
#     cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
#     user_id = cur.fetchone()[0]
#
#     cur.execute('''INSERT OR IGNORE INTO Course (title)
#         VALUES ( ? )''', ( title, ) )
#     cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
#     course_id = cur.fetchone()[0]
#
#     cur.execute('''INSERT OR REPLACE INTO Member
#         (user_id, course_id , role) VALUES ( ?, ?, ?)''',
#         ( user_id, course_id, role ) )
#
#     conn.commit()
# cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM
#     User JOIN Member JOIN Course
#     ON User.id = Member.user_id AND Member.course_id = Course.id
#     ORDER BY X''')
# print('result\n',cur.fetchall())

print(ord('L'))
