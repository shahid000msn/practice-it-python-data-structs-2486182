from collections import deque 
def check_palindrome(word):
    d= deque(word.lower())
    while len(d)>1:
        if d.pop() != d.popleft():
            print(len(d))
            return False
    return True

def main():
    #add code here
    word = "toccot"
    print(check_palindrome(word))
    return

if __name__ == "__main__":
    main()