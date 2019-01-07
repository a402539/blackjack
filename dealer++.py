print("1-st card")
p = {'NoAces':{}, 'Aces':{}}
p['NoAces'].fromkeys(range(0,23),0)
p['Aces'].fromkeys(range(0,23),0)
for c in range(1,11):
    if c == 1:
        p['Aces'][1] = 1/13
    elif c == 10:
        p['NoAces'][c] = 4/13;
    else:
        p['NoAces'][c] = 1/13
print(f"p['NoAces'] {dict(sorted(p['NoAces'].items()))}")
print(f"p['Aces'] {dict(sorted(p['Aces'].items()))}")
print(f"p overall {sum(p['NoAces'].values()) + sum(p['Aces'].values())}")
#r['NoAces'] {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 4}
#r['Aces'] {1: 1}
#r overall 13
d = {}
for card in range(2,10):
    print(f"{card} cards")
    q = {'NoAces':{}, 'Aces':{}}
    q['NoAces'].fromkeys(range(0,23),0)
    q['Aces'].fromkeys(range(0,23),0)
    for c in range(1,11):
        if c == 1:
            for total_cards in range(1,17):
                if total_cards + c > 21: # Dealer busts! Player wins.
                    new_total = 22
                elif total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                    new_total = total_cards + c + 10
                else: # play continues
                    new_total = total_cards + c
                NoAces = p['NoAces'].get(total_cards,0)
                Aces = p['Aces'].get(total_cards,0)
                NewAces = q['Aces'].get(new_total,0)
                new_value = NewAces + (NoAces + Aces)/13
                if new_value > 0:
                    q['Aces'][new_total] = new_value
        else:
            if c ==  10:
                score = 4/13
            else:
                score = 1/13
            for total_cards in range(1,17):
                if total_cards + c > 21: # Dealer busts! Player wins.
                    new_total = 22
                else: # play continues
                    new_total = total_cards + c
                NoAces = p['NoAces'].get(total_cards,0)
                Aces = p['Aces'].get(total_cards,0)
                NewNoAces = q['NoAces'].get(new_total,0)
                new_valueNo = NewNoAces + score * NoAces
                if new_valueNo > 0:
                    q['NoAces'][new_total] = new_valueNo
                if total_cards + c > 6 and total_cards + c < 12: # Dealer stops
                    new_total = total_cards + c + 10
                NewAces = q['Aces'].get(new_total,0)
                new_value = NewAces + score * Aces
                if new_value > 0:
                    q['Aces'][new_total] = new_value
    print(f"q['NoAces'] {dict(sorted(q['NoAces'].items()))}")
    print(f"q['Aces'] {dict(sorted(q['Aces'].items()))}")
    print(f"q overall {sum(q['NoAces'].values()) + sum(q['Aces'].values()) + sum(d[m][k] for m in d.keys() for k in range(17,23))} = 1")
    d[card] = {}.fromkeys(range(17,23),0)
    for m in range(17,23):
        d[card][m] = q['NoAces'].get(m,0) + q['Aces'].get(m,0)
    print(f"distribution for stop with {card} cards")
    print(dict(sorted(d[card].items())))
    print(f" distribution for stop with {card} of fewer cards")
    print(list({k:sum(d[m][k] for m in d.keys())} for k in range(17,23)))
    p = q
# {17: 0.14512590362524794}, {18: 0.13949692597148125}, {19: 0.13346395470620018},
# {20: 0.18025242302968267}, {21: 0.12006794090080618}, {22: 0.2815928404506306}
print(f"Total percent investigated {100*sum(sum(d[m].values()) for m in range(2,10))}")
