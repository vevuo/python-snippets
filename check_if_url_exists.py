import urllib.request
from colorama import init, Fore

init(autoreset=True)

site = {
	'Wikipedia' : [
		'https://en.wikipedia.org/wiki/Python_(film)',
		'https://en.wikipedia.org/wiki/Python_(programming_language)',
		'https://en.wikipedia.org/wiki/Pdfsthon_(mythology)',
	],
	'Wikipedia2' : [
		'https://en.wikipedia.org/wiki/Python_(film)',
		'https://en.wikipedia.org/wiki/Python_(programming_language)',
		'https://en.wikipedia.org/wiki/Pdfsthon_(mythology)',
	],
	'Wikipedia3' : [
		'https://en.wikipedia.org/wiki/Python_(film)',
		'https://en.wikipedia.org/wiki/Python_(programming_language)',
		'https://en.wikipedia.org/wiki/Pdfsthon_(mythology)',
	],
}

tested_urls, successful, failed = 0, 0, 0

def doesURLwork(url):
	try:
		response = urllib.request.urlopen(url)
		if response.code == 200:
			return True
		else:
			return False
	except urllib.error.URLError:
		return False
	else:
		return False

for name, urls in site.items():
	print("\n" + name)
	for u in urls:
		result = doesURLwork(u)
		if result == True:
			print(u + Fore.GREEN + "\t[OK]")
			successful += 1
		else:
			print(u + Fore.RED +"\t[FAIL]")
			failed += 1
		tested_urls += 1

print('\nURLs tested: ' + str(tested_urls) + ' | Successful: ' + str(successful) + ' | Failed: ' + str(failed))