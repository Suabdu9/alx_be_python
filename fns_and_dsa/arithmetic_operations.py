def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num2 == 0:
                print("you've tried to divide a number by zero!")
            elif num1 == 0 :
                print("Zero divided by any number is zero!")
            else:
                result = num1 / num2
    return result
    
