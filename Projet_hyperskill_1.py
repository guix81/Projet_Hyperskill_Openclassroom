
"""
print('''Prices: 
Bubblegum: $2
Toffee: $0.2
Ice cream: $5
Milk chocolate: $4
Doughnut: $2.5
Pancake: $3.2''')
"""

produits = ['Bubblegum', 'Toffee', 'Ice cream', 'Milk chocolate', 'Doughnut', 'Pancake']
list_produit = dict.fromkeys(produits, 0)
chaine = ''

list_produit['Bubblegum'] = 202
list_produit['Toffee'] = 118
list_produit['Ice cream'] = 2250
list_produit['Milk chocolate'] = 1680
list_produit['Doughnut'] = 1075
list_produit['Pancake'] = 80

income = sum(list_produit.values())

print('Earned amount:')

for key, val in list_produit.items():
    chaine = chaine + key + ': $' + str(val) + '\n'
chaine = chaine + '\nIncome: $' + str(income)

print(chaine)

staff_expenses = int(input('Staff expenses: '))
other_expenses = int(input('Other expenses: '))

expenses = staff_expenses + other_expenses
income_net = income - expenses

print('Net income: $' + str(income_net))