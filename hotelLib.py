# Jessica Soriano

class book:
    def __init__(self, season, budget):
        self.season = season
        self.budget = budget

    def recommend(self, season, budget):
        if season == 'spring':
            if budget == 'low':
                print("Recommended time to visit: March\n"
                      "Recommended countries to visit: Mexico, Vietnam, Argentina, Ukraine")
            if budget == 'medium':
                print("Recommended time to visit: April\n"
                      "Recommended countries to visit: UK, USA, Italy, Australia")
            if budget == 'high':
                print("Recommended time to visit: May\n"
                      "Recommended countries to visit: Switzerland, Norway, Iceland, Denmark")
        if season == 'summer':
            if budget == 'low':
                print("Recommended time to visit: June\n"
                      "Recommended countries to visit: Mexico, Vietnam, Argentina, Ukraine")
            if budget == 'medium':
                print("Recommended time to visit: July\n"
                      "Recommended countries to visit: UK, USA, Italy, Australia")
            if budget == 'high':
                print("Recommended time to visit: August\n"
                      "Recommended countries to visit: Switzerland, Norway, Iceland, Denmark")
        if season == 'fall':
            if budget == 'low':
                print("Recommended time to visit: November\n"
                      "Recommended countries to visit: Mexico, Vietnam, Argentina, Ukraine")
            if budget == 'medium':
                print("Recommended time to visit: October\n"
                      "Recommended countries to visit: UK, USA, Italy, Australia")
            if budget == 'high':
                print("Recommended time to visit: September\n"
                      "Recommended countries to visit: Switzerland, Norway, Iceland, Denmark")
        if season == 'winter':
            if budget == 'low':
                print("Recommended time to visit: January\n"
                      "Recommended countries to visit: Mexico, Vietnam, Argentina, Ukraine")
            if budget == 'medium':
                print("Recommended time to visit: February\n"
                      "Recommended countries to visit: UK, USA, Italy, Australia")
            if budget == 'high':
                print("Recommended time to visit: December\n"
                      "Recommended countries to visit: Switzerland, Norway, Iceland, Denmark")

    def __str__(self):
        return f"Season: {self.season} \nBudget: {self.budget}"

class bookingext(book):
    def __init__(self, season, budget, country):
        book.__init__(self, season, budget)
        self.country = country
    def __str__(self):
        return f"Season: {self.season} \nBudget: {self.budget} \nCountry: {self.country}"
