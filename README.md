Just some little ai thing im working on, if I end up liking it I think I may try and convert the AI part into its own library I can just call up. 

Blackjack playing AI, will hopefully end up counting a couple cards. 

The objective is to get the bot to make a profit, which shouldn't be too hard as I am adding in some basic info that will let it count cards. 

Current thoughts on neurons:

input:

Players first card

Players second card

Dealers show card

Total value on board

Total value since shuffle

output:

Hit

Stand

Split

Bet amount (% of total value at table)

Still trying to decide on the fitness, I am thinking either %changed per hand, or total %changed over X hands. 

