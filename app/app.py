from goog import goog

"""Function to obtain query
To be further improved with more google hacking techniques
and GUI form
"""
def obtain_query():
    try:
        name = input('Input your full name\n')
        country = input('\nInput your country\n')
        extra = input("\nInput other query params(put space in between)\n\n")
    except:
        print("Invalid input")
    return name.replace(' ', '+') + '+' + country.replace(' ', '+') + "+" + extra.replace(' ', '+')

def main():
    query = obtain_query()

    #scraped items
    goog_search = goog(query)
    scrap_items = [goog_search] #more to be added in the future
    
    for item in scrap_items:
        for i, result in enumerate(item.get_results()):
            print(i , result, '\n')

if __name__ == "__main__":
    main()