{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww19620\viewh13420\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # DelTuit\
\
This simple script deletes all the tuits of a given account except for the last N by using the twitter archive\
\
## Using the script\
\
1. Download the files\
\
2. Register a new application on [Twitter\'92s developer page](https://dev.twitter.com/)\
\
3. Fill <code>config.py</code> with the keys acquired in the Twitter\'92s site. <code>ntuits</code> sets the number of tweets to keep in the account. It is set to 2000 by default.\
\
4. Download your twitter archive from the [settings page of your Twitter account](https://twitter.com/settings/account) and put it in the same folder than the script. Change its name to \cf2 \outl0\strokewidth0 <code>\cf2 \outl0\strokewidth0 \strokec2 archivo.zip\cf2 \outl0\strokewidth0 </code>.\
\
5. Run \cf2 \outl0\strokewidth0 \strokec2 <code>$ python Deltuit.py</code>. This will start deleting all the tweets in the account except for the last \cf2 \outl0\strokewidth0 <code>ntuits</code>. It will take a lot of time due to twitter API limitations (about 10000 per hour).\cf2 \outl0\strokewidth0 \strokec2 \
\
\
## Author\
\
* **Mario Herrero** \
\
Inspired by the script in [Rinze\'92s repository.](https://github.com/rinze/obliterate_tweets).\
\
}