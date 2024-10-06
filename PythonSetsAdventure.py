#Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a 
# competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:
#1. Destinations that both airlines fly to.
#2. Destinations unique to your airline.
#3. Whether there are any destinations that neither airline shares.
#Example Code:
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)

unique_our_routes = our_routes.difference(competitor_routes)

unique_competitor_routes = competitor_routes.difference(our_routes)


all_destinations = our_routes.union(competitor_routes)
shared_destinations = common_destinations
neither_shared_destinations = all_destinations.difference(shared_destinations)


print("Common Destinations:", common_destinations)
print("Unique to Our Airline:", unique_our_routes)
print("Unique to Competitor:", unique_competitor_routes)
print("Destinations neither airline shares:", neither_shared_destinations)