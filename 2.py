# a = int(input('inter a no., '))
# # b = int(input('inter a no., '))
# b = []
# i=1
# while i<=a:
#     if a%i==0:
#         b.append(i)
#         i+=1
# print(b)

a = int(input('Enter a number: '))

# Khaali list banate hain jisme divisors store karenge
b = []

i = 1
while i <= a:
    if a % i == 0:
        b.append(i)
    i += 1  # yeh line loop ke end mein aani chahiye

# List of divisors ko print karna
print(b)

