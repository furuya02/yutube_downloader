# yutube_downloader

YouTube動画をMP4形式でダウンロードするコマンドラインツール

## 概要

`yutube_downloader`は、URLを指定してYouTube動画をMP4ファイルとしてダウンロードします。プレーヤー互換性を最大化するためH.264（avc1）コーデックを優先し、ffmpegを使用して映像と音声を自動的に結合します。

## 機能

- URLを指定してYouTube動画をダウンロード
- MP4形式で保存（H.264映像 + AAC音声）
- 最大1080p解像度
- 保存先ディレクトリの指定が可能
- プレイリストURLでも単一動画のみダウンロード

## インストール

```bash
git clone https://github.com/furuya02/yutube_downloader.git
cd yutube_downloader
pip install -e .
```

pipでインストール後、`yutube_downloader`コマンドがグローバルに使用可能になります：

```bash
yutube_downloader
```

## 必要条件

- Python 3.10 以上
- [ffmpeg](https://ffmpeg.org/)（映像と音声の結合に必要）

## 使用方法

### 基本的な使い方

```bash
yutube_downloader "https://www.youtube.com/watch?v=xxxxx"
```

### 保存先ディレクトリを指定

```bash
yutube_downloader "https://www.youtube.com/watch?v=xxxxx" ./videos
```

> **注意**: URLは必ずダブルクォートで囲んでください。YouTubeのURLには`&`文字が含まれることが多く、シェルに解釈されてしまいます。

### 使用例

**単一動画をダウンロード：**

```bash
yutube_downloader "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

**プレイリストURLから（指定された動画のみダウンロード）：**

```bash
yutube_downloader "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf"
```

## 動作の仕組み

1. コマンドライン引数からYouTube URLを解析
2. yt-dlpを使用して動画のメタデータを取得
3. 最適なH.264映像ストリーム（最大1080p）とAAC音声ストリームを選択
4. 映像と音声を個別にダウンロード
5. ffmpegを使用して単一のMP4ファイルに結合
6. 一時ファイルを削除

## 出力

- **ファイル名形式**: `{動画タイトル}.mp4`
- **出力先**: カレントディレクトリ（または指定したディレクトリ）
- **形式**: MP4（H.264映像 + AAC音声）

## ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。

## コントリビューション

コントリビューションは歓迎します！お気軽にPull Requestを送ってください。
