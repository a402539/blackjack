# 1-st card
r1 = {'NoAces':{}, 'Aces':{}}
r1['NoAces'].fromkeys(range(0,23),0)
r1['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        r1['Aces'][1] = 1
    elif c == 10:
        r1['NoAces'][c] = 4;
    else:
        r1['NoAces'][c] = 1
print(f"r1['NoAces'] {dict(sorted(r1['NoAces'].items()))}")
print(f"r1['Aces'] {dict(sorted(r1['Aces'].items()))}")
print(f"r1 overall {sum(r1['NoAces'].values()) + sum(r1['Aces'].values())}")
#r1['NoAces'] {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 4}
#r1['Aces'] {1: 1}
#r1 overall 13
# 2-nd card
r2 = {'NoAces':{}, 'Aces':{}}
r2['NoAces'].fromkeys(range(0,23),0)
r2['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            elif total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            else: # play continues
                new_total = total_cards + c
            NoAces = r1['NoAces'].get(total_cards,0)
            Aces = r1['Aces'].get(total_cards,0)
            NewAces = r2['Aces'].get(new_total,0)
            new_value = NewAces + NoAces + Aces
            if new_value > 0:
                r2['Aces'][new_total] = new_value
    else:
        if c ==  10:
            score = 4
        else:
            score = 1
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            else: # play continues
                new_total = total_cards + c
            NoAces = r1['NoAces'].get(total_cards,0)
            Aces = r1['Aces'].get(total_cards,0)
            NewNoAces = r2['NoAces'].get(new_total,0)
            new_valueNo = NewNoAces + score * NoAces
            if new_valueNo > 0:
                r2['NoAces'][new_total] = new_valueNo
            if total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            NewAces = r2['Aces'].get(new_total,0)
            new_value = NewAces + score * Aces
            if new_value > 0:
                r2['Aces'][new_total] = new_value
print(f"r2['NoAces'] {dict(sorted(r2['NoAces'].items()))}")
print(f"r2['Aces'] {dict(sorted(r2['Aces'].items()))}")
print(f"r2 overall {sum(r2['NoAces'].values()) + sum(r2['Aces'].values())} (13**2 = {13**2})")
#r2['NoAces'] {4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7, 11: 8, 12: 15, 13: 14, 14: 13, 15: 12, 16: 11, 17: 10, 18: 9, 19: 8, 20: 16}
#r2['Aces'] {2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 8}
#r2 overall 169 (13**2 = 169)
# 3-rd card
r3 = {'NoAces':{}, 'Aces':{}}
r3['NoAces'].fromkeys(range(0,23),0)
r3['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            elif total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            else: # play continues
                new_total = total_cards + c
            NoAces = r2['NoAces'].get(total_cards,0)
            Aces = r2['Aces'].get(total_cards,0)
            NewAces = r3['Aces'].get(new_total,0)
            new_value = NewAces + NoAces + Aces
            if new_value > 0:
                r3['Aces'][new_total] = new_value
    else:
        if c ==  10:
            score = 4
        else:
            score = 1
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            else: # play continues
                new_total = total_cards + c
            NoAces = r2['NoAces'].get(total_cards,0)
            Aces = r2['Aces'].get(total_cards,0)
            NewNoAces = r3['NoAces'].get(new_total,0)
            new_valueNo = NewNoAces + score * NoAces
            if new_valueNo > 0:
                r3['NoAces'][new_total] = new_valueNo
            if total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            NewAces = r3['Aces'].get(new_total,0)
            new_value = NewAces + score * Aces
            if new_value > 0:
                r3['Aces'][new_total] = new_value
print(f"r3['NoAces'] {dict(sorted(r3['NoAces'].items()))}")
print(f"r3['Aces'] {dict(sorted(r3['Aces'].items()))}")
print(f"r3 overall {sum(r3['NoAces'].values()) + sum(r3['Aces'].values())} (13**3 = {13**3})")
#r3['NoAces'] {6: 1, 7: 3, 8: 6, 9: 10, 10: 15, 11: 21, 12: 28, 13: 36, 14: 54, 15: 70, 16: 84, 17: 96, 18: 106, 19: 104, 20: 101, 21: 97, 22: 380}
#r3['Aces'] {3: 1, 4: 3, 5: 6, 6: 9, 12: 20, 13: 29, 14: 26, 15: 23, 16: 20, 17: 23, 18: 13, 19: 14, 20: 15, 21: 16}
#r3 overall 1430 (13**3 = 2197)
#>>> 1430+13*(10+9+8+16+2+2+2+2+8)
#2197
# 4-th card
r4 = {'NoAces':{}, 'Aces':{}}
r4['NoAces'].fromkeys(range(0,23),0)
r4['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            elif total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            else: # play continues
                new_total = total_cards + c
            NoAces = r3['NoAces'].get(total_cards,0)
            Aces = r3['Aces'].get(total_cards,0)
            NewAces = r4['Aces'].get(new_total,0)
            new_value = NewAces + NoAces + Aces
            if new_value > 0:
                r4['Aces'][new_total] = new_value
    else:
        if c ==  10:
            score = 4
        else:
            score = 1
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            else: # play continues
                new_total = total_cards + c
            NoAces = r3['NoAces'].get(total_cards,0)
            Aces = r3['Aces'].get(total_cards,0)
            NewNoAces = r4['NoAces'].get(new_total,0)
            new_valueNo = NewNoAces + score * NoAces
            if new_valueNo > 0:
                r4['NoAces'][new_total] = new_valueNo
            if total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            NewAces = r4['Aces'].get(new_total,0)
            new_value = NewAces + score * Aces
            if new_value > 0:
                r4['Aces'][new_total] = new_value
print(f"r4['NoAces'] {dict(sorted(r4['NoAces'].items()))}")
print(f"r4['Aces'] {dict(sorted(r4['Aces'].items()))}")
print(f"r4 overall {sum(r4['NoAces'].values()) + sum(r4['Aces'].values())} (13**4 = {13**4})")
#r4['NoAces'] {8: 1, 9: 4, 10: 10, 11: 20, 12: 35, 13: 56, 14: 84, 15: 120, 16: 177, 17: 252, 18: 342, 19: 348, 20: 353, 21: 356, 22: 1778}
#r4['Aces'] {4: 1, 5: 4, 6: 10, 12: 40, 13: 70, 14: 112, 15: 162, 16: 204, 17: 222, 18: 140, 19: 143, 20: 147, 21: 152, 22: 702}
#r4 overall 6045 (13**4 = 28561)
#>>> 6045+13*(13*(10+9+8+16+2+2+2+2+8)+(96+106+104+101+97+380+23+13+14+15+16))
#28561
