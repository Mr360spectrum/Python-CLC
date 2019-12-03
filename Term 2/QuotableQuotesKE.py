# Karter Ence
# Quotable Quotes
# 11/25/2019
import random

def select_quote():
    quotes = ("My fake plants died because I did not pretend to water them - Mitch Hedberg", \
            "There cannot be a crisis next week.  My schedule is already full. - Henry Kissinger", \
            "Weather forecast for tonight: dark. - George Carlin", \
            "All generalizations are false, including this one. - Mark Twain", \
            "Why do they call it rush hour when nothing moves? - Robin Williams")
    numQuotes = len(quotes)
    index = random.randrange(0, numQuotes)
    print(quotes[index])
    return

select_quote()
select_quote()
