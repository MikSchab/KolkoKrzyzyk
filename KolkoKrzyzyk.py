# Mikołaj Schab  Paweł Przybylski projekt python Kołko krzyzyk
import os
import time
from colorama import Fore, Back

def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

def screenXO(screen):
    os.system('cls')

    
    corners = {
               "upperLeft":     "┌",  
               "upperRight":    "┐",  
               "mediumLeft":    "├",  
               "mediumRight":   "┤",  
               "bottomLeft":    "└",  
               "bottomRight":   "┘",  
               "upperMid":      "┬",  
               "midiumMid":     "┼",  
               "bottomMid":     "┴"   
              }
    lines =   {
               "vertical": "│",       
               "horizontal": "─"      
              }
    
    size = len(screen)               

    verticalLine = [lines["horizontal"]*3]*size        

    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
   

    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if(j>0): printGreen(" X ")
            elif j<0: printRed(" O ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")


if __name__ == "__main__":

    rozmiar = 3
    dane = []
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        dane.append(kolumna)
   

    gracz = 1
    while True:
        screenXO(dane)
        if gracz == 1: printGreen("Gracz 1\n")
        else: printRed("Gracz 2\n")
        x = int(input("Podaj wsp x: "))
        y = int(input("Podaj wsp y: "))
        if x>2 or x<0 or y>2 or y<0:
            screenXO(dane)
            printRed("Podaj poprawne współrzędne")
            time.sleep(5)
        else:
            if dane[y][x] == -1 or dane[y][x] == 1:
                screenXO(dane)
                printRed("To miejsce jest zajete")
                time.sleep(5)
            else:
                dane[y][x] = gracz
                gracz *= -1
                if dane[0][0] == dane[0][1] == dane[0][2] == 1 or dane[1][0] == dane[1][1] == dane[1][2] == 1 or dane[2][0] == dane[2][1] == dane[2][2] == 1 or dane[0][0] == dane[1][0] == dane[2][0] == 1 or dane[0][1] == dane[1][1] == dane[2][1] == 1 or dane[0][2] == dane[1][2] == dane[2][2] == 1 or dane[0][0] == dane[1][1] == dane[2][2] == 1 or dane[0][2] == dane[1][1] == dane[2][0] == 1: 
                    screenXO(dane)
                    printGreen("Gracz X wygrał")
                    break
                elif dane[0][0] == dane[0][1] == dane[0][2] == -1 or dane[1][0] == dane[1][1] == dane[1][2] == -1 or dane[2][0] == dane[2][1] == dane[2][2] == -1 or dane[0][0] == dane[1][0] == dane[2][0] == -1 or dane[0][1] == dane[1][1] == dane[2][1] == -1 or dane[0][2] == dane[1][2] == dane[2][2] == -1 or dane[0][0] == dane[1][1] == dane[2][2] == -1 or dane[0][2] == dane[1][1] == dane[2][0] == -1:
                    screenXO(dane)
                    printRed("Gracz O wygrał")
                    break
                else: 
                    pass
