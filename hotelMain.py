# Jessica Soriano
# create lists of relevant attributes in hotel bookings txt file
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
import seaborn as sns
import hotelLib as htl

if __name__ == '__main__':
    print("Welcome to the Hotel Optimizer")
    print("1 - Statistics Report")
    print("2 - Booking Frequency by Month")
    print("3 - ADRs by Country")
    print("4 - ADRs by Month")
    print("5 - Sample Recommendations")
    answer = input("What tool would you like to use?")
    if answer == '1':
        file = open('hotel_bookings.txt', 'r')
        all = []
        for line in file:
            line = line.split()
            for num in line:
                all.append(num)

        file.close()

        # organize data by column
        hotel = [all[index]for index in range(19, len(all), 18)]
        arrivalDateYear = [all[index]for index in range(20, len(all), 18)]
        arrivalDateMonth = [all[index]for index in range(21, len(all), 18)]
        arrivalDateWeek = [all[index]for index in range(22, len(all), 18)]
        arrivalDateDayNum = [all[index]for index in range(23, len(all), 18)]
        NumWeekendStays = [all[index]for index in range(24, len(all), 18)]
        NumWeeknightStays = [all[index]for index in range(25, len(all), 18)]
        adults = [all[index]for index in range(26, len(all), 18)]
        children = [all[index]for index in range(27, len(all), 18)]
        babies = [all[index]for index in range(28, len(all), 18)]
        country = [all[index]for index in range(29, len(all), 18)]
        isRepeatedGuest = [all[index]for index in range(30, len(all), 18)]
        previousCancellations = [all[index]for index in range(31, len(all), 18)]
        previousBookingsNotCancelled = [all[index]for index in range(32, len(all), 18)]
        requiredCarSpaces = [all[index]for index in range(33, len(all), 18)]
        NumSpecialRequests = [all[index]for index in range(34, len(all), 18)]
        adr = [all[index]for index in range(35, 1000, 18)]

        write = open('StatisticsReport.txt', 'w')
        # find percentage of types of hotels booked
        resort = 0
        city = 0
        counter = 0
        for i in hotel:
            if i == 'Resort':
                resort += 1
            else:
                city += 1
            counter += 1
        write.write("% of Bookings for Resort Hotels :" + " {:.2%}".format(resort/counter) + "\n")
        write.write("% of Bookings for City Hotels :" + " {:.2%}".format(city/counter) + "\n")

        # find frequency of hotel bookings in each month - rank busiest months
        jan = 0
        feb = 0
        mar = 0
        apr = 0
        may = 0
        jun = 0
        jul = 0
        aug = 0
        sep = 0
        oct = 0
        nov = 0
        dec = 0
        counter = 0
        for j in arrivalDateMonth:
            if j == '1':
                jan += 1
            if j == '2':
                feb += 1
            if j == '3':
                mar += 1
            if j == '4':
                apr += 1
            if j == '5':
                may += 1
            if j == '6':
                jun += 1
            if j == '7':
                jul += 1
            if j == '8':
                aug += 1
            if j == '9':
                sep += 1
            if j == '10':
                oct += 1
            if j == '11':
                nov += 1
            if j == '12':
                dec += 1
            counter += 1
        write.write("% Bookings made in January:" + " {:.2%}".format(jan / counter) + "\n")
        write.write("% Bookings made in February:" + " {:.2%}".format(feb / counter) + "\n")
        write.write("% Bookings made in March:" + " {:.2%}".format(mar / counter) + "\n")
        write.write("% Bookings made in April:" + " {:.2%}".format(apr / counter) + "\n")
        write.write("% Bookings made in May:" + " {:.2%}".format(may / counter) + "\n")
        write.write("% Bookings made in June:" + " {:.2%}".format(jun / counter) + "\n")
        write.write("% Bookings made in July:" + " {:.2%}".format(jul / counter) + "\n")
        write.write("% Bookings made in August:" + " {:.2%}".format(aug / counter) + "\n")
        write.write("% Bookings made in September:" + " {:.2%}".format(sep / counter) + "\n")
        write.write("% Bookings made in October:" + " {:.2%}".format(oct / counter) + "\n")
        write.write("% Bookings made in November:" + " {:.2%}".format(nov / counter) + "\n")
        write.write("% Bookings made in December:" + " {:.2%}".format(dec / counter) + "\n")

        # find average number of weekend stays
        avgWeekend = round(stat.mean([int(i) for i in NumWeekendStays]),2)
        write.write("Average Number of Weekend Stays per Booking: " + str(avgWeekend) + "\n")

        # find average number of weekday stays
        avgWeeknight = round(stat.mean([int(i) for i in NumWeeknightStays]), 2)
        write.write("Average Number of Weeknight Stays per Booking: " + str(avgWeeknight) + "\n")

        # average number of adults in bookings
        avgAdults = round(stat.mean([int(i) for i in adults]), 2)
        write.write("Average Number of Adults per Booking: " + str(avgAdults) + "\n")

        # percentage of time children visit
        child = 0
        counter = 0
        for k in children:
            if k >= '1':
                child += 1
            counter += 1
        write.write("% Bookings with Children:" + " {:.2%}".format(child / counter) + "\n")

        # percentage of times babies visit
        baby = 0
        counter = 0
        for i in babies:
            if i >= '1':
                baby += 1
            counter += 1
        write.write("% Bookings with Babies:" + " {:.2%}".format(baby / counter) + "\n")

        # number of bookings per country for 20 'most visited countries' - rank most popular country,
        # 195 countries in world, 178 counties in dataset == no time
        PRT = 0
        FRA = 0
        USA = 0
        ESP = 0
        CHN = 0
        ITA = 0
        GBR = 0
        DEU = 0
        THA = 0
        AUS = 0
        GRC = 0
        RUS = 0
        JPN = 0
        for i in all:
            if i == 'PRT':
                PRT += 1
            if i == 'FRA':
                FRA += 1
            if i == 'USA':
                USA += 1
            if i == 'ESP':
                ESP += 1
            if i == 'CHN':
                CHN += 1
            if i == 'ITA':
                ITA += 1
            if i == 'GBR':
                GBR += 1
            if i == 'DEU':
                DEU += 1
            if i == 'THA':
                THA += 1
            if i == 'AUS':
                AUS += 1
            if i == 'GRC':
                GRC += 1
            if i == 'JPN':
                JPN += 1
        write.write("Bookings for Hotels in Portugal: " + str(PRT) + "\n")
        write.write("Bookings for Hotels in France: " + str(FRA) + "\n")
        write.write("Bookings for Hotels in USA: " + str(USA) + "\n")
        write.write("Bookings for Hotels in Spain: " + str(ESP) + "\n")
        write.write("Bookings for Hotels in China: " + str(CHN) + "\n")
        write.write("Bookings for Hotels in Italy: " + str(ITA) + "\n")
        write.write("Bookings for Hotels in UK: " + str(GBR) + "\n")
        write.write("Bookings for Hotels in Germany: " + str(DEU) + "\n")
        write.write("Bookings for Hotels in Thailand: " + str(THA) + "\n")
        write.write("Bookings for Hotels in Australia: " + str(AUS) + "\n")
        write.write("Bookings for Hotels in Greece: " + str(GRC) + "\n")
        write.write("Bookings for Hotels in Japan: " + str(JPN) + "\n")

        # frequency car spaces needed
        avgCarSpaces = round(stat.mean([int(i) for i in requiredCarSpaces]), 2)
        write.write("Average Number of Car Spaces Requested per Booking: " + str(avgCarSpaces) + "\n")

        # average number of special requests
        avgSpecialReq = round(stat.mean([int(i) for i in NumSpecialRequests]), 2)
        write.write("Average Number of Special Requests Made per Booking: "+ str(avgSpecialReq) + "\n")
        write.close()
        print("Your report has been created!")

    if answer == '2':
        hotelBookings = pd.read_csv('hotel_bookings.csv')
        # booking frequency by month
        hotelBookings.hist('arrival_date_month')
        plt.title('Booking Frequency by Month')
        plt.xlabel('Month')
        plt.ylabel('Number of Bookings')

    if answer == '3':
        hotelBookings = pd.read_csv('hotel_bookings.csv')
        # plot ADRs by country
        plot2 = sns.barplot(x='country', y='adr', data=hotelBookings)
        plt.xticks(rotation=30)

    if answer == '4':
        hotelBookings = pd.read_csv('hotel_bookings.csv')
        # plot ADRs by month
        sns.barplot(x='arrival_date_month', y='adr', data=hotelBookings)
        plt.xticks(rotation=30)

    if answer == '5':
        booking1 = htl.book('spring', 'low')
        print(booking1)
        booking1.recommend('spring', 'low')
        booking2 = htl.book('winter', 'high')
        print(booking2)
        booking2.recommend('winter','high')
        booking3 = htl.bookingext('spring', 'low', 'Norway')
        print(booking3)

    # function to keep a stack of 3 countries user is interested in
    def stack():
        x = input("Enter country:")
        y = input("Enter country:")
        z = input("Enter country:")
        stack1 = list()
        stack1.append(x)
        stack1.append(y)
        stack1.append(z)
        print("Here's your list:")
        print(stack1.pop())
        print(stack1.pop())
        print(stack1.pop())
