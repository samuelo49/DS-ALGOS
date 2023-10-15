"""
Oliver the Dog is missing his favorite hat and is asking his friends
at the dog park if they've seen it. Each dog either has seen it or suggests
a list of other dogs to ask. Return the name of the dog who has seen the hat.
Oliver starts out by asking his best friend. This function will take two parameters.
The first is a map of dogs to a list of their friends.
The second is Oliver's best friend, who Oliver will ask first.


One of the most common uses of a queue is to keep a list of "work to be done".
Just like doing housework, often new things get added to the to-do list while
doing some other task. New jobs get added to the end of the queue, and when one
is complete,the next one is taken from the top of the list.
let dogs = {
  'Carter': ['Fido', 'Ivy'],
  'Ivy': ["HAT"], // Ivy has seen the hat
  'Loki': ['Snoopy'],
  'Pepper': ['Carter'],
  'Snoopy': ['Pepper'],
  'Fido': []
};
console.log(findHat(dogs, 'Loki')); // returns 'Ivy'
"""

def findHat(dogs, bestFriend):
    dogsToAsk = [bestFriend]
    dogsAlreadyAsked = set()
    while len(dogsToAsk) > 0:
        nextDogToAsk = dogsToAsk.pop()
        if nextDogToAsk in dogsAlreadyAsked:
            continue
        for dog in dogs[nextDogToAsk]:
            if dog == 'HAT':
                return nextDogToAsk
            dogsAlreadyAsked.add(nextDogToAsk)
            dogsToAsk.append(dog)
    return "Couldn't find the hat"


dogs = {'Carter': ['Fido', 'Ivy'],
        'Ivy': ["HAT"],
        'Loki': ['Snoopy'],
        'Pepper': ['Carter'],
        'Snoopy': ['Pepper'],
        'Fido': []
        }
print(findHat(dogs, 'Loki'))
