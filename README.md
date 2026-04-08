# yutube_downloader

A command-line tool to download YouTube videos as MP4.

[日本語版 README はこちら](README.ja.md)

## Features

- Download YouTube videos by specifying a URL
- Save as MP4 format with best available quality
- Specify custom output directory

## Requirements

- Python 3.10 or higher
- [ffmpeg](https://ffmpeg.org/) (required for merging video and audio streams)

## Installation

```bash
git clone https://github.com/furuya02/yutube_downloader.git
cd yutube_downloader
pip install -e .
```

## Usage

```bash
# Basic usage
yutube_downloader https://www.youtube.com/watch?v=xxxxx

# Specify output directory
yutube_downloader https://www.youtube.com/watch?v=xxxxx ./videos
```

## Output

- **File name format**: `{video_title}.mp4`
- **Output directory**: Current working directory (or specified directory)
- **Format**: MP4 (best video + best audio merged)

## Project Structure

```
yutube_downloader/
├── src/
│   └── yutube_downloader/
│       ├── __init__.py
│       ├── __main__.py          # Entry point
│       ├── cli.py               # CLI interface
│       └── downloader.py        # Download logic
├── .gitignore
├── README.md                    # English documentation
├── README.ja.md                 # Japanese documentation
├── pyproject.toml               # Project configuration
└── LICENSE                      # MIT License
```

## License

MIT License - see [LICENSE](LICENSE) file for details

## Author

furuya02
