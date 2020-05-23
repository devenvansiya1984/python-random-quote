def mainT():
    print("Responsive is better than fast")
    print("Hi Deven")
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    
    print(quotes[12])

if __name__== "__main__":
  mainT()
