# peek-link-bot

A reddit bot that gives a preview of a parent comment's linked URLs so you don't get rickrolled anymore.

## Dependencies

``` bash
    pip install beautifulsoup4 praw sqlalchemy
```

## Running the code

First, you have to create a reddit account and add the peek-link-bot application to the authorized applications for the account. You can do this on https://old.reddit.com/prefs/apps/.

After you register the application, fill out the informations on the ```praw.template.ini``` file and save it as ```praw.ini```. Now you can just run the ```main.py``` file on the command line and the bot will be actively looking for mentions asking it to peek some link.

