def countLines():
    readm=open("README.md","r")
    lines=readm.readlines()
    readm.close()
    return len(lines)

def printtoHTML():
    lcount=open("numlines.html","w")
    numlines=countLines()
    head=f'''
<!doctype html>
    <html lang="en">
    <head>
        <title>Number of Lines</title>
    </head>
    <body>
        <h2>Number of lines in README.md is {numlines}</h2>
    </body>
</html>
    '''
    lcount.write(head)
    return

if __name__ == "__main__":
    printtoHTML()