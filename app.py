from pet import Pet

class app():
    def __init__(self):
        type = input(f"""Enter the pet type from the list
{Pet.get_pet_type_list()}: """)
        while not Pet.verify_type(type):
            type = input(f"""The requested type is not found in the list,
Enter the pet type from the list
{Pet.get_pet_type_list()}: """)
    
        name = input("Enter the pet's name: ")
        while not Pet.verify_name(name):
            name = input("""The name must be 2-9 chars long and contain only letters,
Enter the pet's name: """)
        
        self.pet = Pet(name, type)
        self.play()
        
    def play(self):
        actions_list = Pet.get_actions_list()
        actions_str = ""
        for i in range(len(actions_list)):
            actions_str += f"{i+1} - {actions_list[i-1]}\n"
        output_str = "Enter the number of the requested action:\n" + actions_str
        # Check if the input is a digit and if the digit is valid
        requested_action_str = ""
        while not 0 < requested_action_str <= len(actions_list):
            requested_action_str = input(output_str)
            while not requested_action_str.isdigit():
                requested_action_str = input(f"The number of the requested action is not a digit\n{output_str}")
            if not 0 < requested_action_str <= len(actions_list):
                requested_action_str = input(f"The number of the requested action was out of range\n{output_str}")
        requested_action_num = int(requested_action_str)
        
        # while True:
        #     if requested_action == 1:
        #     elif requested_action == 2:
        #     elif requested_action == 3:
##להמשיך מפה לממש את ממשק המשחק למשתמש

app()