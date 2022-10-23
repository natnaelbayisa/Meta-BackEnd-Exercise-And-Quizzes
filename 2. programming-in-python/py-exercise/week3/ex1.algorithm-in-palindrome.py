
def palindrome(y):
    for i in range(0, int(len(y)/2)):                                 
        if y[i] != y[len(y)-i-1]:
            return False
    
    return True
        
print(palindrome("alula"))


def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True


print(isPalindrome("racecar"))


