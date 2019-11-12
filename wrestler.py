#!/usr/bin/env python3

import sys


def main():
    lineup = openFile(sys.argv[1])
    matchups = parseMatchups(lineup)
    teams = bfs(matchups)


# Open the file with the passed name as read only, using the readlines method to insert each line into a list, then
# return the created list.
def openFile(fileName):
    with open(fileName, 'r') as file:
        contents = file.readlines()
    return contents


def parseMatchups(lineup):
    wrestlers = {}

    # Set the first wrestler to be a Babyface
    team = 'Babyfaces'

    # Get the number of wrestlers at the first index in our list that we made based off of our input file
    numWrestlers = int(lineup[0])

    # Get the number of matchups between different wrestlers at the list index that's one more than the number
    # wrestlers we found in our file
    numMatchups = int(lineup[numWrestlers + 1])

    for i, name in enumerate(lineup[1:numWrestlers + 1]):
        wrestlers[name.rstrip()] = {'team': team,
                                    'distance': 0,
                                    'visited': False,
                                    'adj': []}
        # Don't assign a team yet to any subsequent wrestlers
        team = 'Unassigned'

    # Get each matchup beginning from the list index after we find the total number of matchups, then ending
    # after we've read the number of matchups that were specified in the input file. Add the wresters found
    # on each line to each other's adjacency list.
    for j, rivalry in enumerate(lineup[numWrestlers + 2:(numWrestlers + 2 + numMatchups)]):
        matchup = [wrestler for wrestler in rivalry.split()]
        wrestlers[matchup[0]]['adj'].append(matchup[1])
        wrestlers[matchup[1]]['adj'].append(matchup[0])

    return wrestlers


def bfs(matchups):
    print(matchups)
    babyfaces = []
    heels = []
    queue = []

    for i, nextWrestler in enumerate(matchups):
        if not matchups[nextWrestler]['visited']:
            queue.append(nextWrestler)
            while queue:
                nextWrestler = queue.pop(0)
                matchups[nextWrestler]['distance'] += 1
                matchups[nextWrestler]['visited'] = True
                print(matchups[nextWrestler])

    # for wrestler in matchups:
    #   print(matchups[wrestler]['visited'])
    #    queue = [wrestler]
    #    matchups[wrestler]['visited'] = True
    #    print(matchups[wrestler]['visited'])
    #    #print(len(queue))


if __name__ == "__main__":
    main()
