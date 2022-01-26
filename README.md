# BDO Barter Inventory Bot

A Discord bot created at the peak of my BDO addiction to make managing my bartering inventory a little easier. Converts an inventory image similar to this one

![Capture](https://user-images.githubusercontent.com/24500086/151235103-db733a87-5cf8-4ec2-9704-a5c7949d4b14.PNG)

Into a spreadsheet of item names and quantities

![image](https://user-images.githubusercontent.com/24500086/151235320-3f4cd8a9-3085-4a54-bf09-5681c79f0ea2.png)

This is achieved by computing a difference hash for known items, and comparing it to segmented items from a grid detected in the image. The quantity is then read from a preprocessed segement of the item text which is then fed into PyTesseract.

[Video](https://www.youtube.com/watch?v=Sq-yNccsHu4&t=156s)
