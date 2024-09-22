
def reverse_name(name):
    
    """Return the reversed version of the name."""
    
    return name[::-1]

def main():
    user_name = input("Enter your name: ")
    reversed_name = reverse_name(user_name)
    
    print(f"Your name in reverse is: {reversed_name}")

if __name__ == "__main__":
    main()
