for count in range(1,101):
    if count%5==0 and count%3==0:
        print("FIZZBUZZ")
    elif count%3==0:
        print("FIZZ")
    elif count%5==0:
        print("BUZZ")
    else:
        print(count)