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
        This is constructor
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

    # step 6 : Create function to ask user two numbers and return the numbers
    def get_input(self):
        """
        This function asks user to enter two input
        :return: (int, int) for operation
        """
        print('Bellow are the mentioned options:')
        print('1 -> Addition')
        print('2 -> Subtraction')
        print('3 -> Multiplication')
        print('4 -> Division')

    def get_numbers(num1=0, num2=0):
        """
        :param num1: the first number
        :param num2: the second number
        :return: none
        """
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

    # step 7 : Create function for addition and return sum result
    def addition(num1=0, num2=0):
        """
        This function performs addition and returns addition result
        :param num1: input 1
        :param num2: input 2
        :return: sum
        """
        print(num1 + num2)

    # step 8 : Create function for subtraction and return difference result
    def subtraction(num1=0, num2=0):
        """
        This function performs subtraction and returns subtraction result
        :param num1: input 1
        :param num2: input 2
        :return: difference
        """
        print(num1 - num2)

    # step 9 : Create function for multiplication and return product result
    def multiplication(num1=0, num2=0):
        """
        This function performs multiplication and multiplication addition result
        :param num1: input 1
        :param num2: input 2
        :return: product
        """
        print(num1 * num2)

    # step 10 : Create function for division
    #     a : If second value is zero throw invalid input Exception
    #     b : else return division result
    def division(num1=0, num2=0):
        """
        This function performs division and returns division result
        :param num1: input 1
        :param num2: input 2
        :return: quotient
        :raises: CalculatorException when num2 == 0
        """
        try:
            print(num1 / num2)
        except:
            return ('Second value can\'t be \'0\'')
            CalculatorUtil().division()

    # step 10 : Create function for remainder
    #     a : If second value is zero throw invalid input Exception
    #     b : else return remainder result
    def remainder(num1, num2):
        """
        This function performs remainder and returns remainder result
        :param num1: input 1
        :param num2: input 2
        :return: remainder
        :raises: CalculatorException when num2 == 0
        """
        print(num1 % num2)


    # Step 13 : Create function to display thank you message
    def thank_you_message(self):
        """
        This method helps to print thank message and see you soon
        :return: none
        """
        print('Thank you for trying the code!')

    def run_application(inp, num1, num2):
        """
        This functions run the main application code
        :return: none
        """
        # Step 14: Create function to run application

        # a : call get numbers
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        # b : call get option
        CalculatorUtil.get_input()
        inp = int(input('5 -> Remainder\n'))
        if inp == 1:
            print(num1 + num2)
        elif inp == 2:
            print(num1 - num2)
        elif inp == 3:
            print(num1 * num2)
        elif inp == 4:
            print(num1 / num2)
        elif inp == 5:
            print(num1 % num2)
        else:
            print('Invalid input! Please input only the numbers from \'1\' to \'5\'')
        CalculatorUtil.thank_you_message()

if __name__ == '__main__':
    '''
    This main function to test calculator application running code
    '''
    CalculatorUtil.run_application(inp, num1, num2)
