logging_path = 'Your Logging Path' # modify here
user = 'Your Link Email' # modify here
password = 'Your Password' # modify here

from urllib.request import urlopen
import logging, time, os, requests
url = 'http://captive.apple.com'
login_url = 'https://securelogin.net.cuhk.edu.hk/cgi-bin/login'
logging.basicConfig(filename=logging_path, level=logging.INFO, format='%(levelname)s:%(asctime)s %(message)s')
logging.info(f'Program Started. PID: {os.getpid()}.')

sleep_interval = .5
reconnect_interval = 3600*12 - 3

current_count = 0
cmd = 'authenticate'
submit = 'Login'
form = {'cmd': cmd, 'user': user, 'password': password, 'submit': submit}

def connect_test():
    try:
        resp = urlopen(url).read().decode('utf-8')
        return 'Success' in resp
    except Exception as e:
        logging.error(e)
    return False

def login():
    resp = requests.post(login_url, data=form, timeout=60)
    if resp.status_code == 200:
        logging.info(f'Login Success.')
        return True
    else:
        logging.warning(f'Login Failed. Status Code: {resp.status_code}')
        return False

while True:
    if connect_test():
        current_count += 1
        if current_count == 600:
            sleep_interval = 5
            logging.info(f'Switched to Slow Mode.')
    else:
        logging.info(f'No Internet Connection.')
        if login():
            current_count = 0
            sleep_interval = .5
            logging.info('Sleep for 12h.')
            time.sleep(reconnect_interval)
            logging.info('Wake up.')
        else:
            sleep_interval = 60
    time.sleep(sleep_interval)