# yutube_downloader

A command-line tool to download YouTube videos as MP4.

[日本語版 README はこちら](README.ja.md)

## Overview

`yutube_downloader` downloads a YouTube video as an MP4 file by specifying its URL. It prioritizes H.264 (avc1) codec for maximum player compatibility and automatically merges the best available video and audio streams using ffmpeg.

## Features

- Download YouTube videos by specifying a URL
- Save as MP4 format (H.264 video + AAC audio)
- Up to 1080p resolution
- Specify custom output directory
- Playlist URLs are handled as single video downloads

## Installation

```bash
git clone https://github.com/furuya02/yutube_downloader.git
cd yutube_downloader
pip install -e .
```

After installing with pip, the `yutube_downloader` command will be available globally:

```bash
yutube_downloader
```

## Requirements

- Python 3.10 or higher
- [ffmpeg](https://ffmpeg.org/) (required for merging video and audio streams)

## Usage

### Basic usage

```bash
yutube_downloader "https://www.youtube.com/watch?v=xxxxx"
```

### Specify output directory

```bash
yutube_downloader "https://www.youtube.com/watch?v=xxxxx" ./videos
```

> **Note**: Always quote the URL with double quotes. YouTube URLs often contain `&` characters which are interpreted by the shell.

### Examples

**Download a single video:**

```bash
yutube_downloader "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**Download from a playlist URL (only the specified video is downloaded):**

```bash
yutube_downloader "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf"
```

## How it works

1. Parses the YouTube URL from command-line arguments
2. Extracts video metadata using yt-dlp
3. Selects the best H.264 video stream (up to 1080p) and AAC audio stream
4. Downloads both streams separately
5. Merges video and audio into a single MP4 file using ffmpeg
6. Cleans up temporary files

## Output

- **File name format**: `{video_title}.mp4`
- **Output directory**: Current working directory (or specified directory)
- **Format**: MP4 (H.264 video + AAC audio)

## Requirements

- Python 3.10 or higher
- [ffmpeg](https://ffmpeg.org/)

## License

MIT License - see [LICENSE](LICENSE) file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
