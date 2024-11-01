
'''
❓ PROMPT
You are designing an iPhone carousel widget that displays a list of apps in a vertical scrolling carousel. The apps array contains the names of the apps in the carousel from bottom 
to the top (index 0 for the bottom). The commands array contains the list of commands to navigate the vertical carousel, in all lowercase: "scroll up", "scroll down", and "tap".

The carousel works as follows:
* Initially, the first app in the apps array is selected.
* If the user taps on an app, it opens the app.
* If the user scrolls up, the carousel moves one app up. If the user scrolls down, the carousel moves one app down.
* If the user scrolls past the top of the carousel, the carousel wraps around to the bottom, and vice versa.
* Your task is to simulate the behavior of the carousel and return an array of strings representing the names of the opened apps.

Assume with every subsequent command, the user is already back on the home page, scrolling through the carousel again.

Example(s)
let apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
let commands = ["tap", "scroll down", "scroll up", "scroll up", "scroll down", "scroll down", "tap"]

In this example, we first tap on "Maps" in the carousel (Index 0)
Scrolling down takes you to "Settings" (Index 4)
Scrolling up takes you back to "Maps" (Index 0)
Scrolling up takes you to "Music" (Index 1)
Scrolling down takes you to "Maps" (index 0)
Scrolling down again takes you to "Settings" (index 4)
Tap to open "Settings" (index 4)

Output: ["Maps", "Settings"]
 

🔎 EXPLORE
List your assumptions & discoveries:
let apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
let commands = ["tap", "scroll down", "scroll up", "scroll up", "scroll down", "scroll down", "tap"]

let apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
let commands = ["tap", "scroll up", "scroll up", "scroll up", "tap", "scroll down", "scroll down","tap"]
output = ["Maps", "Music","Messages"]

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
- use a variable to keep track of selected app on the carousel
- Loop through the list of commands.
- If the user performs a Tap, then add the current command index to a return list
- IF the user scrolls up or down, change the index with the appropriate direction.(up+1, Down - 1)
- Make sure to calcuate for teh circular array.i.e scrolling down on 0th index takes you to the last index of the array.
 

🛠️ IMPLEMENT
function simulateCarousel(apps, commands){} // returns list of str
def simulate_carousel(apps: list[str], commands: list[str]) -> list[str]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def simulate_carousel(apps: list[str], commands: list[str]) -> list[str]:
    selectedApp = 0
    numApps = len(apps)
    result = []
    for command in commands:
        if command == "tap":
            result.append(apps[selectedApp])
        elif command == "scroll up":
            selectedApp = (selectedApp + 1) % numApps
        elif command == "scroll down":
            selectedApp = (selectedApp - 1) % numApps
    
    return result



apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["tap", "scroll down", "scroll up", "scroll up", "scroll down", "scroll down", "tap"]
result = simulate_carousel(apps, commands)
print(result == ["Maps", "Settings"])

# Test Case 1: No commands
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = []
print(simulate_carousel(apps, commands) == [])

# Test Case 2: Single "tap" command
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["tap"]
print(simulate_carousel(apps, commands) == ["Maps"])

# Test Case 3: Single "scroll up" command
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["scroll up", "tap"]
print(simulate_carousel(apps, commands) == ["Music"])

# Test Case 4: Single "scroll down" command
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["scroll down", "tap"]
print(simulate_carousel(apps, commands) == ["Settings"])

# Test Case 5: Multiple "scroll up" and "scroll down" commands
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["scroll down", "scroll up", "scroll up", "scroll up", "scroll up", "tap"]
print(simulate_carousel(apps, commands) == ["Messages"])

# Test Case 6: Mix of "tap", "scroll up", and "scroll down" commands
apps = ["Maps", "Music", "Photos", "Messages", "Settings"]
commands = ["tap", "scroll up", "tap", "scroll down", "tap", "scroll down", "tap"]
print(simulate_carousel(apps, commands) == ["Maps", "Music", "Maps", "Settings"])

# Test Case 7: Carousel with only one app
apps = ["Maps"]
commands = ["tap", "scroll up", "scroll down", "tap"]
print(simulate_carousel(apps, commands) == ["Maps", "Maps"])

# Test Case 8: Carousel with only one app & scroll spam
apps = ["Maps"]
commands = ["scroll up", "scroll up", "tap", "scroll up", "scroll up", "scroll up", "scroll up", "tap"]
print(simulate_carousel(apps, commands) == ["Maps", "Maps"])