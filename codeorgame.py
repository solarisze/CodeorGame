print("You are sitting in the library in fifth period. You have a study hall, so there's nothing you're required to do at the moment. You have a couple options until school ends, in an hour. You can wait for your father to purchase video games and send you the Stealth codes for them, or you can code something in Viper. What will you do?")
# Loop back to the beginning of loop. 
# Initialize variables. 
choice1 = input("('Code' to play around with Viper, 'Wait' to wait for the video games.)")

# a bunch of choices and stuff to keep it consistent and vaguely easier to read
code = "Code"
meta_dnd = "('Meta' for a fourth wall breaking meta-commentary on your current position that drags on entirely too long and becomes a multi-day project, 'DND' for a quick Daggers and Danger-themed adventure.)"
meta = "Meta"
dnd = "DND"
wait = "Wait"
wepipe_read = "('Video' to watch WePipe, 'Read' to read a book)"; 
video = "Video"


if (choice1 == code): print("You sit for a second before opening Optical Workspace Program. You decide to make a choose your own adventure style text game- What should it be about?"); print(meta_dnd)  
choice11 = input() #choice 1 route 1
if (choice11 == meta): print("You start typing an adventure shockingly like this one, but you replace all the product names with obviously non-trademarked versions. Viper becomes Python, WePipe becomes YouTube, Daggers and Danger becomes Dungeons and Dragons, you know. Clearly rediculous names. You test it- it doesn't send you back to the choice when you say something not predefined. Dammit. You look up one tutorial, then another- Why is none of this working? Fast forward a day, still fifth period. You're sitting in Science class, ignoring the Big Project the teacher has been talking about for entirely too long. You're allowed to use your laptop- awesome. You open up Optical Workspace Program- something you've dubbed 'Visual Studio Code' in your project- and keep typing. You've just fixed the bug where your code will loop the text 'Sorry, what was that?' endlessly no matter what you input, which is good. You decide to add more options- you only had two, and you'd prefer to finish this project sooner rather than later. You don't have a set stopping point, you just know you'll know it when you get there. Every word you write in your print() functions ticks up in your head- 150, 200, 1000. How much have you just written? You don't know. You should probably move on to the next option soon, you think. But you don't. You keep writing until you can't think of anything else, and then some. It's halfway through fifth period. You wish you could get yourself to stop typing, to do anything else, to work on anything else. All your schoolwork is overdue, and the ones that aren't aren't good enough. Nothing is good enough except an A+. A is for average, B is for bad, C is for Crappy, D is for disasterous, F is for failure. You know that's not actually what they stand for, but nobody's ever told you the true meanings, and that's what they feel like. Failure. Failure. Failure. You're average at best. You stop. Why isn't average enough for you? It's enough for everyone else.")
if (choice1 == wait): print("You sit down and look around. There's not much to do- you could find a book, or watch one of your favourite WePipers videos, he seems to have uploaded recently. What now?"); print(wepipe_read)
choice12 = input() #choice 1 route 2
if (choice12 == video): print("You open WeTube, and it looks like you were right- DogDog uploaded recently. It seems like just a few hours ago, too, so you wouldn't have had time to watch this one yet. You can watch DogDog's new Amazing Larceny Vehicle video, or you can watch a Daggers and Danger video. What do you want to do?")
 
