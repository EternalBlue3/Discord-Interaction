# Discord Interaction
This is a simple easy to use script for interacting with your discord account.
It requires the requests, random and json modules to work.

Example:

(I couldn't get the example here so I put it in example.py)
    
If you look, this script will change your status 4 times/sec. The change_status() function takes 2 inputs: the new status and the token.

Just a warning, but if you try to send requests to discord too fast, it will return 400 (meaning that your request didn't go through). 
For example, if you were to try to spam someone with messages, discord would stop you by blocking your requests.
