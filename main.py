import sqlite3
connect = sqlite3.connect('compare_application.db')
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS CompareApp (marketName TEXT, marketQuality INT, legumePrice INT, bakeryPrice INT, greenGroce INT)")
#Database has been created

class Market:
    def __init__(self, quality, marketName, legumePrice, bakeryPrice, greenGroce ):
        self.quality = quality
        self.marketName = marketName
        self.legumePrice = legumePrice
        self.bakeryPrice = bakeryPrice
        self.greenGroce = greenGroce
#Market class is defining


def get_key(val, dict):
    for key, value in dict.items():
         if val == value:
             return key


def comparing(product):
    scores_with_names = {}
    scores_with_names.update({'A marketi': market_attributes_on_list['market_A'][product] / market_A.quality})
    scores_with_names.update({'B marketi': market_attributes_on_list['market_B'][product] / market_B.quality})
    scores_with_names.update({'C marketi': market_attributes_on_list['market_C'][product] / market_C.quality})
    scores_with_names.update({'D marketi': market_attributes_on_list['market_D'][product] / market_D.quality})
    scores_with_names.update({'E marketi': market_attributes_on_list['market_E'][product] / market_E.quality})
    print("\n", scores_with_names)
    print("The best score is: {} and it's score of the: {}".format(min(scores_with_names.values()), get_key(min(scores_with_names.values()), scores_with_names)))
    print("\nWarning! Smaller scores means better performance.")

def attribue_assigning():
    global market_A, market_B, market_C, market_D, market_E
    cursor.execute("SELECT * FROM CompareApp")
    data = cursor.fetchall()
    market_A = Market(marketName=data[0][0], quality=data[0][1], legumePrice=data[0][2],
                          bakeryPrice=data[0][3], greenGroce=data[0][4])
    market_B = Market(marketName=data[1][0], quality=data[1][1], legumePrice=data[1][2],
                          bakeryPrice=data[1][3], greenGroce=data[1][4])
    market_C = Market(marketName=data[2][0], quality=data[2][1], legumePrice=data[2][2],
                          bakeryPrice=data[2][3], greenGroce=data[2][4])
    market_D = Market(marketName=data[3][0], quality=data[3][1], legumePrice=data[3][2],
                          bakeryPrice=data[3][3], greenGroce=data[3][4])
    market_E = Market(marketName=data[4][0], quality=data[4][1], legumePrice=data[4][2],
                          bakeryPrice=data[4][3], greenGroce=data[4][4])

attribue_assigning()
#Creating all market objectss
def program():
    while True:
        product_selection = int(input("Welcome to the price / performance comparison application.\n"
                                  "Please select the product you want to compare price performance with.\n"
                                  "Legumes : 1, Bakeries : 2, Green Groces : 3 : "))
        if product_selection == 1:
            comparing(1)
        if product_selection == 2:
            comparing(2)
        if product_selection == 3:
            comparing(3)
        break

market_attributes_on_list = {'market_A' : [market_A.legumePrice, market_A.bakeryPrice, market_A.greenGroce],
                             'market_B' : [market_B.legumePrice, market_B.bakeryPrice, market_B.greenGroce],
                             'market_C' : [market_C.legumePrice, market_C.bakeryPrice, market_C.greenGroce],
                             'market_D' : [market_D.legumePrice, market_D.bakeryPrice, market_D.greenGroce],
                             'market_E' : [market_E.legumePrice, market_E.bakeryPrice, market_E.greenGroce]}

program()



