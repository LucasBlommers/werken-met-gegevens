ticketPrijs=7.45
tickets = 3
vrPerMinuut = 0.37 / 5
vrMinuten = 45

totalPrice = (tickets*ticketPrijs) + (vrPerMinuut * vrMinuten)

print("Dit geweldige dagje-uit met " + str(tickets) + " mensen in de speelhal met " + str(vrMinuten) + " minuten vr kost je maar " + str(totalPrice) + " euro")