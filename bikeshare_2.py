import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Checked
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!'
          '\n (note: there is some messing data for washington) ')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("\n Please enter the city name {washington, new york city, chicago}: ").lower()
    while city.lower() not in CITY_DATA:
       city= input("Please choose from the the list").lower()

    print("You have chosen{ ", city, " }")
    # get user input for month (all, january, february, ... , june)
    month_list=["all", "january", "february","march" ,"april","may", "june"]
    month=input("Please enter the specifc month from jan to jun OR all: ").lower()
    while month.lower() not in month_list:
      month= input("please choose a month from the given months: ").lower()
    print("You have chosen{ ", month, " }")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_list = ["all", "monday", "tuesday", "wednesday", "thursday", "friday","saturday", "sunday"]
    day = input("Please enter the specifc day OR all: ").lower()
    while day.lower() not in day_list:
       day= input("not valid please choose a month from the given days: ").lower()
    print("You have chosen{ ",day," }")

    print('-'*40)
    return city, month, day

#Checked
def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        df = df[df['month'] == month]

    # filter by day of week
    if day.lower() != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

#Checked1
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    y=input("Would you like to see the time data?  enter yes if you want to").lower()
    if y.lower() == 'yes':
        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # display the most common month
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        common_month = df['month'].mode()[0]
        print('Most common month: ', common_month)

        # display the most common day of week
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['day_of_week'] = df['Start Time'].dt.month
        common_day = df['day_of_week'].mode()[0]
        print('Most common day: ' , common_day)


        # display the most common start hour
        df['hour'] = df['Start Time'].dt.hour

        # find the most popular hour
        common_hour = df['hour'].mode()[0]

        print('Most Popular Start Hour:', common_hour)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)
    else:
        print("skip")

#test1

#Checked
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    x=input("do you want to display the stations Data? \nenter yes if you want to").lower()
    if x=="yes":
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # display most commonly used start station
        startstation=df['Start Station'].mode()[0]
        print("most commonly used start station: "+startstation)

        # display most commonly used end station
        endstaion = df['Start Station'].mode()[0]
        print("most commonly used end station: " + endstaion)

        # display most frequent combination of start station and end station trip
        df["frequent_comb"]= df['Start Station'] + df['End Station']
        combination = df['frequent_comb'].mode()[0]
        print("most frequent combination of start station and end station trip: " + combination)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("Skip")

#Checked
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    w=input("would you like to displays statistics on the total and average trip duration? \nenter yes if you want to")
    if w=="yes":
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # display total travel time
        print("total travel time: ",df["Trip Duration"].sum())

        # display mean travel time
        print("mean travel time: ",df["Trip Duration"].mean())


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("Skip")
#Checked
def user_stats(df):
    """Displays statistics on bikeshare users."""
    u = input("would you like to displays statistics on the total and average trip duration? \nenter yes if you want to")
    if u == "yes":

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print("ounts of user types: ",user_types)


        # Display counts of gender
        try:
            gender_counts = df['Gender'].value_counts()
            print(" counts of gender: ",gender_counts)
        except KeyError:
            print("We're sorry! There is no data of user birth years for washington")

        # Display earliest=MIN, most recent=MAX, and most common year of birth
        try:
            print('Earliest year of Birth:', df['Birth Year'].min())
            print('Most Recent year of Birth:', df['Birth Year'].max())
            print('Most Common year of Birth:', df['Birth Year'].mode()[0])
        except KeyError:
             print("We're sorry! There is no data of user birth years for washington" )

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    else:
        print("Skip")


def displaydata(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes if you want\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        displaydata(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if (restart.lower() != 'yes'):
            print("restarting")

        else:
             print("Thank you for using our service ")


if __name__ == "__main__":
    main()
