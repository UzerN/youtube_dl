# youtube_dl
This is a Python script that allows users to download YouTube videos by providing the video URL and choosing the desired format from a list of available formats. The script utilizes the yt_dlp library, an improved version of youtube-dl, to fetch the available formats and perform the downloads.

Features:

1. Choose Video Format: The script presents a list of available video formats for the given YouTube URL, including information about the video quality, file extension, and any additional format notes.
2. Filter by MP4 Format: Users can select a video format from the list, and the script ensures that only formats with the mp4 file extension are displayed, allowing for easy selection of the preferred format.
3. Optional Format Note Filter: The script offers an optional input for users to specify a desired format note. It displays only the formats that match the provided note, helping users narrow down their choices based on specific requirements.
4. Custom Download Path: Users can specify a custom download path or leave it empty to use the default location (C:\Videos\).

Usage:
Run the script in a Python environment.
Enter the YouTube video URL when prompted.
Optionally, enter the desired format note to filter the available formats. If not required, leave the input empty.
Choose the desired format number from the displayed list.
If you provided a custom download path, the video will be downloaded to the specified location; otherwise, it will be saved in the default folder (C:\Videos\).


Requirements:
Python 3.x
yt_dlp library (install using pip install yt-dlp)
Please make sure to have the required Python version and install the yt_dlp library before using the script. The script provides an easy way to download YouTube videos in various formats, making it a convenient tool for users who need to save videos for offline viewing or other purposes.
