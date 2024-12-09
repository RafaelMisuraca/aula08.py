def eh_palindromo(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

print(eh_palindromo("palindromo"))  
print(eh_palindromo("python"))
print(eh_palindromo("ana"))
print(eh_palindromo("abraao"))  
print(eh_palindromo("e"))
print(eh_palindromo("aaaaaaaaaaa"))     