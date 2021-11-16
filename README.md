# DikPix generation script
# Intro
This project was forked from the original BitBirds project by nft-fun. This is the original intro

> This is published under MIT license, which means you can do whatever you want with it - entirely at your own risk.
> 
> Please don't be an asshole. This is, like, grassroots and stuff. 
> 
> Specifically I'm asking you in good faith not to directly knock off the BitBirds project, or otherwise screw me over for sharing this. Do not use this > for anything hateful or discriminatory.
> 
> There is a YouTube video walkthrough to complement this ReadMe [...Link...](https://youtu.be/vTxjLLHncMo).

# Setting the expectations
If you're new to programming you may struggle to set up the dependencies. If you're persistent, you can do it! I believe in you. 

Often in technology, setting up a pre-requisite like PIP (a python asset installation tool) isn't something the developer thinks about in a given project because it has been on their computer for months or years. 

Even having set up a number of dependencies just a few weeks ago for this project, I don't remember exactly how I worked through the various error messages. When you try to run the script, if it fails there will often be some useful nugget of information buried in the cryptic response blob. As a rule for life - Google is your friend, and others have probably encountered your exact error message. When asking questions on discord, stackoverflow, or wherever, say very specifically (1) what you've tried (2) what you expect as the result and (3) what issue/error you're encountering. That'll get a lot more useful feedback than just shouting HALP.

# Dependencies
The dependenices were all installed with the terminal/command line. There is documentation abound about terminal generally, and these tools specifically, but unfortunately I did not save copies of the web pages I used. From memory the things I needed to setup were:

- Python 3 (default on my mac was python 2.7)

- PIP - a command-line installation mechanism for python assets. 

IIRC I needed to use some special command with python 3 to use pip as an installation mechanism for the items below- perhaps `pip3 install ...` rather than `pip install ...`?

- Pillow - python library to generate images - installed via terminal/command-line with PIP

- NumPy - python library to work with arrays - installed via terminal/command-line with PIP

- I don't *think* I had to install the 'random' library (included in the script) to use the number-randomization feature, but might have.

If you encounter specific setup items I haven't mentioned here let me know, and I'll add them.

# How this script works
The [video](https://youtu.be/vTxjLLHncMo) from BitBirds on YouTube complements this overview. 

We are iterating through a 'loop' once for each dik. The loop starts with a 'seed number' that is used to deterministically generate pseudo-random numbers. I say 'deterministically' and 'pseudo-random' because from the same seed number the 'random' output will always be the same. It's not truly random in a security or mathematical sense. I used the most recent ETH block at the time as my seed number - 11981207.

There is then a 'chain' of additional random numbers generated that are used to define all of the various traits of the dik. Many of the attributes generate a random number between 1-1000 and use that for some sort of logical statement (e.g. to decide skin color). 

- Skin color (hd) is a random 1-5 number to generate 5 different skin colors
- Eye color looks at a random number between 1-1000 and if it's 47 or less, will give the bird crazy eyes. Crazy eyes always have a random pupil color and then generate a same color (240,248,255) for the 'white of the eye,' in the same way the head and throat color are generated.
- Lips color (bk) is determined by an evaluation of another 1-1000 'random' number. Light pink and pink are most common, darker pink is the least common

The final images are 50x50 arrays of variables split into head(17x50), shaft(10x50) and balls(23x50); representing every pixel in the final image. I've used variables with two letters for each type of pixel (e.g. outline `ol`, skin `hd, lips `bk`), so as to keep the 'matrix' of pixel variables easy to see and work with. If you zoom way out on the code you may even be able to see a rough picture of the diks and accesories in the code, just from the slight differences in the variables.

The script uses another 1-1000 'random' number to decide which of the dik type templates to use. It combines a head, shaft and balls array at random. A head array may have a hat accessory, the shaft array may have an eyewear accessory and the balls may contain facial hair or a joint in the mouth.

From there, you're just about home free. The final bit of the loop re-sizes the generated bird from 50x50 pixels up to 120x120 pixels. It generates the image file path (dynamically, wherever you have the folder using the `os` library), and saves the image into the included folder `bird_images`.

Then it goes right back to the top of the loop, and does it again for the next bird, until the number of defined loops is completed. 

# Wrap up
I am hoping this project will amuse people enough for them to run the code and learn from it. I have been in the  crypto space for less than 1 year so I am still learning. For me this project has helped me understand the potential of the Ethereum blockchain and how it could disrupt many different industries.

A portion of any proceeds to go to prostate cancer charities to help raise awareness and encourage men to get tested. https://prostatecanceruk.org/get-involved/donate

If you feel compelled to send ETH or NFTs to Bitbirds or DikPix directly, please know that it is not necessary,
- the BitBirds project hardware wallet address is: 0x1fd146a5e6152c5ACd3A013fBC42A243e4DfCe63
- the DikPix project hardware wallet address is: 0x3844aaaf3c139acf89de2316ffff9763a830a95f

Thanks to Bitbirds and the rest of the NFT community to inspire me to learn more about NFTs and Crypto!
