#All the data is located in here.
A_market_prices = { 'GreenGroce': 5, 'Bakery': 1, 'Drinks': 3, 'Spices Kinds': 2, 'legume family' : 5 }
B_market_prices = { 'GreenGroce': 7, 'Bakery': 2, 'Drinks': 4, 'Spices Kinds': 1, 'legume family' : 5 }
C_market_prices = { 'GreenGroce': 10, 'Bakery': 2, 'Drinks': 5, 'Spices Kinds': 0.5, 'legume family' : 3}
D_market_prices = { 'GreenGroce': 3, 'Bakery': 1.5, 'Drinks': 2.5, 'Spices Kinds': 1, 'legume family' : 1}
E_market_prices = { 'GreenGroce': 4, 'Bakery': 3, 'Drinks': 3, 'Spices Kinds': 3, 'legume family' : 2}
GreenGroce = [A_market_prices['GreenGroce'], B_market_prices['GreenGroce'], C_market_prices['GreenGroce'], D_market_prices['GreenGroce'],
              E_market_prices['GreenGroce']]
Bakeries = [A_market_prices["Bakery"],B_market_prices["Bakery"],C_market_prices["Bakery"],D_market_prices["Bakery"],E_market_prices["Bakery"]]
Drinks = [A_market_prices["Drinks"],B_market_prices["Drinks"],C_market_prices["Drinks"],D_market_prices["Drinks"],E_market_prices["Drinks"]]
Spices = [A_market_prices["Spices Kinds"],B_market_prices["Spices Kinds"],C_market_prices["Spices Kinds"],D_market_prices["Spices Kinds"],E_market_prices["Spices Kinds"]]
legumes = [A_market_prices["legume family"],B_market_prices["legume family"],C_market_prices["legume family"],D_market_prices["legume family"],E_market_prices["legume family"]]
qualities = [5,6,3,4,7]
markets = ["A marketi", "B marketi", "C marketi", "D marketi", "E marketi"]
#Data's location is finishing in here.

def comparing(qualities, aisle):
  empty_list =  {}
  for i in range(0, len(qualities), 1):
    for x in markets:
      comparing_score = aisle[i] / qualities[i]
      empty_list.update({x : comparing_score})
    if i == 4:
       print(empty_list)
#There is a function which compares the input arguments.

def shopping():
    compare_selection = int(input('Lütfen hangi ürünü kıyaslamak istediğinizi giriniz: '
                                  '\nManav Reyonu(1), Unlu Mamüller(2), Meşrubatlar(3), Baharat Çeşitleri(4), Baklagiller(5) '))
    if compare_selection == 1:
        comparing(qualities, GreenGroce)
    if compare_selection == 2:
        comparing(qualities, Bakeries)
    if compare_selection == 3:
        comparing(qualities, Drinks)
    if compare_selection == 4:
        comparing(qualities, Spices)
    if compare_selection == 5:
        comparing(qualities, legumes)

print("Cimri Ticaret' e hoş geldiniz. Burada, lokasyonunuza en yakın 5 markete göre fiyat/performans kıyaslaması yapabileceğiniz bir hizmet sunmaktayız.\n ")
city = input('Devam etmek için lütfen şehrinizi giriniz :')
district = input('Lütfen semtinizi giriniz: ')
neighborhood = input('Lütfen mahallenizin/sitenizin ismini giriniz: ')

while(1):
  print(f"{city}/{district}/{neighborhood} adresine en yakın beş market şunlar: A marketi, B marketi, C marketi, D marketi, E marketi ")
  market_continue_check = str(input('Fiyat/Kalite kıyaslaması yapmak ister misiniz ? Evet(E), Hayır(H)'))
  if market_continue_check == "E" or market_continue_check == "e":
      shopping()
      break
  elif market_continue_check == "H" or market_continue_check == "h":
    print('İşlem son buldu.')
    break














