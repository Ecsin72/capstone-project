# capstone-project
This project is a Wordle game coded via my own skills rather than the skills of the example provided.

The game works  by using the list of valid Wordle game words provided by the NYT and available for download as a text file on github which is the extra file in the repository; this is converted into a list that we can use throughout the code.

Next, I have created a class called WordleGame to be able to set up game variables and manage the new list of words we have created. Most importantly the class allows us to have a random target word selected for the game without the player setting it up or seeing so you can actually play the game with no cheating.

The next big step in code is the Wordle function that compares the player's guess and the random target so it can give the classic colour feedback from the original game.It checks that both variables are 5 letters long, creates a default output list of all 'Red' letters and makes a remaining letters list so that letters cannot be counted twice. The function works in two passes, the first one checks for letters that are exactly the same (position and content) so it can mark them green, then the second pass checks for letters that are the same in content but not in position. Finally the resulting string of colours is returned.

I added a tracker with two variables, current guesses and corresponding outputs so the player can see these at all times when they play as this is a feature of the game.

Finally the last function is the one that allows the user to play, it asks for a guess and will return the output and print the tracker off for the player to look at. It loops through this until the player guesses the target word exactly then the player is told they have won.