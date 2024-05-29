#!/bin/bash

# 対象ディレクトリ
DIRECTORY="./"

# ディレクトリ内のすべてのファイルを取得し、リネーム
i=1
for file in "$DIRECTORY"/*; do
  if [ -f "$file" ]; then
    # ファイル名のベース部分と拡張子を取得
    filename=$(basename -- "$file")
    extension="${filename##*.}"
    basename="${filename%.*}"
    
    # ファイル名のベース部分が数字かどうかをチェック
    if [[ "$basename" =~ ^[0-9]+$ ]]; then
      # 新しいファイル名を生成（4桁の0埋め）
      new_filename=$(printf "%04d.%s" "$basename" "$extension")
      new_filename=$(printf "%04d.%s" "$basename" "$extension")
      echo "New filename: $new_filename"

      
      # 古いファイルパスと新しいファイルパス
      old_filepath="$file"
      new_filepath="$DIRECTORY/$new_filename"
      
      # ファイルをリネーム
      mv "$old_filepath" "$new_filepath"
      echo "Renamed $old_filepath to $new_filepath"
    fi
  fi
done
