# C++ 実装

CLRS の内容を C++ で実装したコードを置く場所。

## ディレクトリ構成

```text
implementations/cpp/
  chapter-02/
    merge_sort.cpp
```

## ビルド（g++）

```sh
g++ -std=c++17 implementations/cpp/chapter-02/merge_sort.cpp -o /tmp/clrs-merge-sort
```

## 実行（g++）

```sh
/tmp/clrs-merge-sort
```

## VS Code でデバッグ

デバッグしたい `.cpp` ファイルを開いた状態で、Run and Debug から `C++: Debug active file (CodeLLDB)` を選んで実行する。

アクティブなファイルが `implementations/cpp/chapter-02/merge_sort.cpp` でも、今後追加する `implementations/cpp/chapter-03/*.cpp` でも同じ設定で動く。

ビルド成果物は `implementations/cpp/build/debug/` に作られる。

## Code Runner で実行

実行したい `.cpp` ファイルを開いて Code Runner を実行する。

ビルド成果物は `implementations/cpp/build/code-runner/` に作られる。
