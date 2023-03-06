skumria_price = float(input())
caca_price = float(input())
palamud_weight = float(input())
safrid_weight = float(input())
midi = int(input())
palamud_price = skumria_price * 1.6
safrid_price = caca_price * 1.8
final_price = palamud_price * palamud_weight + safrid_price * safrid_weight + midi * 7.5
print(f"{final_price:.2f}")