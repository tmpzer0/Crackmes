import subprocess

fo = open("./wordlist", "r+")

for line in fo:
    key = 'r' + str(line).rstrip()+'qidinghood'
    result = subprocess.run(["./forest"],text=True,input=key,capture_output=True)

    if 'Flag is correct' in result.stdout:
        print("Accepted key: " +key)
