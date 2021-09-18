widthText, heightText = 56, 16
widthVol, heightVol = 32, 16
marginX, marginY = 8, 8
gapX, gapY = 8, 8 


def formatOutput(x, y, w, h, i, v):
    print('Edit')
    print('{')
    print('    Title "Edit"')
    print(f'    X "{x}"')
    print(f'    Y "{y}"')
    print(f'    Width "{w}"')
    print(f'    Height "{h}"')
    print(f'    IDC_EDIT{i}')
    print(f'    Value "{v}{i//2}"')
    print(f'    SetFocus "0"')
    print('}')

def boxText(row, col, counter):
    posX = marginX + (widthText + widthVol + gapX) * col
    posY = marginY + (heightText + gapY) * row
    width = widthText
    height = heightText
    value = "name_"
    
    formatOutput(posX, posY, width, height, counter, value)

def boxVol(row, col, counter):
    posX = marginX + widthText + (widthVol + gapX + widthText) * col
    posY = marginY + (heightVol + gapY) * row
    width = widthVol
    height = heightVol
    
    value = 'volume_'
    formatOutput(posX, posY, width, height, counter, value)

#

controlID = 0
for col in range (5):
    for row in range(10):
        boxText(row, col, controlID)
        controlID = controlID + 1
        boxVol(row, col, controlID)
        controlID = controlID + 1
