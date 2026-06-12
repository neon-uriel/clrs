# scripts

講義ノートの補助スクリプト。

## verify_math.py

各章に登場する数式・数値主張を SymPy で機械検証する回帰テスト。

```bash
.venv/bin/python scripts/verify_math.py
```

- 全チェックが通れば終了コード 0、1つでも失敗すれば 1 を返す。
- 新しい式をノートに追加したら、このスクリプトにも `check(...)` を足しておくと、
  以後その式の正しさを自動で再確認できる。
- 依存は `requirements.txt`（`sympy` ほか）。仮想環境の作り方は [CLAUDE.md](../CLAUDE.md) を参照。
