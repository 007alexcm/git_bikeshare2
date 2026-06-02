import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Choose a city (chicago, new york city or washington)").lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print("Not valid city, try again")
        city = input("Choose a city (chicago, new york city or washington)").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Choose a month (all, january, february, ... , june)").lower()
    while month not in ('all', 'january', 'february', 'march', 'april', 'may' , 'june'):
        print("Not valid month, try again")
        month = input("Choose a month (all, january, february, ... , june)").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Choose a day of the week (all, monday, tuesday, ... sunday)").lower()
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print("Not valid day, try again")
        day = input("Choose a day of the week (all, monday, tuesday, ... sunday)").lower()
        
    print('-'*40)
    return city, month, day




def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])	
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['Month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print(f'The most common month of travel is {months[popular_month - 1]}')

    # TO DO: display the most common day of week
    popular_day = df['Day of Week'].mode()[0]
    print(f'The most common day of travel is on {popular_day}')
    
    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    popular_hour = df['Hour'].mode()[0]
    print(f'The most common hour of travel is {popular_hour}h')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_sstation = df['Start Station'].mode()[0]
    print(f'The most common start station of travel is {popular_sstation}')

    # TO DO: display most commonly used end station
    popular_estation = df['End Station'].mode()[0]
    print(f'The most common end station of travel is {popular_estation}')

    # TO DO: display most frequent combination of start station and end station trip
    popular_combstation = df.value_counts(['Start Station', 'End Station']).idxmax()
    #popular_combstation = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'The most common combination of start-end station is {popular_combstation}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"The total time travelling was: {round(df['Trip Duration'].sum() / 3600, 2)} h")

    # TO DO: display mean travel time
    print(f"The average travelling time was: {round(df['Trip Duration'].mean() / 60, 2)} min")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df.groupby(['User Type'])['User Type'].count())

    # TO DO: Display counts of gender
    try:
        print(df.groupby(['Gender'])['Gender'].count())
    except KeyError:
        print("Gender information cannot be displayed")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print(f"\nThe earliest year of birth is: {int(df['Birth Year'].min())}")
        print(f"The most recent year of birth is: {int(df['Birth Year'].max())}")
        print(f"The most common year of birth is: {int(df['Birth Year'].mode()[0])}")
    except KeyError:
        print("Birth Date information cannot be displayed.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def seedata(df):
    line = 0
    n = 5
    answer = input(f"Would you like to see {n} lines of your studied data? ('y' or 'n')").lower()
    while ((answer == 'y') or (answer == 'yes')) and (line < df.shape[0]):
        print(df.iloc[line:line + n])
        line += n
        answer = input("Would you like to see 5 more lines? ('y' or 'n')").lower()



def main():
    while True:
        city, month, day = get_filters()
        #city, month, day = ('washington', 'june', 'monday')
        df = load_data(city, month, day)
        print(df.columns)
        print(df.head(8))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        seedata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
