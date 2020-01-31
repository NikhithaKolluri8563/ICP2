def string_alternative():
    alternative = ""
    str = input("Please enter any string")
    for i in range(len(str)):
        if (i%2) == 0 :
            alternative+=(str[i])
    print (alternative)

string_alternative()