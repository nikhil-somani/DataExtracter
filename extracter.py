#import regular expression module
import re

#define parse_name function taking a text as a argumemt
def parse_name(text):
  #split the given line separator as whitespaces, results in a list of data
  name = text.split()
  #first element of name will be first name, 
  first_name = name[0]
  #second element of this list name will be last name
  last_name = name[1]
  #return those firstname and lastname of employee.
  return first_name, last_name

#define parse address function taking a text as a argument
def parse_address(text):
  #again split the data into a list separator: whitespaces
  name = text.split()
  #now first two element will be name and last element will be email thus
  #remaining iin between is address and can be accessed using list slice index 2 to second last index
  address = name[2:-1]
  #return the address in a string format
  return ' '.join(address)

#define parse_email function taking a text as argument
def parse_email(text):
  #define the regex expression
  regex = r'\b[\w.-]+?@\w+?\.\w+?\b'
  #findall email from given text using regex, returns list of all email present in text.
  emails = re.findall(regex,text)
  #first element will be the required and only email
  return emails[0]

#define the class address
class address():
  #define constructor,taking addr as input and parse it
  def __init__(self, addr):
    #split the text into list of data
    address = addr.split()
    #first element will be street
    self.street = address[0]
    #first element will be city
    self.city = address[-2]
    #last element will be state
    self.state = address[-1]

#define the class employee
class employee():
  #define constructor, take the line from main() and set its variables
  def __init__(self, content):
    #take the content and store it 
    self.content = content
    #call parse_name to get return of firstname and lastname and store them for that instance
    self.first_name, self.last_name = parse_name(self.content)
    #call parseaddress to parse the content for address 
    self.address = parse_address(self.content)
    #create instance of address for each instance of employee
    #this will parse address into city, state and street in address class
    c = address(self.address)
    #call the parse email function to get in return the email.
    self.email = parse_email(self.content)

#define the main function take path as argument
def main(path):
  #create employee list
  employee_list = []
  #open the file for given path
  with open(path) as f:
    #read the complete content
    contents = f.readlines()
  #for each line in content
  for line in contents:
    #create instance of employee passing that line as argument 
    a = employee(line)
    #append the instance to employee list
    employee_list.append(a)
  #print the employee list length
  print(len(employee_list))



#calling main function
if __name__ == '__main__':
  #file should be in current directory or can provide the path of 
  #people.txt file.
  path = "people.txt"
  #calling main function passsing path in argument
  main(path)


