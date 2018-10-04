str1="""Python is a widely used high-level programming langauage for \
general-purpose prograaming, created by Guido van Rossum and first released \
in 1991. An interpreted language, Python has a design philosophy which \
emphasizes code readability (notably using whitespace indentation to delimit \
code blocks rather than curly braces or keywords), and a syntax which \
allows programmers to concpets in fewer lines of code than possible \
languages such as C++ or Java. The language provides constructs inteneded \
to enable writing clear programs on both a small scale and a large scale. \
Python featues a dynamic type system and sutomatic memory management and \
supports multiple programming paradgms,including object-oriented, imperative, \
functional programming, and procedural styles. It has a large and \
comprehensive standard library. Python interpreters are available for \
many operating systems, allowing Python code to run on a wide variety of \
systems. CPython , the reference implementation of Python, is opne source \
software and has a community-based development model, as do nearly all of \
its variant implementations. CPython os managed by the non-profit Python \
Software Foundation."""


wordCountTable={}
wordList=str1.split()
for word in wordList:
	wordCountTable[word]=str1.count(word)


values=wordCountTable.values()
values = sorted(values)
values.reverse()
topFive=values[0:5]
printCount=0

'''
sorted() Parameters

sorted() takes two three parameters:

    iterable - sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator 
    reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
    key (Optional) - function that serves as a key for the sort comparison

'''
sred = sorted(wordCountTable.items(), key=lambda value: value[1], reverse=True)

print ("\n\nTop Five words in the given string with their occurrences")
print ("\n\n---------------------------")
print ("word\t\tcount")
print ("---------------------------")

for idx in range(5):
    print (sred[idx][0],"\t\t",sred[idx][1])

print ("\n\n\n" )