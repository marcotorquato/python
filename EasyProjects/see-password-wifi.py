import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data = meta_data.decode('utf-8', errors = "backslashreplace")

data = data.split('\n')

profile = [] 

for i in data:

    if "All User Profile" in i :
        i = i.spli