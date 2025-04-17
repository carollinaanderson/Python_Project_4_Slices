# Your code below:

#1 

toppings = [ "pepperoni","pineapple","cheese","sausage",
"olives","anchovies","mushrooms"]

#2

prices = [2, 6, 1, 3, 2, 7, 2]

#3

num_two_dollar_slices = prices.count(2)

#4

num_pizzas = len(toppings)

#5 
print("We sell [num_two_dollar_slices] different kinds of pizza!")

#6 
pizza_and_prices = [

[2, "pepperoni"],
[6, "pineapple"],
[1, "cheese"],
[3, "sausage"],
[2, "olives"],
[7, "anchovies"],
[2, "mushrooms"]

]

#7
print(pizza_and_prices)

#8
pizza_and_prices.sort()

#9 
cheapest_pizza = pizza_and_prices[0]

#10 

priciest_pizza = pizza_and_prices[-1:]

#11 

pizza_and_prices.pop()

#12 

toppings.insert("anchovies","peppers")

#13 

three_cheapest = pizza_and_prices[-3:]

#14 

print(three_cheapest)



