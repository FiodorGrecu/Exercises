# Code your solution here
figure_list = {
                "3":"Triangle",
                "4":"Quadrilateral",
                "5":"Pentagon",
                "6":"Hexagon",
                "7":"Heptagon",
                "8":"Octagon", 
                "9":"Nonagon"
}
data = []
# figure = input("figure: ")
figure = "5"
if figure in figure_list:
    data.append(figure_list[figure])
    print (figure_list[figure])
    
else:        
    print(figure) 
