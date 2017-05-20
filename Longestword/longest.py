def main():
    temp = ""
    maxlen = 0
    maxword = ""
    a = input("Enter your string\n")
    a = a + " "
    l = len(a)
    for i in a:
        if not i == " ":
            temp = temp + i
            continue


        if len(temp) > maxlen:
            maxword = temp
            maxlen = len(temp)
        temp = ""
    print('longest word', maxword)
    print('length', maxlen)
    


if __name__ == '__main__':
    main()

