def isPalindrome(word):
  return word == word[::-1]


# get an input from the user

n=int(input("Enter the number"))
print(isPalindrome(n))
