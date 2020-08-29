import re
import sys

input = sys.stdin.readline

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
official = ['Before 02/03/04, but not after December 19, 99,', 'there was a rehash of the 55.34.02 meeting. A date, like November 15,', '95 cannot traverse two lines, nor can it be surrounded by alphabetics', 'or numerics like this: 78November 01, 88, or 6801/12/03, or 02/03/04x.', 'January 01, 25 February 28, 99', ' MMarch 20, 24 March 89,24...April 0, 00 May 99, 01 this is it', 'March 2A, 12 March 21, 12 March 21, 1A April 8, 8 April 08, 08', 'April 8, 8 May 01,01 June 30, 89, December 01/02/03', '01.02.03 99.02.04 02.99.04 02.04.99', 'January 02, 02', 'January 02,', 'December 31, 99', '02/03/04', '99.11.11', '', 'hello there', 'Before 02/03/2004, but not after December 19, 1999,']

for i in range(int(input())):
	line = input().rstrip()
	tokens = [token for token in re.split(r'(\s+)', line)]
	for i in range(len(tokens)):
		if re.match('''(^\d{2}/\d{2}/\d{2}[!\"#$%&'()*+, -.\/:;<=>?@[\]^_`{|}~]*$)''', tokens[i]): # check if date format is valid
			if 1 <= int(tokens[i][0:2]) <= 31 and 1 <= int(tokens[i][3:5]) <= 12: # check if date is valid
				year = int(tokens[i][6:8])
				if year <= 24:
					tokens[i] = tokens[i][:6] + "20" + tokens[i][6:8] + tokens[i][8:]
				else:
					tokens[i] = tokens[i][:6] + "19" + tokens[i][6:8] + tokens[i][8:]
		elif re.match('''(^\d{2}\.\d{2}\.\d{2}[!\"#$%&'() *+, -.\/:;<=>?@[\]^_`{|}~]*$)''', tokens[i]):
			if 1 <= int(tokens[i][3:5]) <= 12 and 1 <= int(tokens[i][6:8]) <= 31: # check if date is valid
				year = int(tokens[i][0:2])
				if year <= 24:
					tokens[i] = "20" + tokens[i]
				else:
					tokens[i] = "19" + tokens[i]
		elif tokens[i] in months and (len(tokens) - i) >= 5:
			if re.match('''(^\d{2}[!\"#$%&'()*+, -.\/:;<=>?@[\]^_`{|}~]*$)''', tokens[i+2]) and re.match('''(^\d{2}[!\"#$%&'()*+, -.\/:;<=>?@[\]^_`{|}~]*$)''', tokens[i+4]): # check if date format is valid
				if 1 <= int(tokens[i+2][0:2]) <= 31: # check if date is valid
					year = int(tokens[i+4][0:2])
					if year <= 24:
						tokens[i+4] = "20" + tokens[i+4]
					else:
						tokens[i+4] = "19" + tokens[i+4]
	if tokens != [""]:
		print("".join(tokens))
	else:
		print("")