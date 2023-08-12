import csv

def get_min_price():
    while True:
        try:
            min_price = int(input("Enter your minimum price: $"))
            if min_price >= 0:
                return min_price
            else:
                print("You entered an invalid number")
        except ValueError:
            print("You didn't enter a whole number")

def get_max_price(min_price):
    while True:
        try:
            max_price = int(input("Enter your maximum price: $"))
            if max_price > min_price:
                return max_price
            else:
                print("Your maximum price cannot be equal to or lower than your minimum price")
        except ValueError:
            print("You didn't enter a whole number")

def get_bedrooms():
    while True:
        try:
            bedrooms = int(input("Enter the number of bedrooms desired: "))
            if bedrooms >= 1:
                return bedrooms
            else:
                print("You entered an invalid number")
        except ValueError:
            print("You didn't enter a whole number")

def get_bathrooms():
    while True:
        try:
            bathrooms = int(input("Enter the minimum number of bathrooms desired: "))
            if bathrooms >= 1:
                return bathrooms
            else:
                print("You entered an invalid number")
        except ValueError:
            print("You didn't enter a whole number")

def parse_listings(min_price, max_price, bedrooms, bathrooms):
    file = 'D:\Documents\IUPUI\Spring Semester 2023\CIT140ProgrammingConcepts\Module16\house_listing.csv'
    matching_listings = []
    
    with open(file) as csvfile:
        listings = csv.DictReader(csvfile, delimiter=",")
        for row in listings:
            price = int(row['price'])
            num_bedrooms = int(row['bedrooms'])
            num_bathrooms = int(row['bathrooms'])
            
            if min_price <= price <= max_price and num_bedrooms >= bedrooms and num_bathrooms >= bathrooms:
                matching_listings.append(row)

    return matching_listings

def main():
    print("Welcome to House Hunters Puerto Rico!")
    
    min_price = get_min_price()
    max_price = get_max_price(min_price)
    bedrooms = get_bedrooms()
    bathrooms = get_bathrooms()
    
    matching_listings = parse_listings(min_price, max_price, bedrooms, bathrooms)
    
    print(f"The number of listings that meet your criteria is {len(matching_listings)}.")
    print("The listings are:")
    
    for listing in matching_listings:
        print(f"{listing['address']} for ${listing['price']}")

if __name__ == "__main__":
    main()
