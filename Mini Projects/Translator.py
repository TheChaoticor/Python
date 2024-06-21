def translate(phrase):
    translation=""
    for i in phrase:
        if i in "AEIOUaeiou":
            translation=translation+'g'
        else:
            translation+=i    
    return translation    
        
print(translate("Goodness"))        