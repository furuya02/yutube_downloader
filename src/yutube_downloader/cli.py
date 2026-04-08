"""CLI インターフェース"""

import sys

from yutube_downloader.downloader import download_video


def main() -> None:
    """メイン関数。コマンドライン引数からURLを取得してダウンロードを実行する。"""
    if len(sys.argv) < 2:
        print("使い方: yutube_downloader <YouTube URL> [保存先ディレクトリ]")
        print("例: yutube_downloader https://www.youtube.com/watch?v=xxxxx ./videos")
        sys.exit(1)

    url: str = sys.argv[1]
    output_dir: str = sys.argv[2] if len(sys.argv) >= 3 else "."

    print(f"ダウンロード開始: {url}")
    download_video(url, output_dir)
    print("ダウンロード完了")
