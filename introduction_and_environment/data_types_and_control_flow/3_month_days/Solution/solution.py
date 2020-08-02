# Code your solution here
<<<<<<< HEAD
month = (input("Enter a month and I'll tel you how many days it has: "))
=======
month = input("Enter a month and I'll tel you how many days it has: ")
>>>>>>> 3_month days doesn't pass

# month = {"January":"31"} 
month_dict = {"January":"31",
              "February":"28,29{#leap year}",
              "March":"31",
               "April":"30",
               "May":"31",
               "June":"30",
               "July":"31",
               "August":"31",
               "September":"30",
               "October":"31",
               "November":"30",
               "December":"31"

}
<<<<<<< HEAD

def data(month,month_dict):
    if month in month_dict.keys(): 
        return month_dict[month]
    else:
        return None
print(data(month,month_dict))
=======
def data(month):
    if month in month_dict.keys():
        return month_dict[month]
    else:
        return None
print(data(month))
>>>>>>> 3_month days doesn't pass
