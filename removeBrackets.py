
def checkBrackets(text):
    queue = []
    bracketClosingPairs = {"(":")", "{":"}", "[":"]"}
    openBrackets = ["(","{","["]
    
    if(len(text.rstrip().lstrip()) > 0):
        for bracket in text:
            if(len(queue) > 0 and bracketClosingPairs[queue[-1]] == bracket):
                queue.pop(-1)
            else:
                if(bracket in openBrackets):
                    queue.append(bracket)
                else:
                    return False

    return len(queue) == 0

test1 = "{[(())]}" #print True
test2 = "{[(()]}"  #print False
test3 = ""         #print True

print(checkBrackets(test3))