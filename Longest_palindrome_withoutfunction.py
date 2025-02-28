def palindrome(s):
    n=len(s)
    max_length=0
    subs=" "
    
    for i in range(n):
        for j in range(i,n):
            abc=s[i:j+1]
            abc1=abc[::-1]
            if abc==abc1:
                subs_length=len(abc)
                if subs_length > max_length:
                    subs=abc
                    
    return subs

s = "babad"  
result = palindrome(s)  
print("Longest Palindromic Substring:", result)  

                    
                
