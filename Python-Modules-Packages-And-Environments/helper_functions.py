import pandas as pd
import numpy as np
import random

df = pd.DataFrame({'a':[1,2,np.nan,8,np.nan,5],'b':[4,np.nan,6,np.nan,6,5]})

adjectives = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

addy_series = pd.Series([
    '890 Jennifer Brooks\nNorth Janet, WY 24785',
    '8394 Kim Meadow\nDarrenville, AK 27389',
    '379 Cain Plaza\nJosephburgh, WY 06332',
    '5303 Tina Hill\nAudreychester, VA 97036'
])

def random_phrase(list1, list2):
    '''random combination of adjectives and nouns'''
    item1 = random.choice(list1)
    item2 = random.choice(list2)
    return str(item1) + ' ' + str(item2)

def random_float(min_val, max_val):
    ''' returns a random float sampled from a uniform distribution 
    with a minimum value of min_val and a maximum value of max_val.'''
    return round(random.uniform(min_val, max_val), 1)

def random_bowling_score():
    'returns a random integer between 0 and 300.'
    return random.randint(0, 300)

def silly_tuple():
    adjective_noun = random_phrase(adjectives, nouns)
    star_rating = random_float(1, 5)
    bowling_score = random_bowling_score()
    return (adjective_noun, star_rating, bowling_score)


def count_nulls(df):
    'return total count of null values in a data frame'
    total = df.isnull().sum().sum()
    return total

def tt_split(df,frac):
    '''split data into train and test
       it takes a df and the test set size'''
    if type(df) == pd.core.frame.DataFrame: 
      if (frac < 1) & (frac != 0):
        test = df[:(round(len(df)*frac))]
        train = df[(round(len(df)*frac)):]
        return (pd.DataFrame(train), pd.DataFrame(test))
      else:
        raise NameError('Second Argument needs a value > 0 and < 1')
    else:
      raise NameError('First Argument is not a DataFrame Type')
    


def randomize(df, seed):
    '''randomizes all of a dataframes cells 
      then returns that randomized dataframe'''
    np_array = df.values
    np.random.seed(seed)
    np.random.shuffle(np_array)
    randomized_df = pd.DataFrame(np_array, columns=df.columns)
    return randomized_df


def addy_split(addy_series):
    #Split addresses into three columns (df['city'], df['state'], and df['zip'])
    result_df = addy_series.str.split('\n|,\s*', expand=True)
    result_df.columns = ['city', 'state', 'zip']   
    return result_df


def abbr_2_st(state_series, abbr_2_st=True):
    # converts abbr of the state to full name str
    state_dict = {
        'AL': 'Alabama',
        'AZ': 'Arizona',
        'CA': 'California',
        'DE': 'Delaware',
        'OH': 'Ohio',
        # Add more states as needed
    }
    result_series = state_series.map(state_dict) if abbr_2_st else state_series.map({v: k for k, v in state_dict.items()})
    return result_series


# input_list = [0, 1, 2]
# input_dataframe = pd.DataFrame()
def list_2_series(input_list, df):
    #conv list to series
    new_series = pd.Series(input_list, name='list')
    df = pd.concat([df, new_series], axis=1)
    return df



def rm_outlier(df):
    # Calculate the first and third quartiles
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    
    # Calculate the interquartile range (IQR)
    iqr = q3 - q1
    
    # Define the lower and upper bounds for outliers
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    # Identify and remove outliers
    df_cleaned = df[((df >= lower_bound) & (df <= upper_bound)).all(axis=1)]
    
    return df_cleaned

# Example Input
df = pd.DataFrame({
    'column 0': [1, 850, 7],
    'column 1': [2, 5, 8],
    'column 2': [3, 6, 9]
})



def split_dates(date_series): 
    date_df = date_series.str.split('/', expand=True) 
    date_df.columns = ['month', 'day', 'year']
    date_df = date_df.apply(pd.to_numeric, errors='coerce')
    
    return date_df

# Example Input
date_series = pd.Series(['02/28/2006', '03/09/2010', '06/12/1850'])
