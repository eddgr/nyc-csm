# NYC Chinese Supermarkets (NYC CSM)
Data Source: https://docs.google.com/spreadsheets/d/1zcMeOqeNeX0aeY807KESo2Ytq3sIaeCiKWfWOXRfbDQ/edit?fbclid=IwAR15BNbiFEnb8vKkaTBaESp6GbmOGNRveWioTBO6ZyNjoXK5aAyyG5vXqS0#gid=0

I've been using the Google Sheet to keep track of Chinese supermarkets that are open within NYC and wanted to share the information with my mom.

My mom isn't tech savvy but she knows how to use WeChat on her smartphone and open links.

The purpose of this project is to make the information from the spreadsheet acessible to people like my mom.

This project is open source so feel free to submit your pull requests!

You can view the current project here: https://kaimenmanyc.com

# Tech Stack
Currently keeping the project simple and using Flask.

# Getting Started
If you plan to use this locally, you will need to create credentials in Google API Console. You can follow these steps: https://gspread.readthedocs.io/en/latest/oauth2.html

I have named the credential file `google-credentials.json`. Once you have yours, you can save it in the project folder.

Then run `pip install -r requirements.txt`. You will need Python 2.7+ to use the `gspread` library.

Then you can run the app using `./run_remote.sh`.

# Deployment
If you plan to deploy this project without pushing your credentials, I created a function to create one if it doesn't exist using the environment variable `GOOGLE_CREDENTIALS`. 

Simply copy your credential json file and assign it to that variable. Look at `generate_credentials.py` for more details.

# To Do
- Add latest update date
- Update translations where necessary
