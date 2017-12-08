import sys

def main():
    filename = sys.argv[1]
    Lines = open(filename).readlines()
    N = Lines[0].strip('\n').split(' ')[0]
    numLinks = Lines[0].strip('\n').split(' ')[1]
    nodeList = Lines[1].strip('\n').split(' ')
    distanceList = []
    for i in range(2, len(Lines)):
        distanceList.append(Lines[i].strip('\n').split(' '))

    print("Number of nodes is: ", N)
    print("Number of links is: ", numLinks)
    print("The node names are: ", nodeList)
    print("The distances between nodes are: ", distanceList)

if __name__=='__main__':
    main()

