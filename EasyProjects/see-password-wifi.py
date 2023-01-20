import subprocess

meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

data = meta_data.decode('utf-8', errors = "backslashreplace")

data = data.split('\n')

profiles = [] 

for i in data:

    if "All User Profile" in i :
        i = i.split(":")

        i = i[1]

        i = i[1:-1]

        profiles.append(i)

print("{:<30} | {:<}".format("WI-FI Name","Password"))
print("-------------------------------------------------------")

for i in profiles:

    try:
        results = subprocess.check_output(['netsh', 'wlan','profile', i, 'key = clear'])

        results = results.decode('utf-8', errors = "backslashreplace")
        results = results.split('\n')

        results = [b.split(":")[1:-1] for b in results if  "key Content" in b] 

        try:
            print("{:<30}| {:<}".format(i, results[0]))

        except indexError:
            print("{:<30} | {:<}".format(i, ""))
    
    except subprocess.CalledProcessError:
        print("Ecoding Error Occured")