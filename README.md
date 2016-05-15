# busdata
a simple bus data dump for sydney

## run
clone repo

create and activate a virtualenv

install requirements:

  pip install -r requirements.txt

go to https://opendata.transport.nsw.gov.au/site/en_us/home.html, register and get yourself
oauth credentials.

hamburger > Applications > Add Application > blah blah

Add "Public Transport - Realtime - Vehicle Positions"

Callback/Redirect URL = "http://127.0.0.1"

Scope = user

Type = confidential

Then substitute in your "API Key" and "Shared Secret" and run:

  oauthkey="my_oauth_key" oauthsecret="my_oauth_secret" ./application.py
