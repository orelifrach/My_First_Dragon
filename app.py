from pet import Pet


class app:
    def __init__(self):
        type = input(f"""Enter the pet type from the list
{Pet.get_pet_type_list(Pet)}: """)
        while not Pet.verify_type(Pet, type):
            type = input(f"""The requested type is not found in the list,
                Enter the pet type from the list
                {Pet.get_pet_type_list(Pet)}: """)

        name = input("Enter the pet's name: ")
        while not Pet.verify_name(Pet, name):
            name = input(
                "The name must be 2-9 chars long and contain only letters,"
                "Enter the pet's name: "
            )

        self._pet = Pet(name, type)
        self.start_game()

    def input_action(self):
        actions_list = Pet.get_actions_list(Pet) + ["exit"]
        actions_str = ""
        for i in range(len(actions_list)):
            actions_str += f"{i+1} - {actions_list[i]}\n"
        output_str = (
            "Enter the number of the requested action:\n"
            f"{actions_str}"
        )
        # Check if the input is a digit and if the digit is valid
        requested_action_str = ""
        is_valid = False
        while not is_valid:
            while not requested_action_str.isdigit():
                requested_action_str = input(
                    "The number of the requested action has to be a digit "
                    f"fronmt he options,\n{output_str}"
                )
            if not 0 < int(requested_action_str) <= len(actions_list):
                is_valid = False
                requested_action_str = input(
                    "The number of the requested action has to be a digit "
                    f"from the options,\n{output_str}"
                )
            else:
                is_valid = True
        return int(requested_action_str)

    def start_game(self):
        requested_action_num = self.input_action()
        while requested_action_num != 6:  # exit
            if requested_action_num == 1:  # eat
                self._pet.eat()
            elif requested_action_num == 2:  # sleep
                self._pet.sleep()
            elif requested_action_num == 3:  # play
                self._pet.play()
            elif requested_action_num == 4:  # state
                self._pet.state()
            elif requested_action_num == 5:  # status
                print(self._pet)
            requested_action_num = self.input_action()
        print("The game is over!")


if __name__ == "__main__":
    app()
