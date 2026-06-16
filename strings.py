a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


print("Hello")
print('Hello')


b = "Hello, World!"
print(b[1:8])


b = "Hello, World!"
print(b[:3])


b = "Hello, World!"
print(b[4:])


b = "Hello, World!"
print(b[-4:-3])


a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


a = "Hello, World!"
print(a.replace("l", "J"))


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "om"
b = "brahmbhatt"
c = a + b
print(c)


a = "om"
b = "brahmbhatt"
c = a + " " + b
print(c)


age = 50
txt = f"My name is John, I am {age}"
print(txt)


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


txt = f"The price is {25 * 52} dollars"
print(txt)


txt = "We are the so-called \"Vikings\" from the north."
print(txt)


txt = "We are the so-called \\Vikings\\ from the north."
print(txt)


txt = "We are the so-called \nVikings\n from the north."
print(txt)


txt = "We are the so-called \rVikings\r from the north."
print(txt)


txt = "We are the so-called \tVikings\t from the north."
print(txt)


txt = "We are the so-called \bVikings\b from the north."
print(txt)


txt = "We are the so-called \fVikings\f from the north."
print(txt)


txt = "We are the so-called \oooVikings\ooo from the north."
print(txt)


txt = "We are the so-called \xhhVikings\xhh from the north."
print(txt)