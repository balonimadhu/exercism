def classify(number):
   if number <= 0:
       raise ValueError("Classification is only possible for positive integers.")
   alliquot_numbers = []
   for i in range(1, number):
       if number % i == 0:
           alliquot_numbers.append(i)
   result = sum(alliquot_numbers)
   if result < number:
       return "deficient"
   if result > number:
       return "abundant"
   else:
       return "perfect"