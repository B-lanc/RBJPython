# RBJPython
Implementations of Robert Bristow-Johnson filters for learning purposes

From reading eq cookbook by robert bristow-johnson
honestly I still don't understand how any of these work, and how to get the coefficients, my maths are just not good enough for this yet. However, I'll try to implement it anyway :p.


I'm not testing it automatically, but manually null testing it with reaEQ (tho the BW parameter is a pain)
needs ./audio/testaudio.wav 
To run the tests, just edit the files in ./tests/ and run it from project root directory


Everything is tested and very closely nulls to reaper
one thing that's interesting is that the bandwidth (BW) parameter doesn't match 1 to 1 with reaEQ's parameter number
setting it to 1 is close to around 0.4 in reaper (hard to null because distortion as my testing audio is close to full scale), 4 here nulls with setting it to 1.74 (octaves) in reaper.
I'm not sure what is the unit in this algorithm, but it works.
