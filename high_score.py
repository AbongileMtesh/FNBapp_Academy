while True:
    game_score = input("Enter your game score: ").strip().lower()

    if game_score == "stop":
     print("Game session ended!")
     break
    else:
       game_score2 = int(game_score)
       if game_score2 > 100:
          print("Wow! Thats  a high score")
       else:
          print("Keep trying!")

 
       


