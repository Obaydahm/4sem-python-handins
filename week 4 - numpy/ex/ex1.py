import matplotlib.pyplot as plt
import numpy as np
import csv

# Week 4 Exercise with Numpy
# Exercise 1
# 1. Open the file './befkbhalderstatkode.csv'
filename = "../../befkbhalderstatkode.csv"

# 2. Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
data = np.genfromtxt(filename, delimiter=",", dtype=np.uint, skip_header=1)

# 3. Using this data:
neighb = {
    1: "Indre By",
    2: "Østerbro",
    3: "Nørrebro",
    4: "Vesterbro/Kgs. Enghave",
    5: "Valby",
    6: "Vanløse",
    7: "Brønshøj-Husum",
    8: "Bispebjerg",
    9: "Amager øst",
    10: "Amager Vest",
    99: "Udenfor",
}
## Find out how many people lived in each of the 11 areas in 2015
def number_of_people_per_neighbourhood(n, mask):
    all_people_in_given_n = data[mask & (data[:, 1] == n)]
    sum_of_people = all_people_in_given_n[:, 4].sum()  # index 4 is no of 'PERSONER'
    return sum_of_people


mask = data[:, 0] == 2015
neighborhoods_population_in_2015 = {
    v: number_of_people_per_neighbourhood(k, mask) for k, v in neighb.items()
}
# print(neighborhoods_population_in_2015)

# 4. Make a bar plot to show the size of each city area from the smallest to the largest
def draw_barplot(areas):
    areas = {k: v for k, v in sorted(areas.items(), key=lambda x: x[1])}
    x_neighb_names = areas.keys()
    y_neighb_population = areas.values()

    plt.bar(x_neighb_names, y_neighb_population)

    plt.title("Population of 11 areas in 2015")
    plt.xlabel("Areas")
    plt.ylabel("Population")

    plt.tight_layout()
    plt.show()


# draw_barplot(neighborhoods_population_in_2015)

# 5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
# 6. How many of those were from the other nordic countries (not dk)
def people_above_65():
    statcodes_nordic = [5110, 5120, 5104, 5105, 5106, 5101, 5901, 5902]
    filtered_data = data[
        (data[:, 0] == 2015)
        & (data[:, 2] > 65)
        & (np.in1d(data[:, 3], statcodes_nordic))
    ]
    return filtered_data[:, 4].sum()


# print(people_above_65())

# 7. Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015
def changes_of_people():
    years = [y for y in range(1992, 2016)]

    x_indexes = np.arange(len(years))

    vesterbro = {
        k: number_of_people_per_neighbourhood(4, data[:, 0] == k) for k in years
    }
    østerbro = {
        k: number_of_people_per_neighbourhood(2, data[:, 0] == k) for k in years
    }

    width = 0.35

    plt.bar(x_indexes, list(vesterbro.values()), width=width, label="Vesterbro")
    plt.bar(x_indexes + width, list(østerbro.values()), width=width, label="Østerbro")

    plt.legend()

    plt.xticks(ticks=x_indexes, labels=years)

    plt.title("Changes of people in Vesterbro and Østerbro from 1992 to 2015")
    plt.xlabel("Areas")
    plt.ylabel("Population")

    plt.tight_layout()
    plt.show()


changes_of_people()
