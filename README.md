Finding optimal investment
==========================
A simple calculator to find the maximum return on investment from
historical price movements.

Requires Python 2.6

Goal
====
Given an input list of price movements, provide the optimal dates to
buy and sell to maximise the return on investment.


Running
=======
The main program "find_optimal_return.py" can be run via Python, or
(on Unix/Linux/OSX) can be run directly like so:

    % ./find_optimal_return.py

It reads the file "prices.txt" and writes to the file "output.txt",
both in the current working directory.


Running tests
=============
The unit tests in t_return_optimiser.py can be run like so:

    % python t_return_optimiser.py


Performance and implementation
==============================
Algorithmically, this program performs in linear time using constant
memory. It accesses the file prices.txt in a linear sequence. Internally,
it uses generators to avoid storing data.

It is implemented using some high level Python features such as
regular expressions which would provide some low hanging fruit for
further optimisation, but I would want to do some profiling with
representative data first.

I have avoided putting all the logic into a class for its own sake; I
use a class (return_optimiser.BestReturn) simply as a data structure.


Bugs and assumptions
====================
In the event of no available profit (because of no uptick in the
data), both the low and high dates written will be the start date,
and the profit will be shown as "0.0".

The program does no explicit input validation. Python will perform
some (e.g. it will throw an exception if the input file does not
exist, or if the movement is not convertible to float), but this
may not be sufficient (it depends on the reliability of whatever
generates prices.txt, for instance).

I have deliberately not validated dates; I assume that the generator
of prices.txt generates correct format dates. This program has no
concept of a date and just treats the 2nd column of prices.txt as a
string. The big benefit here is the program is resilient in the face
of a date format change (e.g. changing to a 4 digit year).

The output writes the profit field with only a single decimal place.
This minimises some issues with precision lost due to use of floating
point maths (e.g. 10% cannot be faithfully represented in binary
floating point).

Not a bug: the single division in the program will never divide by zero
because the only situation where that could happen is if the low price
is 0, caused by a -100% movement, and in that case no subsequent
upticks will cause a high price (and trigger the division) because
movement is expressed as a factor of price, and 0*x=0.

Further investment optimisation
===============================
As it stands, the optimiser misses the case where there is more than
one equivalent return but with a narrower date range. This may or may
not be a worthwhile optimisation, depending on other investment
opportunities and inflation etc., but all things being equal it would
make sense to invest for the shortest period.
