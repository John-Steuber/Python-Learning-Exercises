#QUESTION 1
print("1. What is seven to the power of four?")
print(7**4)

#QUESTION 2
print("2. Split the following string into a list")
s = "Hi there Sam!"
print(s)
print(s.split())

#QUESTION 3
print("3. Given the following variables, use .format() to print the following string:")
print("The diameter of the Earth is 12742 Kilometers")

planet = "Earth"
diameter = 12742

print(planet)
print(diameter)
print('The diameter of the is {} Kilometers {}'.format(planet, diameter))

#QUESTION 4
print("4. Given this nested list, use indexing to grab the word hello")

lst = [1, 2, [3,4], [5, [100,200, ['hello']], 23,11], 1,7]

print(lst)
print(lst[3][1][2][0])

#QUESTION 5
print("5. What is the difference between a tuple and a list?")
print("Tuples are immutable, meaning they cannot be changed. Lists are mutable.")

#QUESTION 6
print("6. Create a function that grabs the email website domain from a string in the form: user@domain.com")

def domain_grabber(x):
    return x.split('@')[1]

domain_grabber('caffeine@coffee.com')

#QUESTION 7
print("7. Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization")

def dog_catcher(x):
    return 'dog' in x.lower().split()

dog_catcher('Do I love my dog')

#QUESTION 8
print("8. Create a function that counts the number of times the word dog occurs in a string. Again ignore edge cases.")

def dog_counter(x):
    y = 0
    for word in x.lower().split():
        if word == 'dog':
            y += 1
    return y

dog_counter('i like my dog my dog is my favorite dog')

#QUESTION 9
print("9. Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.")

seq = ['soup','dog','salad','cat','great']
list(filter(lambda item: item[0] == 's', seq))

#QUESTION 10
print("10. You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: No ticket, Small ticket, or Big Ticket."
      "If your speed is 60 or less, the result is No Ticket. If speed is between 61 and 80 inclusive, the result is Small Ticket. If speed is 81 or more, the result is Big Ticket."
      "Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases. ")

def speeding(speed, is_bday):
    if  is_bday:
        speed = speed - 5
    if speed > 80:
        return 'Big Ticket'
    elif speed > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

#QUESTION 11
#I did not see this question earlier
print("11. Given this nested dictionary grab the word hello Be prepared, this will be annoying/tricky")

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]



