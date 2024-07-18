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
  