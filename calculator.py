from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number? "))
  
  for op in operations:
      print(op)
  
  doin_it = True
  
  while doin_it:
    
    operations_op = input("Pick an operation: ")
    
    num2 = float(input("What's the next number? "))
    
    calc = operations[operations_op]
    answer = calc(num1, num2)
    
    print(f"{num1} {operations_op} {num2} = {answer}")
    
    decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    if decision == "y":
      num1 = answer
    elif decision == "n":
      doin_it = False
      calculator()

calculator()
