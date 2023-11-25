## import libraries
import time
import pandas as pd
import numpy as np

## csv files
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_valid_input(prompt, valid_options):
    """
    Handles user input by making it case insensitive and ensuring it matches valid options.

    Args:
        prompt (str): The prompt to display to the user.
        valid_options (list): List of valid options to match the user input.

    Returns:
        input_value (str): Valid input value from the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print('Invalid input. Please enter a valid option.')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get valid city input
    city = get_valid_input('Enter city name (chicago, new york city, washington): ', CITY_DATA)

    # Define valid months and days
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # Get valid month input
    month = get_valid_input('Enter month name (all, january, february, ..., june): ', months)

    # Get valid day input
    day = get_valid_input('Enter day of week (all, monday, tuesday, ..., sunday): ', days)

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

    df = pd.read_csv(CITY_DATA[city.lower()])  # Load data for the specified city
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter data based on month and day if applicable
    if month != 'all':
        month_num = months.index(month) + 1
        df = df[df['Start Time'].dt.month == month_num]

    if day != 'all':
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    return df

def display_data(df):
    """
    Displays raw data upon request by the user.
    """

    start_loc = 0
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?: ").lower()
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])  # Convert 'Start Time' to datetime
    df['Month'] = df['Start Time'].dt.month  # Extract month
    common_month = df['Month'].mode()[0]  # Find the mode (most common)
    print(f"The most common month is: {common_month}")

    # TO DO: display the most common day of week
    df['Day_of_Week'] = df['Start Time'].dt.day_name()  # Extract day of the week
    common_day = df['Day_of_Week'].mode()[0]  # Find the mode (most common)
    print(f"The most common day of the week is: {common_day}")

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour  # Extract hour
    common_hour = df['Hour'].mode()[0]  # Find the mode (most common)
    print(f"The most common start hour is: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {common_start_station}")

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']  # Combine start and end stations
    common_trip = df['Trip'].mode()[0]
    print(f"The most frequent combination of start and end station trip is: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time is: {total_travel_time} seconds")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types_count)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("\nCounts of gender:")
        print(gender_count)
    else:
        print("\nGender information not available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print(f"\nEarliest year of birth: {earliest_birth_year}")
        print(f"Most recent year of birth: {most_recent_birth_year}")
        print(f"Most common year of birth: {common_birth_year}")
    else:
        print("\nBirth year information not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Verify filtered and unfiltered data sizes
        filtered_df = load_data(city, month, day)
        unfiltered_df = pd.read_csv(CITY_DATA[city.lower()])
        print(f"Filtered Data Size: {filtered_df.shape[0]}")
        print(f"Unfiltered Data Size: {unfiltered_df.shape[0]}")

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no: ').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
