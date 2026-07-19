for i in range(nr_letters):
     for j in range(nr_symbols):
         for f in range(nr_numbers):
             random_letter=random.choice(letters)
             random_symbol=random.choice(symbols)
             random_number=random.choice(numbers)
             collection=[random_letter,random_symbol,random_number]
             end=random.choice(collection)
             print(end,end="")
