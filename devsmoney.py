devs_money = 100
dev_can_play_smash

if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament")
elif devs_money < 1 and dev_can_play_smash:
    print("Dev is too poor to play smash")
else:
    print("Dev just cant play smash")