def generate_permutations(string):
    if not string:
        print("Error: The input string is empty.")
        return []

    if len(string) == 1:
        return [string]
    
    permutations = []
    
    for i in range(len(string)):
        current_char = string[i]
        
        remaining_string = string[:i] + string[i+1:]
        
        for perm in generate_permutations(remaining_string):
            permutations.append(current_char + perm)
    
    return permutations


if __name__ == "__main__":
    user_input = input("Enter a string to generate its permutations: ")
    try:
        result = generate_permutations(user_input)
        if result:
            print(f"Permutations of '{user_input}':")
            for perm in result:
                print(perm)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
