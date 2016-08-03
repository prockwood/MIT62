def functionWithDefaults(thing1, thing2= "fancy feast", thing3 = False):
    if (thing1):
        print "oly owen doesn't show em"
    else:
        print "too much!"
    print "thing2: ", str(thing2)

    if(thing3):
        thing = "thingy is here"
    else:
        thing = "not a ma-jig"

    print thing

def main():
    functionWithDefaults("apple", thing2 = True)

if __name__ == '__main__':
    main()
# oly owen doesn't show em
# thing2:  True
# not a ma-jig
