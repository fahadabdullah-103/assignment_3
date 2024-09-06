name = input("Enter your name: ")
numbers =(int(input("Enter 1st favorite number: ")),int(input("Enter 2nd favorite number: ")),int(input("Enter 3rd favorite number: ")))
print(f"\nHello, {name}! Let's explore your favorite numbers:")
for i in range (0,len(numbers)) :
    if numbers[i]%2==0 :
        print(f"The number {numbers[i]} is even.")
        
    else:
        print(f"The number {numbers[i]} is odd.") 
for i in range (0,len(numbers)) :   
    print(f"The number {numbers[i]} and its square: ({numbers[i]}, {numbers[i]**2})")
total_sum= sum(numbers)
print(f"Amazing! The sum of your favorite numbers is: {total_sum}")

if total_sum==0 or total_sum==1 :
    print("Oh! This not a prime number")
elif total_sum > 1:
    for i in range(2,total_sum):
        if (total_sum % i) == 0 :
            print("Oh! This not a prime number ")
            break
    else:
        print(f"Wow, {total_sum} is a prime number!")
    