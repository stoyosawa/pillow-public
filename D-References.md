## 付録D 参考文献

本書に関連する参考文献を示します。

### D.1 URLs

● [Pythonメインページ](https://www.python.org/ "LINK")（英）ーダウンロードやドキュメントへのアクセスはこちらから。

```https://www.python.org/```

● [Pythonドキュメント](https://docs.python.org/ja/ "LINK")（和）ー初学時はまず［チュートリアル］、慣れてきたら［ライブラリーリファレンス］を参照します。

```https://docs.python.org/ja/```

● [Pillowメインページ](https://pillow.readthedocs.io/ "LINK") (英）ー左パネルのReferenceから、モジュール単位で並べられたリファレンスマニュアルにアクセスできます。画像ファイルフォーマットや文字列アンカーなど付随的な情報はHandbook 》 ConceptsまたはHandbook 》 Appendicesにあります。チュートリアルはHandbook 》 Tutorialです。

```https://pillow.readthedocs.io```

● [Pillowソース](https://github.com/python-pillow/Pillow "LINK")（英）－マニュアルの記述が不足なら、ソースから確認することも必要になります。

```https://github.com/python-pillow/Pillow```

● [Numpyリファレンス](https://numpy.org/doc/stable/reference/index.html "LINK")（英）ーメインページからだとDocumentation 》 API Rerferenceです。機能が膨大すぎて迷いますが、本書の範囲内ならArray Objects（行列オブジェクト）の個所だけでおなががいっぱいになります。もっとも、初学のうちはGogoleでやりたいことを検索した方が早いです。

```https://numpy.org/doc/stable/reference/index.html```

● [tkリファレンス](https://tkdocs.com/shipman/ "LINK")（英）－tkinterの情報は[Pythonの公式リファレンス](https://docs.python.org/ja/3/library/tk.html "INTERNAL")にも記載されていますが、リファレンスマニュアルならこちらの方が構造立っており、（慣れてきたら）読みやすいと思います。ただし、2013年以来更新はされていません。それだけ安定したライブラリとも言えます。

```https://tkdocs.com/shipman/```

● [OpenCVドキュメント](https://docs.opencv.org/ "LINK")（英）ー［Doxygen HTML］の下にバージョン単位で並んでいます。ドキュメントはモジュール単位（core、imgprocなど）に分けられていて、慣れないと思ったものがなかなか見つかりません。特定の関数について知りたいのなら、ページ右上にあるSearchフィールドに入れればたいてい見つかります。

```https://docs.opencv.org/```

● [matplotlibドキュメント](https://matplotlib.org/stable/index.html "LINK")（英）ーここも膨大です。関数リファレンスにはこのページのRefrence 》 API Referenceからアクセスします。もっとも、こちらもググった方が早いでしょう。

```https://matplotlib.org/stable/index.html```

● [pywin32](https://pypi.org/project/pywin32/ "LINK")（英）ーPython Windows APIの開発プロジェクトのページですが、ユーザに参考になる情報はほとんどありません。本書で取り上げた`win32api.GetSystemMetrics()`関数のパラメータ値は[Micosoft Docs](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemmetrics "LINK")に記載されています。

```https://pypi.org/project/pywin32/```  
```https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemmetrics```

● [Pixabay](https://pixabay.com/ "LINK")（和）ー[本書で利用した画像](./C-Source.md)の入手元です。フリーでの商用利用も可なので、重宝します。

```https://pixabay.com/```

● [一般社団法人 カメラ映像機器工業会 規格類](https://www.cipa.jp/j/std/std-sec.html "LINK")（和）－[3.5節](./03-Information.md#35-Exif "INTERNAL")で説明したExif規格を（旧版の方なら）入手できます。ExifタグのIDと意味だけなら、Exif C++ライブラリの[Exiv2](https://exiv2.org/tags.html "LINK")からも確認できます。

```https://www.cipa.jp/j/std/std-sec.html```  
```https://exiv2.org/tags.html```

● [CSSの色名](https://www.w3.org/TR/css-color-4/#named-colors "LINK")（英）－[5.1.2節](./05-Colors.md#512-色名対応表 "INTERNAL")で説明したCSS（Cascade Style Sheet）の色名の仕様です。色名のリストは6.1章に掲載されています。

```https://www.w3.org/TR/css-color-4/#named-colors```

● [TECHNE 映像の教室](https://www.nhk.or.jp/techne/ "LINK")（和）ー[6.7.5節](./06-Draw.md#675-キネティックテキスト "INTERNAL")で作成したキネティックテキストの元ネタは、この番組の「タイポグラフィ」の回のタイトル（テクネID）です。サイトにはこの番組で紹介された古今の映像作品リストや各話タイトルが掲載されています。一部、今は亡きFlash動画のため閲覧できません（いろいろやれば観られますが）。

```https://www.nhk.or.jp/techne/```

● [Video Codecs for FOURCC](https://www.fourcc.org/codecs/ "LINK")（英）－[9.2.6節](./09-Others.md#926-GIFからビデオ "INTERNAL")で説明した、OpenCVのビデオライターで指定する4文字構成のビデオコーデックのリストです。

```https://www.fourcc.org/codecs/```


### D.2 書籍

Pythonおよび画像処理の学習によい書籍を次に数点示します。

- CG-ARTS協会: [ディジタル画像処理](https://www.cgarts.or.jp/book/img_engineer/ "LINK"), CG-ARTS協会 (2020).
- Luciano Ramalho: [Fluent Python](https://www.oreilly.co.jp/books/9784873118178/ "LINK"), オライリージャパン (2017).
- 永田雅人 & 豊沢聡: [実践OpenCV for Python 画像映像情報処理と機械学習](https://www.cutt.co.jp/book/978-4-87783-460-9.html "LINK"), カットシステム (2021).
