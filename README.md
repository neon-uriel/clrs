# CLRS 講義ノート

VitePress で公開するための Markdown 講義ノート。

## ディレクトリ構成

```text
docs/                 # VitePress で公開する講義ノート
implementations/cpp/  # CLRS の C++ 実装
```

## ローカル開発

```sh
npm install
npm run dev
```

## ビルド

```sh
npm run build
```

## Cloudflare Pages

Cloudflare Pages では次の設定にする。

- Framework preset: `None` または `VitePress` を選んで設定を上書き
- Build command: `npm run build`
- Build output directory: `docs/.vitepress/dist`
- Root directory: リポジトリ直下

GitHub リポジトリと Cloudflare Pages を接続すると、Markdown を更新して push するたびに自動でビルド・デプロイされる。
