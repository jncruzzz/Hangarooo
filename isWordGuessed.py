def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for a, b in enumerate(secretWord):
    	if b in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False