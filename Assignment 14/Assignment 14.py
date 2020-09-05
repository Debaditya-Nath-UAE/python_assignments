"""
1 Accessing your bio data from the file
1) Write A bio data write to a file
2) Read the bio data to the file
3) Update new content to the file
4) Simultaneously access and write to the file

2 Download the csv, html, tsv file from online
1) Read the content from the file
2) Print the content from the file

3 Download story from the site do the String operation
"""


# Display welcome message
def display_welcome_message():
    """
    Display welcome message to the user
    :return:
    """
    print("Welcome to bio data application. Enjoy the app.")


# Function to display
def display_user_option():
    """
    This method provide user options for the application
    1 -> Read
    2 -> Write
    Else -> Invalid case to display please enter proper
    :return: none
    """
    print("Enter below mentioned options to the following task\n")
    print("1 -> Read From File")
    print("2 -> Write to a file")


# Function to get user options
def get_user_options():
    """
    This method helps to get user input
    :return: user options in int
    """
    return int(input("Enter your options below \n"))


# Write a bio data
def write_bio_data(filename, biodata):
    """
    This functions helps me to write a bio data to a file
    :param filename: pass name of the file
    :param biodata: require bio data as a string
    :return: none
    """
    with open(filename, 'w+') as f:
        f.write(biodata)
    print('The text was written succesfully! Now you can check the file')


# Read bio data
def read_bio_data(filename):
    """
    This function helps me read
    bio data from the give file
    :param filename: name of the file to read
    :return: none
    """
    print('The content in the text file is:')
    with open(filename, 'r+') as f:
        data = f.read()
        print(data)


# Get input for information from the user
def get_user_input(user=0):
    """
    Here we are getting user input based on  type
    :param write: true for getting bio data
    :return: maps of the input
    """
    user_data = {}
    user_data['fileName'] = input("Enter the file name\n")
    if user == 2:
        user_data['bioData'] = input("Enter your bio data\n")
    return user_data


# Require function to ask user to continue
def display_continue_message_to_ask():
    """
    This functions to ask the user to continue
    :return: true if continue else false
    """
    return bool(input('Would you like to continue(enter \'True\' or \'False\'):\n'))


# Display a function to thanks a user
def thank_message():
    """
    This function display thanks
    :return: none
    """
    print('Thank you for trying this code! Hope you enjoyed it')


# Require main to app
def run_application():
    """
    This is main code to execute the task
    All functions of bio data
    :return: none
    """
    to_continue = True
    # Step1 : Welcome user for applications
    display_welcome_message()
    while to_continue:
        # Step2 : Display an get the options from the user the user
        display_user_option()
        # Step3 : Get user options
        user_options = get_user_options()
        # Step4 : Validate user options
        #   a) For Invalid Options
        if user_options < 0 or user_options > 2:
            print("invalid options choose please choose the valid options")
        #   b) For Valid Options
        else:
            # Step5 : Get User Data for persisting or retrieving
            #   a : 1 -> read data from the file
            #   b : 2 -> write data to the file
            user_data = get_user_input(user_options)
            if user_options == 1:
                read_bio_data(user_data['fileName'])
            else:
                write_bio_data(user_data['fileName'], user_data['bioData'])
        # Step6 : Check user wants to continue read or writing the applications
        #   a: Returns True continue from step2
        #   b: False display thank you message
        to_continue = display_continue_message_to_ask()

    # Step7: Display thank you message
    thank_message()


# Checks if your running the main code then run the application
if __name__ == "__main__":
    run_application()