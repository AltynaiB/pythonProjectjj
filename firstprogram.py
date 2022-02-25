#Eta programma opisyvet kak
#rabotaut peremennye strokovogo
#chislovogo i drobnogo znacheniya

#Otobrajenie na ekran Hello World!
print('Hello world!')
print('hello world!')

x = 5
y = 10

#Opedelili chislovye znacheniya
number1 = 10
number2 = 20
number3 = 2.56
number4 = 2.37
number5 = 54

checkResult = True
#Zadali strokovye znacheniya
name = 'Askar'
myAddress = 'Bishkek city in Lev Tolstoy 123 Street'
#Poluchaem rezultat
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)


print('number1 type: ', type(number1))
print('number2 type: ', type(number2))
print('number3 type: ', type(number3))
print('number4 type: ', type(number4))
print('Name type:', type(name))
print('Address type:',type(myAddress))
print('Text type:', type(name))
result = x**2 + y 
mathresult1 = number1 + number2 / number3 + number5 + 12 * number4
mathresult2 = mathresult1 + number1 #Matematicheskii rezultat
mathresult4 = number1 + number2

print(result)
print(mathresult1)
print(mathresult2) 

print(checkResult)
print(name)
print(myAddress)
#Otobrajaem rezultat
text = 'My name is ' + name + 'I am' + str(number2) + 'years old and my address is '+ myAddress
print(text)
print(type(text))

print('My name is ', name, 'I am', number2, 'years old and my address is ', myAddress)


number1 = 50
number2 = 30
mathresult3 = number1 + number2
print(mathresult3)
print(mathresult4)

#Primem dannye ot polzovatelya
userName = input('Napishite svoe imya')
userAge = int(input('Napishite svoi vozrast'))
wifeAge = (input('Napishite vozrast suprogi:'))
userAddress = input('Napishite svoi address')

resultTwoAges = userAge + wifeAge
print('Name:', userName, 'Age:', userAge, 'Address:', userAddress)
print(resultTwoAges)