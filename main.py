from ScrapeCryptoBubbles import CryptoBubbles
from BubbleChart import BubbleChart

import requests
import matplotlib.pyplot as plt
import schedule
import time
from PIL import Image, ImageDraw, ImageFont

def main():
    # Get Top 100 coin and sort by hourly performance
    top100_coin = CryptoBubbles(best_of=100) # default and max: 1000
    sorted_top100_coin = top100_coin.sort_data(top100_coin.get_data())
    
    # Get highest 10 coin
    top10 = sorted_top100_coin[:10]

    # Colors for bubbles
    colors = ["#791112", "#A31718", "#DB1F1D", "#ED3922", "#F1601F", "#F57720", "#F3951B", "#FEAF1F", "#FFCF27", "#FCEE29"]

    # Create Bubble Chart
    bubble_chart = BubbleChart(area=[i["performance"]["hour"] for i in top10],
                                bubble_spacing=0.1)

    bubble_chart.collapse()

    fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
    bubble_chart.plot(
        ax, [i["symbol"] for i in top10], colors
    )
    ax.axis("off")
    ax.relim()
    ax.autoscale_view()

    # Save figure as transparent
    plt.savefig("davidd.png", transparent=True, dpi=100)

    # Get template background image
    template = Image.open("./static/template.png")

    # Get Bubble Chart image
    bubble_chart = Image.open("davidd.png")

    draw = ImageDraw.Draw(template)

    # Create custom font
    font = ImageFont.truetype("./static/Betzmann.otf", 38)

    # Add bubble chart to template image
    template.paste(bubble_chart, (-65, 85), bubble_chart)

    # First row y coordinate
    coin_y = 85

    # Add every coin text to template image
    for i in top10:
        symbol = i["symbol"] + "_" + "USDT"
        draw.text((625, coin_y), f'{i["rank"]:<3}) {symbol:<9} {i["performance"]["hour"]}', (255, 255, 255), font=font)
        coin_y += 45

    # Save final image
    template.save("bubbledavidd.png")


    # Read image binary
    with open("bubbledavidd.png", "rb") as f:
        my_file = f.read()

    # Discord Webhook URL
    WEBHOOK_URL = ""
    requests.post(WEBHOOK_URL, files={"files": ("ILoveUDavidd.png.png", my_file)})

    # Console Log message
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(f"[{current_time}] Webhook Created")

    
    # # You can send image using bot 
    # TOKEN = "" # Discord Bot Token
    # CHANNEL_ID = 0 # Discord Channel Id
    # headers = {"Authorization":f"Bot {TOKEN}"}
    # requests.post(f"https://discord.com/api/channels/{CHANNEL_ID}/messages", files={"files": ("ILoveUDavidd.png", my_file)}, headers=headers)

if __name__ == "__main__":
    schedule.every().hour.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)