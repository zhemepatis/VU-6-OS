class Interface:
    # MENU
    def print_menu_list(self, title, list):
        length = len(list)

        if title != None:
            print(f"\n{title} menu:")

        for idx in range(length):
            print(f"{idx+1}. {list[idx]}")

    def get_menu_choice(self):
        choice = input("Choose an option: ")
        try:
            choice = int(choice)
        except: 
            return -1
        
        return choice
    
    def main_menu(self):
        title = "Main"
        menu = [
            "Run a program",
            "Change operation mode",
            "Exit"
        ]

        self.print_menu_list(title, menu)
        return self.get_menu_choice()
    
    def step_by_step_menu(self):
        title = "Main"
        menu = [
            "Execute next command",
            "Print CPU state",
            "Print Memory state",
            "Exit step-by-step mode"
        ]

        self.print_menu_list(title, menu)
        return self.get_menu_choice()
    
    # OTHER PRINTING
    def print_cpu(self, cpu):
        pass

    def print_real_memory(self, memory):
        pass

    def print_vm_memory(self, memory):
        pass

    def print_invalid_option(self):
        print("Invalid choice. Try again!")

    def print_vm_exit(self):
        print("Exiting VM.")