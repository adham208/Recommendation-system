import pandas as pd
flights_df = pd.read_csv('flights.csv')
hotels_df = pd.read_csv('hotels.csv')
def recommend_cities(budget, num_cities, flights_df, hotels_df, attractions_dict):
    Mat = [[0] * (budget + 1) for _ in range(num_cities + 1)]
    
    
    for city in range(1, num_cities + 1):
        city_name = flights_df.loc[city, 'to']
        city_price = flights_df.loc[city, 'price'] + hotels_df.loc[city,'price']
        for remaining_budget in range(1, budget + 1):
            if city_price <= remaining_budget:
                attractions_count = Mat[city - 1][remaining_budget - city_price] + len(attractions_dict[city_name])
                Mat[city][remaining_budget] = max(Mat[city - 1][remaining_budget], attractions_count)
            else:
                Mat[city][remaining_budget] = Mat[city - 1][remaining_budget]

    recommended_cities = []
    city = num_cities
    

    while city > 0 and remaining_budget > 0:
        if Mat[city][remaining_budget] != Mat[city - 1][remaining_budget]:
            city_name = flights_df.loc[city, 'to']
            hotel_name = hotels_df.loc[hotels_df['place'] == city_name, 'name'].values[0]
            airline = flights_df.loc[flights_df['to'] == city_name, 'agency'].values[0]
            city_price = flights_df.loc[city, 'price']
            hotel_price = hotels_df.loc[hotels_df['place'] == city_name, 'price'].values[0]
            recommended_cities.append((city_name, hotel_name, airline, city_price, hotel_price))
            remaining_budget -= city_price + hotel_price
            city -= 1 
    return recommended_cities



flights_df['price'] = flights_df['price'].astype(int)
hotels_df['price'] = hotels_df['price'].astype(int)

attractions_dict = {
    'Florianopolis (SC)': ['Attraction 1', 'Attraction 2', 'Attraction 3'],
    'Recife (PE)': ['Attraction 4', 'Attraction 5','Attraction test'],
    'Brasilia (DF)': ['Attraction 6', 'Attraction 7', 'Attraction 8'],
    'Salvador (BH)': ['Attraction 9', 'Attraction 10', 'Attraction 11'],
    'Aracaju (SE)': ['Attraction 12', 'Attraction 13'],
    'Campo Grande (MS)': ['Attraction 14', 'Attraction 15', 'Attraction 16'],
    'Sao Paulo (SP)': ['Attraction 17', 'Attraction 18'],
    'Rio de Janeiro (RJ)': ['Attraction 19','Attraction 20','Attraction 21'],
    'Natal (RN)': ['Attraction 22']
    
}

budget = 6000
num_cities = 3

recommended_cities = recommend_cities(budget, num_cities, flights_df, hotels_df, attractions_dict)

for city_name, hotel_name, airline, city_price, hotel_price in recommended_cities:
    print("City:", city_name)
    print("Airline:", airline)
    print("Price:", city_price)
    print("Hotel:", hotel_name)
    print("Price per night:", hotel_price)
    print()




