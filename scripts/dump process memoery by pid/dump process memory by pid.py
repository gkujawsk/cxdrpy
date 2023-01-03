import requests, time, zipfile, os, gzip
from subprocess import Popen, PIPE

def main(pid):
	url = 'https://download.sysinternals.com/files/Procdump.zip'
	r = requests.get(url)
	with open('procdump.zip', 'wb') as f:
		f.write(r.content)
	with zipfile.ZipFile('procdump.zip', 'r') as zip_ref:
		zip_ref.extractall('.')
	time.sleep(2)
	process = Popen(['procdump.exe', '-accepteula', '-ma', str(pid), str(pid) +'.dmp'], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
	print(stdout)
	time.sleep(2)
	os.remove('eula.txt')
	os.remove('procdump.zip')
	os.remove('procdump64.exe')
	os.remove('procdump.exe')
	with open(str(pid) +'.dmp', 'rb') as f_in, gzip.open(str(pid) +'.zip', 'wb') as f_out:
		f_out.writelines(f_in)
	time.sleep(2)
	os.remove(str(pid) +'.dmp')
	return { 'files_to_get': str(pid) +'.zip' }
	
if __name__ == "__main__":
    main()