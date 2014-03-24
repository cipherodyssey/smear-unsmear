smear-unsmear
=============

Python script to do smearing/unsmearing crypthography
__________________

Example of how to run the script (assuming you are working in the same directory where your script(crypto.py) is saved):

1. >python
2. >>>import crypto
3. >>>new = crypto.Crypto(128,"attackatdawn")
4. >>>new.smear()
output : acktnwdatata
6. >>>new.unsmear(128,"acktnwdatata") 
output : attackatdawn

And that is it! Enjoy!

