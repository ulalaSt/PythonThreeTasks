
#checks if the number is Palindrome
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    value = str(x)
    l = len(value)
    mid = int(l/2)
    for i in range(mid):
        if value[i]!=value[l-1-i]:
            return False
    return True


#finds string length recursively
def stringLength(s: str) -> int:
    if not s:
        return 0
    return 1 + stringLength(s[1:])


#sorts array by quickSort method
def quickSort(array: [int]) -> [int]:
    length = len(array)
    if length <= 1:
        return array
    pivot = array.pop()
    left = []
    right = []
    
    for each in array:
        if each < pivot:
            left.append(each)
        else:
            right.append(each)
    return quickSort(left)+[pivot]+quickSort(right)

number = 123321
print(number ,"isPalindrome:", isPalindrome(number))

string = "asasda"
print("'"+string+"'", "stringLength:", stringLength(string))

array = [3,4,2,5,245,2,6,8]
print(array, "quickSort:", quickSort(array))
