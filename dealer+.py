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
print(f"r2 overall {sum(r2['NoAces'].values()) + sum(r2['Aces'].values())} = 13**2 = {13**2}")
#r2['NoAces'] {4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7, 11: 8, 12: 15, 13: 14, 14: 13, 15: 12, 16: 11, 17: 10, 18: 9, 19: 8, 20: 16}
#r2['Aces'] {2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 17: 2, 18: 2, 19: 2, 20: 2, 21: 8}
#r2 overall 169 (13**2 = 169)
print(*list({k:r2['NoAces'].get(k,0)} for k in range(17,23)))
print(*list({k:r2['Aces'].get(k,0)} for k in range(17,23)))
print(*list({k:r2['NoAces'].get(k,0)+r2['Aces'].get(k,0)} for k in range(17,23)))
print("Probability distribution for dealer's stop with 2 cards")
print(*list({k:13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0))} for k in range(17,23)))
print(f"Probability to stop with 2 or fewer cards is {sum(13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0)) for k in range(17,23))}")
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
print(f"r3 overall {sum(r3['NoAces'].values()) + sum(r3['Aces'].values())}+13*{sum(r2['NoAces'].get(k,0) for k in range(17,23))+sum(r2['Aces'].get(k,0) for k in range(17,23))}=13**3={13**3}")
#r3['NoAces'] {6: 1, 7: 3, 8: 6, 9: 10, 10: 15, 11: 21, 12: 28, 13: 36, 14: 54, 15: 70, 16: 84, 17: 96, 18: 106, 19: 104, 20: 101, 21: 97, 22: 380}
#r3['Aces'] {3: 1, 4: 3, 5: 6, 6: 9, 12: 20, 13: 29, 14: 26, 15: 23, 16: 20, 17: 23, 18: 13, 19: 14, 20: 15, 21: 16}
# 1430+13*(10+9+8+16+2+2+2+2+8)=13**3=2197
print(*list({k:r3['NoAces'].get(k,0)} for k in range(17,23)))
print(*list({k:r3['Aces'].get(k,0)} for k in range(17,23)))
print(*list({k:r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)} for k in range(17,23)))
print("Probabilities for dealer's stop with 3 cards")
print(*list({k : 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0))} for k in range(17,23)))
print("Probability distribution for dealer's stop with 3 or fewer cards")
print(*list({k : 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0))} for k in range(17,23)))
print(f"Probability to stop with 3 or fewer cards is {sum(13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0)) for k in range(17,23))}")
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
print(f"r4 overall {sum(r4['NoAces'].values()) + sum(r4['Aces'].values())} + 13**2*{sum(r2['NoAces'].get(k,0) for k in range(17,23))+sum(r2['Aces'].get(k,0) for k in range(17,23))} + 13*{sum(r3['NoAces'].get(k,0) for k in range(17,23))+sum(r3['Aces'].get(k,0) for k in range(17,23))} = 13**4 = {13**4}")
#r4['NoAces'] {8: 1, 9: 4, 10: 10, 11: 20, 12: 35, 13: 56, 14: 84, 15: 120, 16: 177, 17: 252, 18: 342, 19: 348, 20: 353, 21: 356, 22: 1778}
#r4['Aces'] {4: 1, 5: 4, 6: 10, 12: 40, 13: 70, 14: 112, 15: 162, 16: 204, 17: 222, 18: 140, 19: 143, 20: 147, 21: 152, 22: 702}
#r4 overall 6045 (13**4 = 28561)
#>>> 6045 + 13**2*(10+9+8+16+2+2+2+2+8) + 13*(96+106+104+101+97+380+23+13+14+15+16) = 13**4 = #28561
print(*list({k:r4['NoAces'].get(k,0)} for k in range(17,23)))
print(*list({k:r4['Aces'].get(k,0)} for k in range(17,23)))
print(*list({k:r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)} for k in range(17,23)))
print("Probabilities for dealer's stop with 4 cards")
print(*list({k:13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0))} for k in range(17,23)))
print("Probability distribution for dealer's stop with 4 or fewer cards")
print(*list({k : 13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0))} for k in range(17,23)))
print(f"Probability to stop with 4 or fewer cards is {sum(13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0)) for k in range(17,23))}")
# 5-th card
r5 = {'NoAces':{}, 'Aces':{}}
r5['NoAces'].fromkeys(range(0,23),0)
r5['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            elif total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            else: # play continues
                new_total = total_cards + c
            NoAces = r4['NoAces'].get(total_cards,0)
            Aces = r4['Aces'].get(total_cards,0)
            NewAces = r5['Aces'].get(new_total,0)
            new_value = NewAces + NoAces + Aces
            if new_value > 0:
                r5['Aces'][new_total] = new_value
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
            NoAces = r4['NoAces'].get(total_cards,0)
            Aces = r4['Aces'].get(total_cards,0)
            NewNoAces = r5['NoAces'].get(new_total,0)
            new_valueNo = NewNoAces + score * NoAces
            if new_valueNo > 0:
                r5['NoAces'][new_total] = new_valueNo
            if total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            NewAces = r5['Aces'].get(new_total,0)
            new_value = NewAces + score * Aces
            if new_value > 0:
                r5['Aces'][new_total] = new_value
print(f"r5['NoAces'] {dict(sorted(r5['NoAces'].items()))}")
print(f"r5['Aces'] {dict(sorted(r5['Aces'].items()))}")
print(f"r5 overall {sum(r5['NoAces'].values()) + sum(r5['Aces'].values())} (13**5 = {13**5})")
print(f"r5 overall {sum(r5['NoAces'].values()) + sum(r5['Aces'].values())} + 13**3*{sum(r2['NoAces'].get(k,0) for k in range(17,23))+sum(r2['Aces'].get(k,0) for k in range(17,23))} + 13**2*{sum(r3['NoAces'].get(k,0) for k in range(17,23))+sum(r3['Aces'].get(k,0) for k in range(17,23))} +13*{sum(r4['NoAces'].get(k,0) for k in range(17,23))+sum(r4['Aces'].get(k,0) for k in range(17,23))} = 13**5 = {13**5}")
#r5['NoAces'] {10: 1, 11: 5, 12: 15, 13: 35, 14: 70, 15: 126, 16: 210, 17: 330, 18: 510, 19: 518, 20: 532, 21: 552, 22: 3180}
#r5['Aces'] {5: 1, 6: 5, 12: 35, 13: 90, 14: 184, 15: 332, 16: 544, 17: 780, 18: 603, 19: 604, 20: 607, 21: 613, 22: 3948}
#r5 overall 14430 (13**5 = 371293)
#r5 overall 14430 + 13**3*59 + 13**2*965 +13*4935 = 13**5 = 371293
print(*list({k:r5['NoAces'].get(k,0)} for k in range(17,23)))
print(*list({k:r5['Aces'].get(k,0)} for k in range(17,23)))
print(*list({k:r5['NoAces'].get(k,0)+r5['Aces'].get(k,0)} for k in range(17,23)))
print("Probabilities for dealer's stop with 5 cards")
print(*list({k:13**(-5)*(r5['NoAces'].get(k,0)+r5['Aces'].get(k,0))} for k in range(17,23)))
print("Probability distribution for dealer's stop with 5 or fewer cards")
print(*list({k : 13**(-5)*(r5['NoAces'].get(k,0)+r5['Aces'].get(k,0)) + 13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0))} for k in range(17,23)))
print(f"Probability to stop with 5 or fewer cards is {sum(13**(-5)*(r5['NoAces'].get(k,0)+r5['Aces'].get(k,0)) + 13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0)) for k in range(17,23))}")
# 6-th card
r6 = {'NoAces':{}, 'Aces':{}}
r6['NoAces'].fromkeys(range(0,23),0)
r6['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            elif total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            else: # play continues
                new_total = total_cards + c
            NoAces = r5['NoAces'].get(total_cards,0)
            Aces = r5['Aces'].get(total_cards,0)
            NewAces = r6['Aces'].get(new_total,0)
            new_value = NewAces + NoAces + Aces
            if new_value > 0:
                r6['Aces'][new_total] = new_value
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
            NoAces = r5['NoAces'].get(total_cards,0)
            Aces = r5['Aces'].get(total_cards,0)
            NewNoAces = r6['NoAces'].get(new_total,0)
            new_valueNo = NewNoAces + score * NoAces
            if new_valueNo > 0:
                r6['NoAces'][new_total] = new_valueNo
            if total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            NewAces = r6['Aces'].get(new_total,0)
            new_value = NewAces + score * Aces
            if new_value > 0:
                r6['Aces'][new_total] = new_value
print(f"r6['NoAces'] {dict(sorted(r6['NoAces'].items()))}")
print(f"r6['Aces'] {dict(sorted(r6['Aces'].items()))}")
print(f"r6 overall {sum(r6['NoAces'].values()) + sum(r6['Aces'].values())} (13**6 = {13**6})")
print(f"r6 overall {sum(r6['NoAces'].values()) + sum(r6['Aces'].values())} + 13*{sum(r5['NoAces'].get(k,0) for k in range(17,23))+sum(r5['Aces'].get(k,0) for k in range(17,23))} + 13**2*{sum(r4['NoAces'].get(k,0) for k in range(17,23))+sum(r4['Aces'].get(k,0) for k in range(17,23))} + 13**3*{sum(r3['NoAces'].get(k,0) for k in range(17,23))+sum(r3['Aces'].get(k,0) for k in range(17,23))} + 13**4*{sum(r2['NoAces'].get(k,0) for k in range(17,23))+sum(r2['Aces'].get(k,0) for k in range(17,23))} = 13**6 = {13**6}")
#r6['NoAces'] {12: 1, 13: 6, 14: 21, 15: 56, 16: 126, 17: 252, 18: 462, 19: 462, 20: 465, 21: 476, 22: 3217}
#r6['Aces'] {6: 1, 12: 11, 13: 56, 14: 166, 15: 388, 16: 787, 17: 1401, 18: 1191, 19: 1191, 20: 1191, 21: 1192, 22: 8370}
#r6 overall 21489 (13**6 = 4826809)
#r6 overall 21489 + 13*12777 + 13**2*4935 + 13**3*965 + 13**4*59 = 13**6 = 4826809
print(*list({k:r6['NoAces'].get(k,0)} for k in range(17,23)))
print(*list({k:r6['Aces'].get(k,0)} for k in range(17,23)))
print(*list({k:r6['NoAces'].get(k,0)+r6['Aces'].get(k,0)} for k in range(17,23)))
#{17: 252} {18: 462} {19: 462} {20: 465} {21: 476} {22: 3217}
#{17: 1401} {18: 1191} {19: 1191} {20: 1191} {21: 1192} {22: 8370}
#{17: 1653} {18: 1653} {19: 1653} {20: 1656} {21: 1668} {22: 11587}
print("Probabilities for dealer's stop with 6 cards")
print(*list({k:13**(-6)*(r6['NoAces'].get(k,0)+r6['Aces'].get(k,0))} for k in range(17,23)))
print("Probability distribution for dealer's stop with 6 or fewer cards")
print(*list({k : 13**(-6)*(r6['NoAces'].get(k,0)+r6['Aces'].get(k,0)) + 13**(-5)*(r5['NoAces'].get(k,0)+r5['Aces'].get(k,0)) + 13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0))} for k in range(17,23)))
print(f"Probability to stop with 6 or fewer cards is {sum(13**(-6)*(r6['NoAces'].get(k,0)+r6['Aces'].get(k,0)) + 13**(-5)*(r5['NoAces'].get(k,0)+r5['Aces'].get(k,0)) + 13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0)) for k in range(17,23))}")
# 7-th card
r7 = {'NoAces':{}, 'Aces':{}}
r7['NoAces'].fromkeys(range(0,23),0)
r7['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        for total_cards in range(1,17):
            if total_cards + c > 21: # Dealer busts! Player wins.
                new_total = 22
            elif total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            else: # play continues
                new_total = total_cards + c
            NoAces = r6['NoAces'].get(total_cards,0)
            Aces = r6['Aces'].get(total_cards,0)
            NewAces = r7['Aces'].get(new_total,0)
            new_value = NewAces + NoAces + Aces
            if new_value > 0:
                r7['Aces'][new_total] = new_value
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
            NoAces = r6['NoAces'].get(total_cards,0)
            Aces = r6['Aces'].get(total_cards,0)
            NewNoAces = r7['NoAces'].get(new_total,0)
            new_valueNo = NewNoAces + score * NoAces
            if new_valueNo > 0:
                r7['NoAces'][new_total] = new_valueNo
            if total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                new_total = total_cards + c + 10
            NewAces = r7['Aces'].get(new_total,0)
            new_value = NewAces + score * Aces
            if new_value > 0:
                r7['Aces'][new_total] = new_value
print(f"r7['NoAces'] {dict(sorted(r7['NoAces'].items()))}")
print(f"r7['Aces'] {dict(sorted(r7['Aces'].items()))}")
print(f"r7 overall {sum(r7['NoAces'].values()) + sum(r7['Aces'].values())} (13**7 = {13**7})")
print(f"r7 overall {sum(r7['NoAces'].values()) + sum(r7['Aces'].values())} + 13*{sum(r6['NoAces'].get(k,0) for k in range(17,23))+sum(r6['Aces'].get(k,0) for k in range(17,23))} + 13**2*{sum(r5['NoAces'].get(k,0) for k in range(17,23))+sum(r5['Aces'].get(k,0) for k in range(17,23))} + 13**3*{sum(r4['NoAces'].get(k,0) for k in range(17,23))+sum(r4['Aces'].get(k,0) for k in range(17,23))} + 13**4*{sum(r3['NoAces'].get(k,0) for k in range(17,23))+sum(r3['Aces'].get(k,0) for k in range(17,23))} + 13**5*{sum(r2['NoAces'].get(k,0) for k in range(17,23))+sum(r2['Aces'].get(k,0) for k in range(17,23))} = 13**7 = {13**7}")
#r7['NoAces'] {14: 1, 15: 7, 16: 28, 17: 84, 18: 210, 19: 210, 20: 210, 21: 210, 22: 1560}
#r7['Aces'] {12: 1, 13: 13, 14: 74, 15: 255, 16: 681, 17: 1535, 18: 1409, 19: 1409, 20: 1409, 21: 1409, 22: 10332}
#r7 overall 21047 (13**7 = 62748517)
#r7 overall 21047 + 13*19870 + 13**2*12777 + 13**3*4935 + 13**4*965 + 13**5*59 = 13**7 = 62748517
print(*list({k:r7['NoAces'].get(k,0)} for k in range(17,23)))
print(*list({k:r7['Aces'].get(k,0)} for k in range(17,23)))
print(*list({k:r7['NoAces'].get(k,0)+r7['Aces'].get(k,0)} for k in range(17,23)))
#{17: 84} {18: 210} {19: 210} {20: 210} {21: 210} {22: 1560}
#{17: 1535} {18: 1409} {19: 1409} {20: 1409} {21: 1409} {22: 10332}
#{17: 1619} {18: 1619} {19: 1619} {20: 1619} {21: 1619} {22: 11892}
print("Probabilities for dealer's stop with 7 cards")
print(*list({k:13**(-7)*(r7['NoAces'].get(k,0)+r7['Aces'].get(k,0))} for k in range(17,23)))
print("Probability distribution for dealer's stop with 7 or fewer cards")
print(*list({k : 13**(-7)*(r7['NoAces'].get(k,0)+r7['Aces'].get(k,0)) + 13**(-6)*(r6['NoAces'].get(k,0)+r6['Aces'].get(k,0)) + 13**(-5)*(r5['NoAces'].get(k,0)+r5['Aces'].get(k,0)) + 13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0))} for k in range(17,23)))
print(f"Probability to stop with 7 or fewer cards is {sum(13**(-7)*(r7['NoAces'].get(k,0)+r7['Aces'].get(k,0)) + 13**(-6)*(r6['NoAces'].get(k,0)+r6['Aces'].get(k,0)) + 13**(-5)*(r5['NoAces'].get(k,0)+r5['Aces'].get(k,0)) + 13**(-4)*(r4['NoAces'].get(k,0)+r4['Aces'].get(k,0)) + 13**(-3)*(r3['NoAces'].get(k,0)+r3['Aces'].get(k,0)) + 13**(-2)*(r2['NoAces'].get(k,0)+r2['Aces'].get(k,0)) for k in range(17,23))}")
