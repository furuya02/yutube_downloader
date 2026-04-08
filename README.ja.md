# yutube_downloader

YouTube動画をMP4形式でダウンロードするコマンドラインツールです。

## 機能

- URLを指定してYouTube動画をダウンロード
- 最高画質でMP4形式に保存
- 保存先ディレクトリの指定が可能

## 必要条件

- Python 3.10 以上
- [ffmpeg](https://ffmpeg.org/)（映像と音声の結合に必要）

## インストール

```bash
git clone https://github.com/furuya02/yutube_downloader.git
cd yutube_downloader
pip install -e .
```

## 使い方

```bash
# 基本的な使い方
yutube_downloader https://www.youtube.com/watch?v=xxxxx

# 保存先ディレクトリを指定
yutube_downloader https://www.youtube.com/watch?v=xxxxx ./videos
```

## 出力

- **ファイル名形式**: `{動画タイトル}.mp4`
- **出力先**: カレントディレクトリ（または指定したディレクトリ）
- **形式**: MP4（最高画質の映像 + 最高音質の音声を結合）

## ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 作者

furuya02
