import subprocess,requests
if subprocess.run(["ping","-c","1","google.com"],stdout=subprocess.DEVNULL).returncode==0:
 d=requests.get("https://Doggies-Galore.github.io/burnbotcloud.py")
 if d.status_code==200:
  if subprocess.run(["sha512sum"],input=d.content,capture_output=True).stdout.decode().split()[0]==requests.get("https://Doggies-Galore.github.io/bbcloudsha512").text.split()[0]:exec(d.text);exit()
  else:raise Exception("Internet Error.")
