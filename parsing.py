
import requests
from bs4 import BeautifulSoup

def get_profile_data(username):
    # Make a request to the social network's website to get the user's profile page
    response = requests.get(f"https://twitter.com/{username}")
    html = response.text
    
    # Use BeautifulSoup to parse the HTML of the profile page
    soup = BeautifulSoup(html, "html.parser")
    
    # Extract the profile data from the page
    full_name = soup.find("h1", class_="full-name")
    city = soup.find("span", class_="city")
    dob = soup.find("span", class_="dob")
    
    # Extract the groups and friends from the page
    groups = []
    friends = []
    for div in soup.find_all("div", class_="group"):
        groups.append(div.text)
    for div in soup.find_all("div", class_="friend"):
        friends.append(div.text)
    
    # Return the extracted profile data as a dictionary
    return {
        "full_name": full_name,
        "city": city,
        "dob": dob,
        "groups": groups,
        "friends": friends
    }

# Example usage
profile_data = get_profile_data("P_Obuya")
print(profile_data)
