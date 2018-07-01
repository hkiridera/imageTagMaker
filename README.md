# 概要

イメージにタグをつけるマシーン

# 前提条件

Microsoft Azure Compute Vision APIのキーを取得してください。

# 使い方

python3 computerVision.py "azure compute vision api key" "picture directry"

# 写真を読み込ませるとこんな感じで出力されます。

[読み込ませた画像]
![](./image/DSC_1828.jpg "もみじの写真")

```
"plant_leaves"
"a close up of a tree"
"plant_leaves"
{
    "description": {
        "captions": [
            {
                "confidence": 0.964949981247559,
                "text": "a close up of a tree"
            }
        ],
        "tags": [
            "plant",
            "tree",
            "maple",
            "small",
            "large",
            "lit",
            "sitting",
            "white",
            "close",
            "green",
            "black",
            "red",
            "hanging",
            "table"
        ]
    },
    "requestId": "532a1aed-4ed8-4302-bab9-5523f643ebeb",
    "color": {
        "dominantColorForeground": "Red",
        "accentColor": "2A0802",
        "isBwImg": false,
        "dominantColorBackground": "Red",
        "dominantColors": [
            "Red",
            "Black",
            "Brown"
        ]
    },
    "metadata": {
        "height": 2000,
        "width": 3000,
        "format": "Jpeg"
    },
    "categories": [
        {
            "score": 0.77734375,
            "name": "plant_leaves"
        }
    ]
}

```