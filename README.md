## DelTuit

This simple script deletes all the tuits of a given account except for the last N by using the twitter archive.

## Using the script

1. Download the files

2. Register a new application on [Twitter\'92s developer page](https://dev.twitter.com/)

3. Fill <code>config.py</code> with the keys acquired in the Twitter\'92s site. <code>ntuits</code> sets the number of tweets to keep in the account. It is set to 2000 by default.

4. Download your twitter archive from the [settings page of your Twitter account](https://twitter.com/settings/account) and put it in the same folder than the script. Change its name to \cf2 \outl0\strokewidth0 <code>\cf2 \outl0\strokewidth0 \strokec2 archivo.zip\cf2 \outl0\strokewidth0 </code>.

5. Run \cf2 \outl0\strokewidth0 \strokec2 <code>$ python Deltuit.py</code>. This will start deleting all the tweets in the account except for the last \cf2 \outl0\strokewidth0 <code>ntuits</code>. It will take a lot of time due to twitter API limitations (about 10000 per hour).\cf2 \outl0\strokewidth0 \strokec2 


## Author

* **Mario Herrero** 

Inspired by the script in [Rinze\'92s repository.](https://github.com/rinze/obliterate_tweets).
