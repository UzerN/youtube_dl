import yt_dlp
import os


def show_available_formats(url):
    ydl_opts = {
        'listformats': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])

        mp4_formats = [format for format in formats if format.get('ext') == 'mp4']

        print("Available Formats (Quality - Extension - Format Note):")
        sorted_formats = sorted(mp4_formats, key=lambda x: x.get('height', 9999))
        for idx, format in enumerate(sorted_formats, start=1):
            format_ext = format.get('ext')
            format_res = format.get('resolution', 'N/A')
            format_note = format.get('format_note', 'N/A')
            print(f"{idx}. {format_res} - {format_ext} - Format Note: {format_note}")

        return sorted_formats


def download_with_selected_format(url, format_id, folder_path):
    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


url = input('Enter the URL: ' + '\n')
folder_path = input('Enter the path (leave empty for default): ' + '\n')

default_path = "C:\\Videos\\"

if not folder_path:
    folder_path = default_path

print("Selected path is: " + str(folder_path))
formats = show_available_formats(url)

format_choice = input('Enter the number of the desired format from the list above: ')
format_id = None

try:
    format_choice = int(format_choice)
    if 1 <= format_choice <= len(formats):
        format_id = formats[format_choice - 1].get('format_id')
except ValueError:
    pass

if format_id:
    download_with_selected_format(url, format_id, folder_path)
    print("Video downloaded successfully.")
else:
    print("Invalid format choice. Video download aborted.")
