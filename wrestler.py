#!/usr/bin/env python3

import sys


# Open the file with the passed name as read only, using the readlines method to insert each line into a list, then
# return the created list.
def openFile(fileName):
    with open(fileName, 'r') as file:
        contents = file.readlines()
    return contents


def parse(lineup):
    print(lineup)
    wrestlers = {}

    # Set the first wrestler to be a Babyface
    team = 'Babyfaces'

    # Get the number of wrestlers at the first index in our list that we made based off of our input file
    numWrestlers = int(lineup[0])

    # Get the number of matchups between different wrestlers at the list index that's one more than the number
    # wrestlers we found in our file
    numMatchups = int(lineup[numWrestlers + 1])

    for i, name in enumerate(lineup[1:numWrestlers + 1]):
        wrestlers[name.rstrip()] = team
        print(wrestlers[name.rstrip()])
        # Don't assign a team yet to any subsequent wrestlers
        team = 'Unassigned'

    print(wrestlers)

    # Get each matchup beginning from the list index after we find the total number of matchups, then ending
    # after we've read the number of matchups that were specified in the input file
    for j, rivalry in enumerate(lineup[numWrestlers + 2:(numWrestlers + 2 + numMatchups)], start=1):
        print('%d %s' % (j, rivalry.rstrip()))
        matchup = [wrestler for wrestler in rivalry.split()]


def main():
    lineup = openFile(sys.argv[1])
    parse(lineup)


if __name__ == "__main__":
    main()
