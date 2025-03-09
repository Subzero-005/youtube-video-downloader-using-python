import os
from pytube import YouTube, exceptions
from time import time
from tkinter import *
from customtkinter import *

# Configure UI appearance
set_appearance_mode("System")  # Options: "System", "Light", "Dark"
set_default_color_theme("blue")


def create_download_folder():
    """Ensure the 'youtube_downloads' folder exists."""
    folder_name = "youtube_downloads"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    return folder_name


def download_video(video_url):
    """Download a YouTube video and display a status popup."""
    if not video_url.strip():
        show_popup("Error", "Please enter a valid YouTube link")
        return

    try:
        start_time = time()
        download_location = create_download_folder()
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(download_location)
        end_time = time()

        show_popup("Download Status", f"Download successful!\nTime taken: {round(end_time - start_time, 3)}s")

    except exceptions.RegexMatchError:
        show_popup("Error", "Invalid YouTube URL! Please enter a correct link.")
    except exceptions.VideoUnavailable:
        show_popup("Error", "This video is unavailable. Please try another link.")
    except Exception as e:
        show_popup("Error", f"An error occurred: {str(e)}")


def show_popup(title, message):
    """Display a popup message."""
    popup = CTk()
    popup.title(title)
    popup.geometry("300x120")
    popup.resizable(False, False)
    popup.grid_rowconfigure((0, 1), weight=1)
    popup.grid_columnconfigure(0, weight=1)

    label = CTkLabel(popup, text=message, wraplength=280)
    label.grid(row=0, column=0, pady=10)
    button = CTkButton(popup, text="OK", command=popup.destroy)
    button.grid(row=1, column=0, pady=10)

    popup.mainloop()


def main():
    """Initialize the YouTube downloader GUI."""
    master = CTk()
    master.title("YouTube Downloader")
    master.geometry("400x180")
    master.resizable(False, False)
    master.grid_rowconfigure((0, 1, 2), weight=1)
    master.grid_columnconfigure((0, 1), weight=1)

    CTkLabel(master, text="Enter YouTube Video URL:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

    entry = CTkEntry(master, width=250)
    entry.grid(row=0, column=1, padx=10, pady=10)

    CTkButton(master, text='Download', command=lambda: download_video(entry.get())).grid(row=1, column=0, columnspan=2, pady=10)

    master.mainloop()


if __name__ == "__main__":
    main()
