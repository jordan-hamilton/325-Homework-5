#!/usr/bin/env python3

import sys


def main():
    lineup = openFile(sys.argv[1])
    matchups = parseMatchups(lineup)
    graph = bfs(matchups)
    teams = formTeams(graph)
    printTeams(teams)


# Open the file with the passed name as read only, using the readlines method to insert each line into a list, then
# return the created list.
def openFile(fileName):
    with open(fileName, 'r') as file:
        contents = file.readlines()
    return contents


def parseMatchups(lineup):
    wrestlers = {}

    # Get the number of wrestlers at the first index in our list that we made based off of our input file
    numWrestlers = int(lineup[0])

    # Get the number of matchups between different wrestlers at the list index that's one more than the number
    # wrestlers we found in our file
    numMatchups = int(lineup[numWrestlers + 1])

    for i, name in enumerate(lineup[1:numWrestlers + 1]):
        wrestlers[name.rstrip()] = {'distance': 0,
                                    'visited': False,
                                    'parent': '',
                                    'adj': []}

    # Get each matchup beginning from the list index after we find the total number of matchups, then ending
    # after we've read the number of matchups that were specified in the input file. Add the wrestlers found
    # on each line to each other's adjacency list.
    for j, rivalry in enumerate(lineup[numWrestlers + 2:(numWrestlers + 2 + numMatchups)]):
        matchup = [wrestler for wrestler in rivalry.split()]
        wrestlers[matchup[0]]['adj'].append(matchup[1])
        wrestlers[matchup[1]]['adj'].append(matchup[0])

    return wrestlers


def bfs(matchups):
    queue = []

    # Run BFS by adding a wrestler to the queue if not visited, popping that wrestler off the queue and incrementing
    # the distance to the adjacent wrestlers (those that we found in a matchup), adding each adjacent wrestler to the
    # queue and setting the wrestler we popped off front of the queue as visited by the search.
    for i, currentWrestler in enumerate(matchups):
        if not matchups[currentWrestler]['visited']:
            queue.append(currentWrestler)
            while queue:
                currentWrestler = queue.pop(0)
                for j, adjWrestler in enumerate(matchups[currentWrestler]['adj']):
                    if not matchups[adjWrestler]['visited']:
                        # Sets the distance of each wrestler in an adjacency list to be 1 more than the parent.
                        # This way, all wrestlers at an even distance are Babyfaces since we initialize the
                        # first wrestler in the list as a Babyface since its distance is 0 when visited.
                        matchups[adjWrestler]['distance'] = matchups[currentWrestler]['distance'] + 1
                        matchups[adjWrestler]['parent'] = currentWrestler
                        queue.append(adjWrestler)
                matchups[currentWrestler]['visited'] = True

    return matchups


def formTeams(graph):
    # Confirm that each wrestler with an even distance has an adjacency list with only wrestlers of odd distance
    # and vice versa. Otherwise, the provided lineups are not possible since there is an opponent on an adjacency
    # that would also be on the same team, and we return empty lists.
    babyfaces = []
    heels = []

    possible = True

    for i, wrestler in enumerate(graph):
        if graph[wrestler]['distance'] % 2 == 0:

            for j, adjWrestler in enumerate(graph[wrestler]['adj']):
                if graph[adjWrestler]['distance'] % 2 == 0:
                    possible = False

            babyfaces.append(wrestler)

        elif graph[wrestler]['distance'] % 2 == 1:

            for j, adjWrestler in enumerate(graph[wrestler]['adj']):

                if graph[adjWrestler]['distance'] % 2 == 1:
                    possible = False

            heels.append(wrestler)

    if not possible:
        babyfaces = []
        heels = []

    return babyfaces, heels


def printTeams(teams):
    if len(teams[0]) + len(teams[1]) == 0:
        print('No')
    else:
        print('Yes\nBabyfaces: ', end='')
        for i, name in enumerate(teams[0]):
            print(name + ' ', end='')
        print('\nHeels: ', end='')
        for i, name in enumerate(teams[1]):
            print(name + ' ', end='')
        print('\n', end='')


if __name__ == "__main__":
    main()
