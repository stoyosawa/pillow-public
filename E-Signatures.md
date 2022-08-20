<!-- This page is automatically generated. --->

<!-- This page is automatically generated. --->
## 付録E 関数リスト

本付録では、本書で取り上げたPillow、Numpy、tkinter、OpenCV、matplotlib、win32apiの関数をまとめて表に示します。項目は関数のアルファベット順（記号はASCIIコード順）に並べています。

本書は、[Pillowドキュメント](https://pillow.readthedocs.io/en/stable/)記載の関数をすべてカバーしているわけではありません。また、Pillowの書籍なため、Numpyなどの他ライブラリについては本書で利用する範囲での記載で、機能や引数などは一部省略しています。ご了承ください。

関数 | 章節 | 説明
----|----|----
`Axes.plot(x, y, color=cycler)` | [9.3.1節](./09-Others.md#931-グラフプロット "INTERNAL") | （matplotlib）グラフ（Axes）オブジェクトにグラフをプロットする。
`cv2.cvtColor(src, code)` | [9.2.3節](./09-Others.md#923-日本語文字列の描画 "INTERNAL") | （OpenCV）カラーモードを変換する（ここではRGBとBGRの相互変換）。
`cv2.imread(filename)` | [9.2.1節](./09-Others.md#921-画像表示 "INTERNAL") | （OpenCV）画像ファイルを開く。
`cv2.imshow(winname, src)` | [9.2.1節](./09-Others.md#921-画像表示 "INTERNAL") | （OpenCV）画像を表示する。
`cv2.imwrite(filename, src)` | [9.2.3節](./09-Others.md#923-日本語文字列の描画 "INTERNAL") | （OpenCV）画像を保存する。
`cv2.stylization(src)` | [9.2.2節](./09-Others.md#922-凝った画像処理 "INTERNAL") | （OpenCV）鉛筆画風画像を生成する。
`cv2.VideoCapture(filename)` | [9.2.5節](./09-Others.md#925-ビデオからGIF "INTERNAL") | （OpenCV）ビデオファイルからビデオキャプチャオブジェクトを生成する。
`cv2.VideoCapture.get(propertyId)` | [9.2.5節](./09-Others.md#925-ビデオからGIF "INTERNAL") | （OpenCV）ビデオキャプチャオブジェクトから属性を取得する。
`cv2.VideoCapture.read()` | [9.2.5節](./09-Others.md#925-ビデオからGIF "INTERNAL") | （OpenCV）ビデオキャプチャオブジェクトから現在のフレームを取得する。
`cv2.VideoWriter(filename, fourcc, fps, frameSize)` | [9.2.6節](./09-Others.md#926-GIFからビデオ "INTERNAL") | （OpenCV）ビデオ書き出しオブジェクトを生成する。
`cv2.VideoWriter.release()` | [9.2.6節](./09-Others.md#926-GIFからビデオ "INTERNAL") | （OpenCV）`cv2.VideoWriter`オブジェクトを閉じる。
`cv2.VideoWriter.write(image)` | [9.2.6節](./09-Others.md#926-GIFからビデオ "INTERNAL") | （OpenCV）`cv2.VideoWriter`オブジェクトにフレームを書き込む。
`cv2.VideoWriter_fourcc(c1, c2, c3, c4)` | [9.2.6節](./09-Others.md#926-GIFからビデオ "INTERNAL") | （OpenCV）コーデック種別名をFourCC整数に変換する。
`cv2.waitKey(delay)` | [9.2.1節](./09-Others.md#921-画像表示 "INTERNAL") | （OpenCV）ユーザ入力を待つ。
`features.check(feature)` | [2.4.5節](./02-OpenShowClose.md#245-GIFからWebPへの変換 "INTERNAL") | 指定のモジュール、コーデック、あるいは機能がサポートされていれば`True`を返す。
`Image.alpha_composite(image1, image2)` | [8.5節](./08-Blend.md#85-アルファ合成 "INTERNAL") | アルファ合成。
`Image.close()` | [2.1.4節](./02-OpenShowClose.md#214-画像オブジェクトを閉じる "INTERNAL") | `Image`オブジェクトを閉じる。
`Image.composite(image1, image2, mask)` | [4.4.4節](./04-NewImage.md#444-マスキング "INTERNAL") | マスク付きでの画像の重ね合わせ（機能的には`Image.paste()`と同じ）。
`Image.convert(mode=None, dither=Image.Dither.FLOYDSTEINBERG, palette=Image.Palette.ADAPTIVE, colors=256)` | [5.4節](./05-Colors.md#54-モード変換 "INTERNAL") | 画像のモードを変換する。
`Image.effect_mandelbrot(size, extent, quality)` | [4.5.3節](./04-NewImage.md#453-マンデルブロ "INTERNAL") | マンデルブロ画像の生成。
`Image.effect_noise(size, sigma)` | [4.5.2節](./04-NewImage.md#452-ガウスノイズ "INTERNAL") | ガウス雑音を散りばめた画像を生成する。平均値μは常に128。
`Image.effect_spread(distance)` | [7.4.6節](./07-ImageProcessing.md#746-爆裂効果 "INTERNAL") | ピクセルをランダムに散らすことでざらついた、すりガラスを通して見たような画像を得る。
`Image.eval(image, function(pix))` | [7.3.1節](./07-ImageProcessing.md#731-全体処理 "INTERNAL") | 指定の関数を用いて、ピクセル単位で画像全体を操作する。
`Image.extrema()` | [3.3節](./03-Information.md#33-統計情報 "INTERNAL") | 画像から最小最大値のタプル（モノクロ）あるいはタプルのタプル（カラー）を返す。
`Image.filter(filter)` | [7.4.2節](./07-ImageProcessing.md#742-フィルタ処理 "INTERNAL") | フィルタリング処理。事前に用意されたフィルタが利用できる。
`Image.fromarray(arr, mode=None)` | [4.3.2節](./04-NewImage.md#432-Numpyから画像 "INTERNAL") | `np.ndarray`から`Image`オブジェクトを生成する。
`Image.frombytes(mode, size, data)` | [4.2.1節](./04-NewImage.md#421-バイトから画像 "INTERNAL") | `bytes`からモードとサイズを指定して`Image`オブジェクトを生成する。
`Image.getbands()` | [3.2節](./03-Information.md#32-属性取得関数 "INTERNAL") | 画像バンドを文字単位分解したタプルを返す。
`Image.getbbox()` | [3.2節](./03-Information.md#32-属性取得関数 "INTERNAL") | 画像のバウンディングボックスを4要素のタプルで返す（透過画像でのみ意味がある）。
`Image.getchannel(channel)` | [5.5.2節](./05-Colors.md#552-バンド抽出 "INTERNAL") | 指定のバンドの画像（Lモード）を抽出する。
`Image.getcolors(maxcolors=256)` | [5.1.8節](./05-Colors.md#518-色数 "INTERNAL") | GIFのヒストグラムを(度数, インデックス番号)のタプルのリストで返す。
`Image.getdata(band=None)` | [4.2.3節](./04-NewImage.md#423-シーケンスの取得 "INTERNAL") | 画像のピクセルデータをシーケンスオブジェクトにして返す。
`Image.getexif()` | [3.5節](./03-Information.md#35-Exif "INTERNAL") | 画像オブジェクトからExif情報を取得する。
`Image.getpixel(xy)` | [7.3節](./07-ImageProcessing.md#73-ピクセル操作 "INTERNAL") | 画像から指定の位置のピクセル値を取得する。
`Image.histogram(mask=None)` | [3.4節](./03-Information.md#34-画像ヒストグラム "INTERNAL") | 画像オブジェクトからヒストグラムのリストを取得する。
`Image.init()` | [2.3節](./02-OpenShowClose.md#23-画像ファイルフォーマット "INTERNAL") | Pillowを明示的に初期化することで、画像ファイルフォーマット関連情報を読み込む。
`Image.linear_gradient(mode)` | [4.5.1節](./04-NewImage.md#451-グラデーション "INTERNAL") | 最上辺の黒帯から再下端の白帯まで垂直にグラデーションを付けた(256, 256)のモノクロ画像を生成。
`Image.load()` | [2.1.5節](./02-OpenShowClose.md#215-データの強制読み込み "INTERNAL") | `Image`オブジェクトから強制的にデータを読んで、ファイルオブジェクトを閉じる。
`Image.merge(mode, bands)` | [5.5.3節](./05-Colors.md#553-バンド合成 "INTERNAL") | 複数の単一バンド（Lモード）の画像から指定のモードのカラー画像を合成する。
`Image.new(mode, size, color=0)` | [4.1節](./04-NewImage.md#41-新規生成 "INTERNAL") | 指定のモード、サイズの画像を生成する。
`Image.open(fp, formats=None)` | [2.1.1節](./02-OpenShowClose.md#211-画像ファイルを開く "INTERNAL") | 画像ファイルを開き、`Image`オブジェクトを返す。
`Image.putalpha(alpha)` | [5.4.6節](./05-Colors.md#546-RGBのRGBA化 "INTERNAL") | RGBカラー`Image`オブジェクトにアルファバンドを加える。
`Image.putdata(data, scale=1.0, offset=0.0)` | [4.2.4節](./04-NewImage.md#424-シーケンスのセット "INTERNAL") | シーケンスで表現されたピクセル値データを`Image`にセットする。
`Image.putpalette(data)` | [5.2.3節](./05-Colors.md#523-カラーパレットの変更 "INTERNAL") | 画像のカラーパレットを入れ替える。
`Image.putpixel(xy, value)` | [7.3節](./07-ImageProcessing.md#73-ピクセル操作 "INTERNAL") | 画像の指定の位置のピクセル値を置き換える。
`Image.quantize(colors=256, palette=None)` | [5.2.4節](./05-Colors.md#524-GIFへの変換 "INTERNAL") | 画像をGIF（Pモード）に変換する。
`Image.radial_gradient(mode)` | [4.5.1節](./04-NewImage.md#451-グラデーション "INTERNAL") | 中心の黒点から周辺へ白く同心円状にグラデーションを付けた(256, 256)のモノクロ画像を生成。
`Image.registered_extensions()` | [2.3節](./02-OpenShowClose.md#23-画像ファイルフォーマット "INTERNAL") | 利用できる{拡張子:画像ファイルフォーマット}の辞書を返す。
`Image.resize(size, resample=None, box=None)` | [7.1.1節](./07-ImageProcessing.md#711-リサイズ "INTERNAL") | 画像サイズを指定の (width, height) タプルに拡大縮する。アスペクト比は保存されない。
`Image.rotate(angle, resample=Image.Resampling.NEAREST, expand=False, center=None, translate=None, fillcolor=None)` | [7.2.1節](./07-ImageProcessing.md#721-回転 "INTERNAL") | 画像を回転する。
`Image.save(fp, **params)` | [2.4節](./02-OpenShowClose.md#24-画像ファイルの保存 "INTERNAL") | `Image`オブジェクトをファイルに保存。画像ファイルフォーマットはファイルの拡張子から判定される。
`Image.seek(frame)` | [2.4.5節](./02-OpenShowClose.md#245-GIFからWebPへの変換 "INTERNAL") | 指定のフレーム番号までアニメーション画像のフレームを移動させる。
`Image.show()` | [2.1.2節](./02-OpenShowClose.md#212-画像を表示 "INTERNAL") | `Image`オブジェクトをデフォルト画像表示アプリケーションで表示する。
`Image.split()` | [5.5.1節](./05-Colors.md#551-バンド分解 "INTERNAL") | 画像をバンド単位に分解し、そのタプルを返す。
`Image.tell()` | [2.4.5節](./02-OpenShowClose.md#245-GIFからWebPへの変換 "INTERNAL") | アニメーション画像の現在のフレーム番号を取得する。
`Image.thumbnail(size, resample=Image.Resampling.BICUBIC)` | [7.1.5節](./07-ImageProcessing.md#715-サムネイル "INTERNAL") | 画像からサムネイル（縮小版）の画像を生成する。
`Image.tobytes()` | [4.2.2節](./04-NewImage.md#422-画像からバイト "INTERNAL") | `Image`オブジェクトからピクセル値の`bytes`を取得する。
`ImageChops.add(fg, bg, scale=1.0, offset=0.0)` | [8.1.1節](./08-Blend.md#811-単純加算 "INTERNAL") | 2枚の画像を加算する。
`ImageChops.blend(fg, bg, alpha)` | [8.1.2節](./08-Blend.md#812-輝度補正付き加算 "INTERNAL") | 輝度調整付きで2枚の画像を加算する。
`ImageChops.difference(fg, bg)` | [8.2節](./08-Blend.md#82-画像の差分 "INTERNAL") | 画像の差分の絶対値を生成する。
`ImageChops.multiply(fg, bg)` | [8.3節](./08-Blend.md#83-画像の乗算 "INTERNAL") | 画像の積を生成する。
`ImageChops.offset(image, xoffset, yoffset=None)` | [7.2.4節](./07-ImageProcessing.md#724-はみ出しの折り返し "INTERNAL") | 平行移動。はみ出したピクセルは空き領域に回り込んで配置される。
`ImageChops.screen(fg, bg)` | [8.4.1節](./08-Blend.md#841-スクリーン "INTERNAL") | 2枚の画像に対してスクリーン処理を行う。
`ImageColor.getcolor(color, mode)` | [5.1.4節](./05-Colors.md#514-カラーチャート "INTERNAL") | 指定の色名の輝度（モノクロ化したときのピクセル値）を返す。
`ImageColor.getrgb(color)` | [5.1.1節](./05-Colors.md#511-RGB "INTERNAL") | 色名（文字列）からRGBのタプルを返す。
`ImageDraw.arc(xy, start, end, fill=None, width=0)` | [6.5.2節](./06-Draw.md#652-円弧 "INTERNAL") | 円弧（円の一部）を描く。
`ImageDraw.chord(xy, start, end, fill=None, outline=None, width=1)` | [6.5.2節](./06-Draw.md#652-円弧 "INTERNAL") | 弦（円弧とその端点を結ぶ線で構成された閉曲面）を描く。
`ImageDraw.Draw(image)` | [6.1節](./06-Draw.md#61-描画オブジェクト "INTERNAL") | 描画対象の`Image`に対する`ImageDraw`オブジェクトを準備する。
`ImageDraw.ellipse(xy, fill=None, outline=None, width=1)` | [6.5.1節](./06-Draw.md#651-楕円 "INTERNAL") | 楕円・円を描く。
`ImageDraw.line(xy, fill=None, width=0, joint=None)` | [6.3節](./06-Draw.md#63-線分 "INTERNAL") | 線を描く。
`ImageDraw.pieslice(xy, start, end, fill=None, outline=None, width=1)` | [6.5.2節](./06-Draw.md#652-円弧 "INTERNAL") | 扇（円のパイ状のスライス）を描く。
`ImageDraw.point(xy, fill=None)` | [6.2節](./06-Draw.md#62-点 "INTERNAL") | 点を描く。
`ImageDraw.polygon(xy, fill=None, outline=None, width=1)` | [6.4.3節](./06-Draw.md#643-多角形 "INTERNAL") | 多角形を描く。
`ImageDraw.rectangle(xy, fill=None, outline=None, width=1)` | [6.4.1節](./06-Draw.md#641-長方形 "INTERNAL") | 長方形を描く。
`ImageDraw.regular_polygon(bounding_circle, n_sides, rotation=0, fill=None, outline=None)` | [6.4.2節](./06-Draw.md#642-正多角形 "INTERNAL") | 正多角形を描く。
`ImageDraw.rounded_rectangle(xy, radius=0, fill=None, outline=None, width=1)` | [6.4.1節](./06-Draw.md#641-長方形 "INTERNAL") | 角を丸めた長方形を描く。
`ImageDraw.text(xy, text, fill=None, font=None, anchor=None)` | [6.7節](./06-Draw.md#67-文字列 "INTERNAL") | 文字列を描く。
`ImageEnhance._Enhance.enhance(factor)` | [5.3.3節](./05-Colors.md#533-画像調整 "INTERNAL") | `ImageEnhance.{Color, Contrast, Brightness, Sharpness}`オブジェクトを実際に補正する関数。
`ImageFilter.Kernel(size, kernel, scale=None, offset=0)` | [7.4.5節](./07-ImageProcessing.md#745-自作フィルタ "INTERNAL") | `Image.filter()`で用いるフィルタ（カーネル）オブジェクトを生成する。
`ImageFilter.MedianFilter(size=3)` | [7.4.4節](./07-ImageProcessing.md#744-フィルタコンストラクタ "INTERNAL") | メディアンフィルタを実装した`ImageFilter`のフィルタコンストラクタの1つ。
`ImageFont.getbbox(text)` | [6.7.3節](./06-Draw.md#673-テキストサイズ "INTERNAL") | このフォントを用いて指定の文字列を描画したときのバウンディングボックスを返す。
`ImageFont.load_default()` | [6.7.3節](./06-Draw.md#673-テキストサイズ "INTERNAL") | デフォルトフォントのフォントオブジェクトを取得する。
`ImageFont.truetype(font=None, size=10)` | [6.7.2節](./06-Draw.md#672-TrueTypeフォント "INTERNAL") | TrueTypeフォントを準備する。
`ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=False)` | [9.4.2節](./09-Others.md#942-スクリーンキャプチャ "INTERNAL") | スクリーンキャプチャ。
`ImageGrab.grabclipboard()` | [9.4.1節](./09-Others.md#941-クリップボード "INTERNAL") | Windowsクリップボードに収容された画像データを一時保存したファイルのリストを返す。
`ImageOps.contain(image, size, resample=Image.Resampling.BICUBIC)` | [7.1.4節](./07-ImageProcessing.md#714-アスペクト比保存リサイズ "INTERNAL") | アスペクト比を保存しつつ、可能な限り指定のサイズになるようリサイズする。
`ImageOps.exif_transpose(image)` | [3.5.1節](./03-Information.md#351-Exifを用いた画像回転 "INTERNAL") | ExifのOrientationタグに従って画像を回転反転する。
`ImageOps.grayscale(image)` | [5.3.1節](./05-Colors.md#531-モノクロ化 "INTERNAL") | 画像をモノクロ化（Lモード）する。
`ImageOps.invert(image)` | [5.3.2節](./05-Colors.md#532-反転 "INTERNAL") | 画像の色調を反転（ネガ化）する。
`ImageOps.posterize(image, bits)` | [5.3.4節](./05-Colors.md#534-ポスタリゼーション "INTERNAL") | 指定のビット数まで画像の色数を下げる。
`ImageOps.scale(image, factor, resample=Image.Resampling.BICUBIC)` | [7.1.1節](./07-ImageProcessing.md#711-リサイズ "INTERNAL") | 指定の倍率で画像を拡大（1以上）縮小（1未満）する。
`ImageShow.register(viewer, order=1)` | [2.2節](./02-OpenShowClose.md#22-画像表示アプリケーションの変更 "INTERNAL") | `Image.show()`で用いる画像表示アプリケーションを変更する。
`ImageStat.Stat(image, mask=None)` | [3.3節](./03-Information.md#33-統計情報 "INTERNAL") | 画像統計情報を収容した`ImageStat.Stat`クラスのコンストラクタ。
`ImageTk.PhotoImage(image=None)` | [9.1.2節](./09-Others.md#912-画像表示その2 "INTERNAL") | Pillowの画像オブジェクトをTkの画像形式であるPhotoImageに変換する。
`np.array(object)` | [4.3.1節](./04-NewImage.md#431-画像からNumpy "INTERNAL") | オブジェクトから`np.ndarray`を生成する。
`np.asarray(a, dtype=None)` | [5.2.3節](./05-Colors.md#523-カラーパレットの変更 "INTERNAL") | 行列風（array-like）のデータ列を`np.ndarray`に変換する。
`np.astype(dtype)` | [4.5.2節](./04-NewImage.md#452-ガウスノイズ "INTERNAL") | 行列内のすべての要素を指定のデータ型に変換する。
`np.empty(shape, dtype=float)` | [4.3.2節](./04-NewImage.md#432-Numpyから画像 "INTERNAL") | `np.ndarray`を初期化し、オブジェクトを返す。要素は初期化されないのでランダムな値になっている。
`np.linalg.norm(x)` | [5.2.3節](./05-Colors.md#523-カラーパレットの変更 "INTERNAL") | 行列のノルム（距離）を計算する。
`np.ones(shape, dtype=float)` | [4.3.2節](./04-NewImage.md#432-Numpyから画像 "INTERNAL") | 要素をすべて1で埋めた`np.ndarray`を返す。
`np.random.randint(low, high=None, shape=None, dtype=int)` | [4.5.2節](./04-NewImage.md#452-ガウスノイズ "INTERNAL") | ランダムノイズで埋めた行列を返すNumpyのランダム関数。行列要素は整数。
`np.random.standard_normal(shape=None)` | [4.5.2節](./04-NewImage.md#452-ガウスノイズ "INTERNAL") | 正規分布に従ったランダムノイズで埋めた行列を返すNumpyのランダム関数。行列要素は浮動小数点数。
`np.reshape(a, newshape)` | [7.4.3節](./07-ImageProcessing.md#743-ImageFilterのフィルタ行列 "INTERNAL") | 中のデータを変更することなく行列の形を変える。
`np.zeros(shape, dtype=float)` | [4.3.2節](./04-NewImage.md#432-Numpyから画像 "INTERNAL") | 要素をすべて0で埋めた`np.ndarray`を返す。
`plt.imshow(image)` | [9.3.2節](./09-Others.md#932-Image画像をmatplotlibで開く "INTERNAL") | （matplotlib）Image画像をmatplotlibに貼り付ける。
`plt.savefig(filename)` | [9.3.1節](./09-Others.md#931-グラフプロット "INTERNAL") | （matplotlib）Figureを画像ファイルに保存する。
`plt.show()` | [9.3.1節](./09-Others.md#931-グラフプロット "INTERNAL") | （matplotlib）Figureを表示する。
`plt.subplots()` | [9.3.1節](./09-Others.md#931-グラフプロット "INTERNAL") | （matplotlib）グラフ描画のためのコンテナ（Figure）とグラフ（Axes）オブジェクトを生成する。
`plt.title(title)` | [9.3.3節](./09-Others.md#933-ヒストグラムを描く "INTERNAL") | （matplotlib）タイトルを加える。
`plt.xlabel(xlabel)` | [9.3.3節](./09-Others.md#933-ヒストグラムを描く "INTERNAL") | （matplotlib）x軸にラベルを加える。
`plt.ylabel(ylabel)` | [9.3.3節](./09-Others.md#933-ヒストグラムを描く "INTERNAL") | （matplotlib）y軸にラベルを加える。
`tk.Canvas(parent, option=value)` | [9.1.1節](./09-Others.md#911-画像表示 "INTERNAL") | （Tk）キャンバスオブジェクトを生成する。
`tk.PhotoImage(file=file)` | [9.1.1節](./09-Others.md#911-画像表示 "INTERNAL") | （Tk）画像を読み込む。
`tk.Tk()` | [9.1.1節](./09-Others.md#911-画像表示 "INTERNAL") | （Tk）トップレベルオブジェクト（ウィンドウ）を生成する。
`win32api.GetSystemMetrics(value)` | [9.4.3節](./09-Others.md#943-ディスプレイサイズ "INTERNAL") | （win32api）Windowsのシステム情報を取得する。

