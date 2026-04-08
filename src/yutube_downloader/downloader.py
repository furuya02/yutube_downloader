"""YouTube動画ダウンロード処理"""

import os
import shutil

import yt_dlp


def _find_ffmpeg_dir() -> str | None:
    """ffmpegが存在するディレクトリのパスを返す。"""
    path: str | None = shutil.which("ffmpeg")
    if path:
        return os.path.dirname(path)
    for candidate in ["/Applications/ffmpeg", "/usr/local/bin/ffmpeg", "/opt/homebrew/bin/ffmpeg"]:
        if os.path.isfile(candidate):
            return os.path.dirname(candidate)
    return None


def download_video(url: str, output_dir: str = ".") -> None:
    """指定されたURLのYouTube動画をMP4形式でダウンロードする。

    Args:
        url: YouTubeの動画URL
        output_dir: 保存先ディレクトリ（デフォルト: カレントディレクトリ）
    """
    ydl_opts: dict = {
        "format": "137+140/136+140/135+140/134+140/18/best[ext=mp4]/best",
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "noplaylist": True,
    }

    ffmpeg_dir: str | None = _find_ffmpeg_dir()
    if ffmpeg_dir:
        ydl_opts["ffmpeg_location"] = ffmpeg_dir

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
