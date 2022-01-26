# BDO Barter Inventory Bot

A Discord bot created at the peak of my BDO addiction to make managing my bartering inventory a little easier. Converts an inventory screenshot from the game
into a spreadsheet of item names and quantities

This is achieved by computing a difference hash for known items, and comparing it to segmented items from a grid detected in the image. Hamming distance is used as a metric for item similarity. 
![image](https://user-images.githubusercontent.com/24500086/151237609-a9be5f0a-e7f3-4ac3-9fd8-5f88587c0e4c.png)

The bottom of the tile with the quantity is segmented off, then preprocessed.

![image](https://user-images.githubusercontent.com/24500086/151237864-c86d3b87-1e3c-4ea5-8eca-06862c8ea9c6.png)

This is then fed into PyTesseract to identify quantity via OCR.

[Video](https://www.youtube.com/watch?v=Sq-yNccsHu4&t=156s)
