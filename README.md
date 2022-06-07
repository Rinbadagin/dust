# DUST was a simple framework made for visualising noise generation but eventually just became a way to make cool (I think) images.
It utilises the PyPi module pyfastnoisesimd, the Python Imaging Library (PIL), numpy, and various other builtin modules that come with python 3.

# To run:
1. Clone this repository 
2. Install the pip modules "pyfastnoisesimd" and "PIL" (of course a virtual environment can be used), and
3. Run demo_main.py with a recent version of python 3 (`$ python3 demo_main.py`)

# To fiddle:
If you're looking to mess around with this I'm afraid you'll have to look at the source. I haven't made any proper documentation.
There will be comments, but I give no guarantee that they will be up-to-date or even relevant at all so expect to delve into the source ;)
To get started it is good to know that the provided demo_main.py should work out of the box - if it doesn't your environment might be incorrectly configured.

# Sample Images
The LandFilter is currently the only filter used in this section and the conditions used to generate each respective image are lost to time :)
![Sample image 1 (RAW)](demo_images/demo-1-raw.png "Raw Image 1")
![Sample image 1 (Land Filtered)](demo_images/demo-1-filtered.png "Filtered Image 1")
![Sample image 2 (RAW)](demo_images/demo-2-raw.png "Raw Image 2")
![Sample image 2 (Land Filtered)](demo_images/demo-2-filtered.png "Filtered Image 2")
