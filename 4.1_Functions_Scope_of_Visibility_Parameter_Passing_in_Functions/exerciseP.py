def is_palindrome(x):
    
    if isinstance(x, int):
        return True if str(x) == str(x)[::-1] else False
    
    if isinstance(x, str):
        x = "".join(char for char in x if char.isalnum()).lower()
        return True if x == x[::-1] else False
    
    if isinstance(x, tuple) or isinstance(x, list):
        return True if x == x[::-1] else False


if __name__ == "__main__":
    result = is_palindrome([1, 2, 1, 2, 1])
    print(result)