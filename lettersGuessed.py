def getAvailableLetters(lettersGuessed):
    import string
    lowercase = string.ascii_lowercase
    for d in lettersGuessed:
            for a in lowercase:
                if a == d:
                    lowercase = lowercase.replace (d,"")
    return(lowercase)
            
            