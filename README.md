# algorithm4
MY NOTES FOR ALGORITHMIC 4

I used python2 and python3 in this module.
Although python3 has better performance (as i realised in previous module)
the use of python3 in this has the effect of creating byte objects when 
reading internet files. For example the string of protein of fruitfly has 
the form b'SLAJFAOLJKALEJLJLKBJWOIEUR', where the starting b implies the byte class.
Things were more tricky when reading the pax score, where each value in the dictionary
was byte. To convert a byte object back to string just use mybyteobject.decode()
Keep in mind that the project.py is the same either in python2, or python3.
