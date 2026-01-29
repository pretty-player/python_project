fruites=("red","green","yellow","orange")
print(fruites)

fruites.append("blue")  # This will raise an AttributeError since tuples are immutable

'''
    fruites.append("blue")  # This will raise an AttributeError since tuples are immutable
    ^^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'append'
'''