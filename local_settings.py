'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'DP193h00eDSPyscqSo012sv6P'
MY_CONSUMER_SECRET = 'uibH8tIjvyldnFYEq2siWQadDYsrim5elW4kaFpqW6DDmHzPx5'
MY_ACCESS_TOKEN_KEY = '926510843294109696-oPUrDlZjfrMB66up3RYXd1iR6S0W1C1'
MY_ACCESS_TOKEN_SECRET = 'asTNxjr1oVNNLL1HMPDU7abtGnY40WhEu6c7eTRDK7ce6'

SOURCE_ACCOUNTS = ["headandtheheart","tbtduluth","thelumineers","johnpaulwhite"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 3 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 2 is low and 4 is high.
SOURCE_EXCLUDE = r'^$' #Source tweets that match this regexp will not be added to the Markov chain. You might want to filter out inappropriate words for example.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = "ravettbrothers" #The name of the account you're tweeting to.
