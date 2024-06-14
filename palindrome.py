def is_palindrome(s):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def main():
    print("Welcome to the Palindrome Checker!")
    while True:
        # Get input from the user
        user_input = input("Enter a string to check (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Check if the string is a palindrome
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome!")
        else:
            print(f"'{user_input}' is not a palindrome.")
        
        # Ask if the user wants to revise their input
        revise = input("Would you like to revise your input? (yes/no): ").lower()
        if revise == 'yes':
            user_input = input("Enter the revised string: ")
            
            # Check the revised string
            if is_palindrome(user_input):
                print(f"'{user_input}' is a palindrome!")
            else:
                print(f"'{user_input}' is not a palindrome.")
        
        # Ask if the user wants to check another string
        again = input("Would you like to check another string? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()