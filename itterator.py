import os
import time
from colorama import Fore

banner = r""" ______   __                                    __                         
|      \ |  \                                  |  \                        
 \$$$$$$_| $$_     ______    ______   ______  _| $$_     ______    ______  
  | $$ |   $$ \   /      \  /      \ |      \|   $$ \   /      \  /      \ 
  | $$  \$$$$$$  |  $$$$$$\|  $$$$$$\ \$$$$$$\\$$$$$$  |  $$$$$$\|  $$$$$$\
  | $$   | $$ __ | $$    $$| $$   \$$/      $$ | $$ __ | $$  | $$| $$   \$$
 _| $$_  | $$|  \| $$$$$$$$| $$     |  $$$$$$$ | $$|  \| $$__/ $$| $$      
|   $$ \  \$$  $$ \$$     \| $$      \$$    $$  \$$  $$ \$$    $$| $$      
 \$$$$$$   \$$$$   \$$$$$$$ \$$       \$$$$$$$   \$$$$   \$$$$$$  \$$   v1.2
                         .:: github @cyberm0n ::.
"""
 
print(Fore.BLUE+banner+Fore.WHITE)

progress = input("["+Fore.YELLOW+"?"+Fore.WHITE+"]"+" progress (Exm:python hello.py) >>> ")
count = input("["+Fore.YELLOW+"?"+Fore.WHITE+"]"+" loop count (forever = 0) >>> ")
timex = int(input("["+Fore.YELLOW+"?"+Fore.WHITE+"]"+" second (this can be 0) >>> "))
def whi():
	a = 1
	while True:
		time.sleep(timex)
		try:
			os.system(progress)
			print("["+Fore.BLUE+"*"+Fore.WHITE+"]"+" Count> "+str(a))
			a += 1
		except:
			print("["+Fore.RED+"!"+Fore.WHITE+"]"+" Finished..")


def fo():
	a = 1
	for i in range(1,(int(count)+1)):
		time.sleep(timex)
		try:
			os.system(progress)
			print("["+Fore.BLUE+"*"+Fore.WHITE+"]"+" Count> "+str(i))
			a += 1
		except:
			print("["+Fore.RED+"!"+Fore.WHITE+"]"+" Finished...")
			
def start():
	if count == "0":
		whi()
	else:
		try:
			fo()
			print("["+Fore.RED+"!"+Fore.WHITE+"]"+" Finished!")
		except:
			print("["+Fore.RED+"!"+Fore.WHITE+"]"+" Failure!")

if __name__ == '__main__':
    start()
