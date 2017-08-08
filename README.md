# most-kmers

A program that found all the 6-mers sequences inside the genome of E. coli. It is expected that there will be some very high frequency 6-mers since viral DNA and transposons can be incorperated into the genome.

However, unsure of what the very low 6-mers are or why the line still slopes upward slightly. A future test may include forward and backwards concensus sequences since the transposons could clearly be backwards. Also, since the genome is circular, really a couple more sequences, like only 5, should be added that span the gap.

Altogether though, I'm pretty suprised that the result was that clear. A success!

The final plot is [6-mers.png](6-mers.png), and the main code is [rank-kmers.py](rank-kmers.py).
