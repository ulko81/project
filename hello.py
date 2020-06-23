class First:

    @property
    def first_first(self):
        return 1


x = {'2': First().first_first}
z = First()
print(x['2'])

#y = z.x['2']
#print(y)
