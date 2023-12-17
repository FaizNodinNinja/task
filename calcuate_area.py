# calculate the area of rectangle

length = input("enter the length ")
width = input("enter the width ")

area = (lenght * breath)

print(area)











def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))

        result = calculate_area(length, width)

        if isinstance(result, str):
            print(result)
        else:
            print("The area of the rectangle is:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values for length and width.")

if __name__ == "__main__":
    main()
