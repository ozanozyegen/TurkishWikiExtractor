Introduction
------------
I have created this to extract turkish wiki dumps for testing NLP algorithms. Other extractors I've tried have character issues and didn't work well with TR Wiki Dump. It doesn't work perfect. But it is good enough to test NLP algorithms.

This module contains code for manipulating wikipedia dumps available from
http://download.wikimedia.org/backup-index.html

It is designed to be used at "https://dumps.wikimedia.org/trwiki/20170601/trwiki-20170601-pages-articles.xml.bz2" this Turkish Wikipedia Dump.
There is no guarantee that it will work well with other dumps.

Installation
------------
Required libraries are re, string, mwxml and cleantext. Written on Python 3.6


Program requires wiki dump to be named as "wiki.xml" in the root directory.
