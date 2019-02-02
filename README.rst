Introduction
------------
I have created this code to extract turkish wiki dumps for testing NLP algorithms. Other extractors I've tried have character issues and didn't work well with Turkish Wiki Dump.

This module contains code for manipulating wikipedia dumps available at
http://download.wikimedia.org/backup-index.html

It is tested with ("https://dumps.wikimedia.org/trwiki/20170601/trwiki-20170601-pages-articles.xml.bz2") Turkish Wikipedia Dump.
It is not tested with other dumps.

Installation
------------
Required libraries are re, string, mwxml and cleantext. Written in Python 3.6

Program requires wiki dump to be named as "wiki.xml" in the root directory.
