import tweepy
import os
from datetime import datetime
from PIL import Image, ImageDraw

# Twitter API credentials
bearer_key = 'AAAAAAAAAAAAAAAAAAAAANa%2FsAEAAAAA4supkIJjGyNRn6w50OPcTDcGT5g%3Dm8kbW0q8suYbNXBL0pdVq5YG44fXWvpL8JS6SBtYviEM56yWeM'
consumer_key = 'i9YBCusdiPaMgtAEk2pyG5JFJ'
consumer_secret = 'RgGZyoxX54UDgdVCYsX6SVXqSa5sSQ7YLhVt6b7imURvgX8tyH'
access_token = '1619200056212729856-gOObcvjN79yVbhZqDosQNEHXcXqNW7'
access_token_secret = '5PpbLjblweIpixNTUM0BVUfb2gMMGszbqYZqjQu5QV1UE'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(
    bearer_key,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)
def calculate_year_progress():
    now = datetime.now()
    year_start = datetime(now.year, 1, 1)
    year_end = datetime(2024, 4, 9)  # April 8, 2024 is counted as a day
    total_days = (year_end - year_start).days
    days_passed = (now - year_start).days
    progress_percentage = (days_passed / total_days) * 100
    return progress_percentage

# Function to generate progress bar image
def generate_progress_bar(progress):
    # Define image dimensions
    width = 400
    height = 50
    
    # Create a new image with white background
    img = Image.new('RGB', (width, height), color = 'white')
    draw = ImageDraw.Draw(img)

    # Calculate progress bar width
    progress_width = int(width * (progress / 100))

    # Draw progress bar
    draw.rectangle([0, 0, progress_width, height], fill='blue')

    # Save the image to the specified folder
    img.save('progress_bar.png')

# Main function to tweet the progress
def tweet_year_progress():
    progress = calculate_year_progress()
    status_text = f"Year Progress: {progress:.2f}%\nHappy Birthday Allu Arjun! 🎉🎂"

    # Generate progress bar image
    generate_progress_bar(progress)

    # Upload the progress bar image and tweet
    media = api.media_upload('progress_bar.png')
    api.update_status(status_text, media_ids=[media.media_id])
    print("Tweeted:", status_text)

if __name__ == "__main__":
    tweet_year_progress()
