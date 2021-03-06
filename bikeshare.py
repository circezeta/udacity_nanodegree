# this file has been created for UDACITY Nanodegree program.
import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february','march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = None
    while city is None:
        city_in = input('Enter City [chicago, new york city, washington] :')
        if city_in.lower() in CITY_DATA:
            city = city_in.lower()

    month = None
    while month is None:
        month_in = input('Enter Month [all, january, february, ... , june] :')
        if month_in.lower() in months:
            month = month_in.lower()    

    day = None
    while day is None:
        day_in = input('Enter Day [all, monday, tuesday, ... sunday] :')
        if day_in.lower() in days:
            day = day_in.lower()
        

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month:', calendar.month_name[popular_month])

    # TO DO: display the most common day of week
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    popular_dayofweek = df['dayofweek'].mode()[0]
    print('Most Frequent Start Day of Week:', calendar.day_name[popular_dayofweek])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most commonly used start station:', df['Start Station'].value_counts().index[0])

    print('Most commonly used end station:', df['End Station'].value_counts().index[0])


    print('Most frequent combination of start station and end station trip:')
    print(df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    
    print('Total travel time: ', df['Travel Time'].sum())
    
    print('Mean travel time: ', df['Travel Time'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('User Type Counts: ')
    print(df['User Type'].value_counts())

    print('Gender Counts: ')
    try:
        print(df['Gender'].value_counts())
    except:
        print('No gender information found within the selected data set')
    


    try:
        print('Earliest Year of Birth:', df['Birth Year'].min())
        print('Most Recent Year of Birth:', df['Birth Year'].max())
        print('Most Common Year of Birth:', df['Birth Year'].value_counts().index[0])
    except:
        print('No birth year found within the selected data set')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    print('Welcome to Udacity Nanodegree program bikeshare data analysis application!')
	main()
