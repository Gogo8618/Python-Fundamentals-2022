teams = input().split(' ')

team_A = 11
team_B = 11

failed_payers = []
in_boolean = False
for player in teams:
    if 'A' in player:
        team_A -= 1
    elif 'B' in player:
        team_B -= 1
    if team_A < 7 or team_B < 7:
        in_boolean = True
        break
if in_boolean:
    print(f"Team A - {team_A}; Team B - {team_B}")
    print("Game was terminated.")
else:
    print(f"Team A - {team_A}; Team B - {team_B}")

