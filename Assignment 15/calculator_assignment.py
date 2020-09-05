"""
Create a Calculator Util Class and perform following

Step 1: Create a class to do calculator utils
Step 2: Design function to show welcome message
Step 3: Designs a function show operations
    a : 1 -> Addition
    b : 2 -> Subtraction
    c : 3 -> Multiplication
    d : 4 -> division
    e : 5 -> remainder
Step 4 : Ask user to enter input and return the input option
Step 5 : Validate the input option
    a : If valid take input
    b : else throw invalid option exception
Step 6 : Create function to ask user two numbers and return the numbers
Step 7 : Create function for addition and return sum result
Step 8 : Create function for subtraction and return difference result
Step 9 : Create function for multiplication and return product result
Step 10 : Create function for division
    a : If second value is zero throw invalid input Exception
    b : else return division result
Step 10 : Create function for division
    a : If second value is zero throw invalid input Exception
    b : else return remainder result
Step 11: creation function to perform operation and print the result
Step 12 : Create function to display continue message and return boolean
Step 13 : Create function to display thank you message
Step 14: Create function to run application
    a : call welcome message
    b : call option message
    c : call get option
    d : call validate option
    e : call input data
    f : call operation and pass option and inputs
    g : call run again option in case true start from b
    f : incase false display thank you message
"""


# Create exception to handle calculator
class CalculatorException(Exception):
    """
    This is the exception class helps to raise in
    order to avoid business
    """

    def __init__(self, message):
        """
        This is constructor for exception message
        :message: to provide message for the exception
        """
        super(CalculatorException, self).__init__()
        self.message = message


# Step 1: To create a calculator util class
class CalculatorUtil:
    """
    This class helps to create util functions for the calculator
    """

    # Step 2: Design function to show welcome message
    def welcome_message(self):
        """
        This function helps to print the welcome message
        :return: none
        """
        print('Welcome to the calculator class! Enjoy the app')

    #     Step 3: Designs a function show operations
    #     a : 1-> Addition
    #     b : 2 -> Subtraction
    #     c : 3 -> Multiplication
    #     d : 4 -> division
    #     e : 5 -> remainder
    def show_options(self):
        """
        This function helps in printing the option to the user
        :return: none
        """
        print("Please choose below shown options:\n")
        print("1 -> Addition")
        print("2 -> Subtraction")
        print("3 -> Multiplication")
        print("4 -> Division")
        print("5 -> Remainder")

    # Step 4 : Ask user to enter input and return the input option
    def get_user_options(self):
        """
        This function helps to get the user input for the above mentioned operations
        :return: user selected option as int
        """
        return int(input("Choose any one option from the above mentioned options:\n"))

    # Step 5 : Validate the input option
    #     a : If valid take input
    #     b : else throw invalid option exception
    def validate_user_input(self, user_options: int):
        """
        This function will validate the option the user has selected
        :return: True if valid else it will throw invalid option
        """
        if user_options < 1 or user_options > 5:
            raise CalculatorException('Invalid option, accepted option range from 1 to 5')
        return True

    # step 6 : Create function to ask user two numbers and return the numbers
    def get_input(self):
        """
        This function asks user to enter two input
        :return: (int, int) for operation
        """
        print('Enter the input to perform the operation')
        num1 = int(input("Enter the first number\n"))
        num2 = int(input("Enter the second number\n"))
        return num1, num2

    # Step 7 : Create function for addition and return sum result
    def addition(self, num1, num2):
        """
        This function will perform the addition operation
        :num1: The first number to be added
        :num2: The second number to be added
        :return: The sum of the values
        """
        return num1 + num2

    # Step 8 : Create function for subtraction and return difference result
    def subtraction(self, num1, num2):
        """
        This function will perform the subtraction operation
        :num1: The first number to be subtracted
        :num2: The second number to be subtracted
        :return: The difference of the values
        """
        return num1 - num2

    # Step 9 : Create function for multiplication and return product result
    def multiplication(self, num1, num2):
        """
        This function will perform the multiplication operation
        :num1: The first number to be multiplied
        :num2: The second number to be multiplied
        :return: The product of the values
        """
        return num1 * num2

    # Step 10 : Create function for division
    #     a : If second value is zero throw invalid input Exception
    #     b : else return division result
    def division(self, num1, num2):
        """
        This function will perform the division operation
        :num1: The dividend
        :num2: The divisor
        :return: The quotient of the values
        :raise: CalculatorException for the divisor being '0'
        """
        if num2 == 0:
            raise CalculatorException("Divisor can't be 0")

        return num1 / num2

    # Step 10 : Create function for remainder
    #     a : If second value is zero throw invalid input Exception
    #     b : else return remainder result
    def remainder(self, num1, num2):
        """
        This function will perform the remainder operation
        :num1: The dividend
        :num2: The divisor
        :return: The remainder of the values
        :raise: CalculatorException for the divisor being '0'
        """
        if num2 == 0:
            raise CalculatorException("Divisor can't be 0")

        return num1 % num2

    # Step 11: create a function to perform operation and print the result
    def perform_operation(self, options, num1, num2):
        """
        This helps us to perform the calculator operation based on the options chosen
        :options: The selected operation
        :num1: Input 1
        :num2: Input 2
        :return: none
        """
        try:
            result = 0
            if options == 1:
                result = self.addition(num1, num2)
            elif options == 2:
                result = self.subtraction(num1, num2)
            elif options == 3:
                result = self.multiplication(num1, num2)
            elif options == 4:
                result = self.division(num1, num2)
            else:
                result = self.remainder(num1, num2)
            print('Your Result is :', result, sep="\t")
        except CalculatorException as c:
            print('Something went wrong!')
            print(c.message)

    #   Step 12 : Create function to display continue message and return boolean
    def continue_message(self):
        """
        This function will ask the user if he wants to run the code again ot not
        :return: True if user enters y/yes or False
        """
        print("Do you want to continue?", "Type Yes or y", "Else press any other values", sep="\n")
        option = input("Type your option\n")
        return option == "Yes" or option == "Y" or option == "y" or option == "yes"

        #   Step 13 : Create function to display thank you message

    def thank_you_message(self):
        """
        This function will print the thank you message
        :return: none
        """
        print('Thank you for using our calculator application. You can visit us again')

    # Step 14: Create function to run application
    #     a : call welcome message
    #     b : call option message
    #     c : call get option
    #     d : call validate option
    #     e : call input data
    #     f : call operation and pass option and inputs
    #     g : call run again option in case true start from b
    #     f : incase false display thank you message
    def run_application(self):
        """
        This is the main starting code of our application which will run the calculator algorithms
        """
        self.welcome_message()
        while True:
            try:
                self.show_options()
                options = self.get_user_options()

                if self.validate_user_input(options):
                    num1, num2 = self.get_input()
                    self.perform_operation(options, num1, num2)

            except CalculatorException as c:
                print("Something went wrong!")
                print(c.message)
            if not self.continue_message():
                break
        self.thank_you_message()


if __name__ == '__main__':
    '''
    This main function to test calculator application running code
    '''
    util = CalculatorUtil()
    util.run_application()
