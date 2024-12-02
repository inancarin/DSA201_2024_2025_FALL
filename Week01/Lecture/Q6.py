def timeInWords(h, m):
    # Write your code here
    d = {1:'one' , 2 : 'two' , 3 : 'three' , 4 : 'four' , 5: 'five' , 6:'six' , 7 : 'seven' , 8:'eight' , 9:'nine' , 0: 'zero',
    10:"ten", 11:"eleven",12:"twelve",13:"thirteen",14:"fourteen", 15:"fifteen",
    16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen",20:"twenty",30:"thirty"}

    if m == 0:
        return d[h] + " o' clock"
    elif m == 30:
        return "half past " + d[h]
    else:
        output_middle = " past "
        if m > 30:
            output_middle = " to "
            h += 1
            if h == 13:
                h = 1
            m = 60 - m
        if m < 10:
            output_pre = d[m] + " minute"
            if m > 1:
                output_pre += "s"
        elif m == 15:
            output_pre = "quarter"
        elif m < 20:
            output_pre = d[m] + " minutes"
        else:
            last_digit = m % 10
            decimal = m - last_digit
            if last_digit == 0:
                output_pre = d[decimal] + " minutes"
            else:
                output_pre = d[decimal] + " " + d[last_digit] + " minutes"
        return output_pre + output_middle + d[h]
        

# main
timeInWords(10, 57)