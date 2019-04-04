# Function to calculate average price per category for a DataFrame

def avg_price_cat(city_pd):
    result_pd = city_pd.groupby('Category').filter(lambda x: x['Name'].count() >= 5)
    return result_pd.groupby('Category')['Price'].mean()


# Function to extract top 5 restaurants from a given DataFrame

def top_five(city_df):
    city_top_df = city_df[['Name', 'Rating', 'Review Count', 'Price']]
    city_top_df = city_top_df.drop_duplicates()
    city_top_df.sort_values(['Review Count', 'Rating'], ascending = [0, 0], inplace = True, )
    city_top_df = city_top_df.head()
    
    return city_top_df


# Function to generate formated restaurant info for info_box_content in gmaps

def info_box_text(city_top_df):
    
    mid_str = ''
    
    for index, row in city_top_df.iterrows():
        name = row['Name']
        rating = row['Rating']
        mid = f'{name} | {rating}&#9733;<br>'
        mid_str = mid_str + mid
    
    info_text = '\n<dl>\n<dt>Restaurants</dt><dd>' + mid_str + '</dd>\n</dl>'
    
    return [info_text]