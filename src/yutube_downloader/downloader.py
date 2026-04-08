"""YouTube動画ダウンロード処理"""

import yt_dlp


def download_video(url: str, output_dir: str = ".") -> None:
    """指定されたURLのYouTube動画をMP4形式でダウンロードする。

    Args:
        url: YouTubeの動画URL
        output_dir: 保存先ディレクトリ（デフォルト: カレントディレクトリ）
    """
    ydl_opts: dict = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
