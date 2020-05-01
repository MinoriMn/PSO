# PSO
## 実行の流れ
- `jupyter notebook`
- pythonファイル書きだし `jupyter nbconvert --to python *.ipynb`

## 構成
- `Main` : メイン処理

## 実行
以下の6種のパラメータに関して5回ずつ実行
- 共通パラメータ{`世代数`:100}

- `個体数N`:50, `ω`:0.8, `c1`:2.7, `c2`:0.9
  - `prefix`:`N50G100_o0d8_cp2d7_cg0d9_0` ~ `N50G100_o0d8_cp2d7_cg0d9_4`
- `個体数N`:50, `ω`:0.8, `c1`:0.9, `c2`:2.7
  - `prefix`:`N50G100_o0d8_cp0d9_cg2d7_0` ~ `N50G100_o0d8_cp0d9_cg2d7_4`
- `個体数N`:20, `ω`:0.8, `c1`:2.7, `c2`:0.9
  - `prefix`:`N20G100_o0d8_cp2d7_cg0d9_0` ~ `N20G100_o0d8_cp2d7_cg0d9_4`
- `個体数N`:20, `ω`:0.8, `c1`:0.9, `c2`:2.7
  - `prefix`:`N20G100_o0d8_cp0d9_cg2d7_0` ~ `N20G100_o0d8_cp0d9_cg2d7_4`
- `個体数N`:20, `ω`:0.2, `c1`:1.8, `c2`:0.6
  - `prefix`:`N20G100_o0d8_cp1d8_cg0d6_0` ~ `N20G100_o0d8_cp1d8_cg0d6_4`
- `個体数N`:20, `ω`:0.2, `c1`:0.6, `c2`:1.8
  - `prefix`:`N20G100_o0d8_cp0d6_cg1d8_0` ~ `N20G100_o0d8_cp0d6_cg1d8_4`

## 実行結果
- `csv/<prefix>/<prefix>_best_eval.csv` … 各世代のpbest, gbestの値記録
- `video/` … 探索の様子(↓に記載したもの)
  - 打点の説明 `gray`:`x`, `white`:`pbest`, `orange`:`gbest`

#### `個体数N`:50, `ω`:0.8, `c1`:2.7, `c2`:0.9
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp2d7_cg0d9_0_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp2d7_cg0d9_1_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp2d7_cg0d9_2_video.gif" width="33%">
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp2d7_cg0d9_3_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp2d7_cg0d9_4_video.gif" width="33%">

#### `個体数N`:50, `ω`:0.8, `c1`:0.9, `c2`:2.7
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp0d9_cg2d7_0_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp0d9_cg2d7_1_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp0d9_cg2d7_2_video.gif" width="33%">
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp0d9_cg2d7_3_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N50G100_o0d8_cp0d9_cg2d7_4_video.gif" width="33%">

#### `個体数N`:20, `ω`:0.8, `c1`:2.7, `c2`:0.9
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp2d7_cg0d9_0_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp2d7_cg0d9_1_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp2d7_cg0d9_2_video.gif" width="33%">
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp2d7_cg0d9_3_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp2d7_cg0d9_4_video.gif" width="33%">

#### `個体数N`:20, `ω`:0.8, `c1`:0.9, `c2`:2.7
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp0d9_cg2d7_0_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp0d9_cg2d7_1_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp0d9_cg2d7_2_video.gif" width="33%">
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp0d9_cg2d7_3_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d8_cp0d9_cg2d7_4_video.gif" width="33%">

#### `個体数N`:20, `ω`:0.2, `c1`:1.8, `c2`:0.6
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp1d8_cg0d6_0_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp1d8_cg0d6_1_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp1d8_cg0d6_2_video.gif" width="33%">
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp1d8_cg0d6_3_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp1d8_cg0d6_4_video.gif" width="33%">

#### `個体数N`:20, `ω`:0.2, `c1`:0.6, `c2`:1.8
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp0d6_cg1d8_0_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp0d6_cg1d8_1_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp0d6_cg1d8_2_video.gif" width="33%">
<img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp0d6_cg1d8_3_video.gif" width="33%"><img src="https://github.com/MinoriMn/PSO/blob/run/some_pattern/video/N20G100_o0d2_cp0d6_cg1d8_4_video.gif" width="33%">
