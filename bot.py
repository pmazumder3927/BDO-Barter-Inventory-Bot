# bot.py
import os
import discord
from discord.utils import get
from discord.ext import commands
import cv2
import numpy as np
from urllib.request import Request, urlopen
import asyncio
import swt
import pytesseract
import grip
import xlsxwriter
import scipy.ndimage as ndi
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

last_seen = "Wednesday, 20-May-20 08:25:22 UTC"

bot = commands.Bot('-')
Barter_items = {
    'Mysterious Rock': 5995724383175971840,
    'Luxury Patterned Fabric': 2456512991978323968,
    'Elixir of Youth': 2024449714325817344,
    'Portrait of the Ancient': 7659015971164801024,
    '102 Year Old Golden Herb': 7720690760415594496,
    'Golden Fish Scale': 1525404326419170048,
    'Taxidermied White Caterpillar': 3475115467251786752,
    'Faded Gold Dragon Figurine': 1451888896718965760,
    'Supreme Gold Candlestick': 1593717975570845184,
    'Statue\'s Tear': 506390040723981888,
    'Taxidermied Morpho Butterfly': 3680341882816430080,
    'Azure Quartz': 6562649723444887552,
    '37 Year Old Herbal Wine': 1669521912011894272,
    'Octagonal Box': 7159506913900888064,
    'Pirate\'s Key': 290570618738339840,
    'Bronze Candlestick': 6058507032813111296,
    'Headless Dragon Figurine': 3713530201499041792,
    'Panacea': 798024470245082624,
    'Seashell Deco': 2242580680296438016,
    'Old Chest with Gold Coins': 9756845558175248384,
    'Boatman\'s Manual': 6497129820895117312,
    'Green Salt Lump': 1057939325159476224,
    'Solidified Lava': 432645741538739200,
    'Marine Knights\' Spear': 1589223241564446464,
    'Amethyst Fragment': 12008305292847099904,
    'Opulent Thread Spool': 5045868924189085696,
    'Stolen Pirate Dagger': 2606555113040379904,
    'Marine Knights\' Helm': 1012798733798475264,
    'Blue Candle Bundle': 11181598947388948480,
    'Ancient Orders': 1672861956543222784,
    'Lopters Fishnet': 10248064279284588544,
    'Rare Herb Pile': 11112180546716633088,
    'Skull Symbol Carpet': 11316788705819115520,
    'Weasel Leather Coat': 1699710948506736128,
    'Gooey Monster Blood': 6059043663475904512,
    'Round Knife': 884114014563862016,
    'Skull Decorated Teacup': 3619119097915117568,
    'Stalactite Fragment': 10614191737373067264,
    'Scout Binoculars': 3029570486336487424,
    'Pirates\' Supply Box': 1668354161555472384,
    'Torn Pirate Treasure Map': 2456174965117288960,
    'Old Hourglass': 3174487998730114560,
    'Urchin Spine': 14993231120859146240,
    'Pirate Gold Coin': 2968830289415900160,
    'Monster Tentacle': 3201034969657905152,
    'Sea Survival Kit': 4416658078293164544,
    'Balanced Stone Pagoda': 4483364301746866176,
    'Narvo Sea Cucumber': 10532038577775509504,
    'Big Stone Slab': 5146236785488822272,
    'Supreme Oyster Box': 8056853513559817216,
    'Conch Shell Ornament': 1082839797845466112,
    'Filtered Drinking Water': 1021803975488179712,
    'Opulent Marble': 310241718901345280,
    'Pirate Ship Mast': 9560731524549124096,
    'Cron Castle Gold Coin': 8454709140958616576,
    'Islanders\' Lunchbox': 10624865730287370240,
    'Pirates\' Gunpowder': 7181731969699422208,
    'Fertile Soil': 14782847296471830528,
    'Rakeflower Seed Pouch': 7446529581376998400,
    'Roa Flower Seed Pouch': 7446533996064410624,
    'Golden Sand': 794611620512730880,
    'Cherry Tree Seed Pouch': 7446529460646120448,
    'Unidentified Ancient Mural': 221524240615575328,
    'Ancient Urn Piece': 221524240615575328,
    'Chewy Raw Gizzard': 15445955149497974784,
    'Raft Toy': 10306304610395062272,
    'Stained Seagull Figurine': 1102552903014613760,
    'Naval Ration': 1398760455056721664,
    'Giant Fish Bone': 5673881866206470144,
    'Dried Blue Rose': 587531843016397824,
    'Empty Slot': 2305843009213759488,
    'Locked Slot': 1446805655582146560
}
"""

Barter_items = {
    'Mysterious Rock': 304280304756939280,
    'Luxury Patterned Fabric': 4020981308162637828,
    'Monster Tentacle': 440638821744793664,
    'Sea Survival Kit': 15862779264567040,
    'Balanced Stone Pagoda': 5638062729884101632,
    'Narvo Sea Cucumber': 13848655248793077760,
    'Big Stone Slab': 9278914241251057664,
    'Supreme Oyster Box': 1894726162284877568,
    'Conch Shell Ornament': 9561459828015710208,
    'Filtered Drinking Water': 904773890030243328,
    'Opulent Marble': 310241718901345280,
    'Pirate Ship Mast': 4778730029446668288,
    'Cron Castle Gold Coin': 3483338002961995264,
    'Islanders\' Lunchbox': 12178689491750748160,
    'Pirates\' Gunpowder': 680142779842494848,
    'Fertile Soil': 15126566167479275520,
    'Rakeflower Seed Pouch': 5670396312448879616,
    'Roa Flower Seed Pouch': 15902592259094431744,
    'Golden Sand': 4622737257161232384,
    'Cherry Tree Seed Pouch': 6643191424952257536,
    'Unidentified Ancient Mural': 7509513866339223552,
    'Ancient Urn Piece': 4634290375572473856,
    'Chewy Raw Gizzard': 11430071885196120064,
    'Raft Toy': 10504252135968768,
    'Stained Seagull Figurine': 14782041092372430848,
    'Naval Ration': 3199050055171542016,
    'Giant Fish Bone': 2766706907898823680,
    'Dried Blue Rose': 587531843016397824,
    'Empty Slot' : 2305843009213759488
}
"""


def hamming(a, b):
    # compute and return the Hamming distance between the integers
    return bin(int(a) ^ int(b)).count("1")


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'})
    resp = urlopen(req).read()
    image = np.asarray(bytearray(resp), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image


@bot.event
async def on_ready():
    for guild in bot.guilds:
        break
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'(id: {guild.id})'
    )
    print(discord.opus.is_loaded())


def pairs_range(limit1, limit2):
    """Produce all pairs in (0..`limit1`-1, 0..`limit2`-1)"""
    for i1 in range(limit1):
        for i2 in range(limit2):
            yield i1, i2


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if '!inventory' in message.content.lower():
        try:
            url = str(message.attachments[0].url)
            img = url_to_image(url)
            template = cv2.imread('./images/feature.png', cv2.IMREAD_GRAYSCALE)
            print(template.shape)
            res = cv2.matchTemplate(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), template, cv2.TM_CCOEFF_NORMED)
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
            items = {}
            workbook = xlsxwriter.Workbook('Inventory.xlsx')
            worksheet1 = workbook.add_worksheet()
            p = grip.GripPipeline()

            for i, b in enumerate(Barter_items):
                worksheet1.write(i, 0, b)

            for x, y in pairs_range(10, 9):
                init = (maxLoc[0] + y * 51 + 8, maxLoc[1] + x * 51 + 46)
                final = (init[0] + 46, init[1] + 46)
                cropped = img[init[1]:final[1], init[0]:final[0]]
                no_text = cv2.cvtColor(cropped[0:27, 0:46], cv2.COLOR_BGR2GRAY)
                text = cropped[28:43, 14:43]
                p.process(text)
                thresh = p.hsv_threshold_output
                stencil = np.zeros(thresh.shape).astype(thresh.dtype)
                contours = p.filter_contours_output
                color = [255, 255, 255]
                cv2.fillPoly(stencil, contours, color)
                processed = cv2.bitwise_and(thresh, stencil)
                processed = cv2.bitwise_not(processed)
                quantity = pytesseract.image_to_string(processed, lang='eng',
                                                       config='--psm 7 -c tessedit_char_whitelist=0912345678')
                if quantity == "":
                    quantity = "1"
                item_key = dhash(no_text)
                item_key = convert_hash(item_key)
                item, dist = recognize_item(item_key)
                if item == 'Empty Slot' or item == 'Locked Slot':
                    break
                #cv2.imwrite('item.jpg', cropped)
                #cv2.imwrite('item_processed.jpg', no_text)
                #cv2.imwrite('item_quantity{}.jpg'.format(quantity), processed)
                #cv2.imwrite('item_quantity{}unprocessed.jpg'.format(quantity), text)
                #await message.channel.send("suspected quantity: {}, \n hash: {}\n suspected item: {} with dist of {}".format(quantity, item_key, item, dist),
                #                          files=[discord.File('item.jpg'), discord.File('item_quantity{}unprocessed.jpg'.format(quantity))])
                items[item] = items.get(item, 0) + int(quantity)
                worksheet1.write(list(Barter_items.keys()).index(item), 1, items[item])
            print(items)
            workbook.close()
            await message.channel.send("Inventory Sheet:", file=discord.File("Inventory.xlsx"))
        except IndexError:
            await message.channel.send("you forgot the image")
    elif 'andrew' in message.content.lower():
        await message.channel.send("politically correct")
    if 'johann' in message.content.lower():
        await message.channel.send("specimen last seen {}".format(last_seen))
    if 'wubby' in message.content.lower():
        await message.channel.send("**THE YIFFENING HAS BEGUN**")
    await bot.process_commands(message)


def dhash(image, hashSize=8):
    # resize the input image, adding a single column (width) so we
    # can compute the horizontal gradient
    resized = cv2.resize(image, (hashSize + 1, hashSize))
    # compute the (relative) horizontal gradient between adjacent
    # column pixels
    diff = resized[:, 1:] > resized[:, :-1]
    # convert the difference image to a hash
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])


def process(im):
    im = np.flip(im[:, :, :3], 2)  # turn bgra to rgb
    height, width, channel = im.shape
    img = cv2.resize(im, (3 * width, 3 * height), interpolation=cv2.INTER_LINEAR)
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    gaussian_3 = cv2.GaussianBlur(img, (9, 9), 10.0)
    img = cv2.addWeighted(img, 1.5, gaussian_3, -0.5, 0, img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale

    gray = cv2.medianBlur(gray, 3)
    return gray


def postprocess(im):
    gray = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    gray = cv2.medianBlur(gray, 3)
    return gray


def convert_hash(h):
    # convert the hash to NumPy's 64-bit float and then back to
    # Python's built in int
    return int(np.array(h, dtype="float64"))


def recognize_item(item_key):
    lowest = 100
    for b in Barter_items:
        dist = hamming(item_key, Barter_items[b])
        if dist < lowest:
            lowest = dist
            suspected_item = b

    return suspected_item, lowest


def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()


@bot.command(pass_context=True, aliases=['l', 'leav'])
async def leave(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('not in a channel')

bot.run('token')