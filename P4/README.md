# P4

### Ruby snippet:

**Prompt:**
I need you to translate the following code to python code.

```
def menu()
    menu_string = "1. Show Menu\n"
    menu_string += "2. Add Numbers\n"
    menu_string += "3. Subtract Numbers\n"
    menu_string += "4. Quit\n"
    return menu_string
  end

  # Main Program Starts

  system "clear" # Clear the screen
  choice = 0

  while choice < 4 do
    puts menu()
    choice = gets.to_i

    if choice == 1
      system "clear"
    elsif choice == 2
      puts "\n\nAdd Some Numbers\n\n"
    elsif choice == 3
      puts "\n\nSubtract some Numbers\n\n"
    else
    end
  end
```

Do not give me any description, I just need the code.

**Response:**

```
import os

def menu():
    menu_string = "1. Show Menu\n"
    menu_string += "2. Add Numbers\n"
    menu_string += "3. Subtract Numbers\n"
    menu_string += "4. Quit\n"
    return menu_string

# Main Program Starts

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
choice = 0

while choice < 4:
    print(menu())
    choice = int(input())

    if choice == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
    elif choice == 2:
        print("\n\nAdd Some Numbers\n\n")
    elif choice == 3:
        print("\n\nSubtract some Numbers\n\n")
    else:
        pass
```

---

### Javascript/NodeJS snippet:

**Prompt:**
I need you to translate the following code to python code.

```
const generateUUID = () =>
	([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, (c) =>
		(
			c ^
			(crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (c / 4)))
		).toString(16)
	);
```

Do not give me any description, I just need the code.

**Response:**

```
import os

def generate_uuid():
    def random_byte():
        return os.urandom(1)[0]

    def randomize(c):
        return c ^ (random_byte() & (15 >> (c // 4)))

    uuid_format = [1e7, -1e3, -4e3, -8e3, -1e11]
    uuid_string = ''.join(format(int(part), 'x') for part in uuid_format)

    return ''.join(
        format(randomize(int(c, 16)), 'x') if c in '018' else c
        for c in uuid_string
    )

# Example usage
print(generate_uuid())
```

---

### Golang snippet:

**Prompt:**
I need you to translate the following code to python code.

```
package main

import "fmt"

func ReverseString(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}

func main() {
    input := "Hello, World!"
    reversed := ReverseString(input)
    fmt.Println("Original:", input)
    fmt.Println("Reversed:", reversed)
}
```

Do not give me any description, I just need the code.

**Response:**

```
def reverse_string(s):
    return s[::-1]

def main():
    input_str = "Hello, World!"
    reversed_str = reverse_string(input_str)
    print("Original:", input_str)
    print("Reversed:", reversed_str)

if __name__ == "__main__":
    main()
```

---
