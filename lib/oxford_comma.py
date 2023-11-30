def oxford_comma(items):
    firstWords = ", ".join(items[0:len(items)-1])
    if len(items) > 2:
        sentence = firstWords + ", and " + items[-1]
    elif len(items) == 2:
        sentence = firstWords + " and " + items[-1]
    else:
        return items[0]
    
    return sentence
