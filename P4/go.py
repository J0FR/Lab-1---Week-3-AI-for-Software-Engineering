def reverse_string(s):
    return s[::-1]

def main():
    input_str = "Hello, World!"
    reversed_str = reverse_string(input_str)
    print("Original:", input_str)
    print("Reversed:", reversed_str)

if __name__ == "__main__":
    main()