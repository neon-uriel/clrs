#!/usr/bin/env python3
"""CLRS 講義ノートの数式を SymPy で機械検証する回帰テスト。

使い方:
    .venv/bin/python scripts/verify_math.py

新しい式を講義ノートに追加したら、ここにも check(...) を足しておくと、
以後ずっと自動で正しさを再確認できる。sympy スキル（.claude/skills/sympy）参照。
"""
import sympy as sp

n, i = sp.symbols("n i", positive=True)
results = []


def check(label, cond):
    results.append((label, bool(cond)))


# ===== 第2章: 挿入ソートの解析 =====
S1 = sp.summation(i, (i, 2, n))            # sum_{i=2}^n i
check("Ch2 sum_{i=2}^n i = n(n+1)/2 - 1", sp.simplify(S1 - (n * (n + 1) / 2 - 1)) == 0)
S2 = sp.summation(i - 1, (i, 2, n))        # sum_{i=2}^n (i-1)
check("Ch2 sum_{i=2}^n (i-1) = n(n-1)/2", sp.simplify(S2 - n * (n - 1) / 2) == 0)

c = sp.symbols("c4 c5 c6")
worst = sp.expand(c[0] * S1 + (c[1] + c[2]) * S2)
check("Ch2 最悪ケースは n の2次 (Theta(n^2))", sp.Poly(worst, n).degree() == 2)

# 第2章: マージソート再帰木の各レベル合計 = n*log2(n)
k = sp.symbols("k", integer=True)
total = sp.summation(n, (k, 0, sp.log(n, 2) - 1))
check("Ch2 マージ再帰木 合計 = n*log2(n) (Theta(n log n))",
      sp.simplify(total - n * sp.log(n, 2)) == 0)

# ===== 第3章: 漸近記法 =====
f = sp.Rational(1, 2) * n**2 - 3 * n
check("Ch3 Ex3.1 上界 c2=1/2 (n0=1)", sp.simplify(sp.Rational(1, 2) * n**2 - f) >= 0)
g = f - sp.Rational(1, 4) * n**2           # = n(n-12)/4
check("Ch3 Ex3.1 下界 c1=1/4 は n>=12 で成立",
      sp.simplify(g.subs(n, 12)) == 0 and sp.simplify(g.subs(n, 13)) > 0)

check("Ch3 Ex3.3-1 n^2 vs n^2+n は Theta", sp.limit(n**2 / (n**2 + n), n, sp.oo) == 1)
check("Ch3 Ex3.3-2 log2 n vs log10 n は Theta",
      sp.limit(sp.log(n, 2) / sp.log(n, 10), n, sp.oo).is_finite)
check("Ch3 Ex3.3-3 2^n = omega(2^(n/2))", sp.limit(2**n / 2**(n / 2), n, sp.oo) == sp.oo)
check("Ch3 Ex3.3-4 n^2 = o(2^n)", sp.limit(n**2 / 2**n, n, sp.oo) == 0)

check("Ch3 Stirling: lg(n!) = Theta(n lg n)",
      sp.limit(sp.log(sp.factorial(n)) / (n * sp.log(n)), n, sp.oo) == 1)
check("Ch3 n! = o(n^n)", sp.limit(sp.factorial(n) / n**n, n, sp.oo) == 0)
check("Ch3 n! = omega(2^n)", sp.limit(sp.factorial(n) / 2**n, n, sp.oo) == sp.oo)
check("Ch3 n^100 = o(1.001^n)",
      sp.limit(n**sp.Integer(100) / sp.Rational(1001, 1000)**n, n, sp.oo) == 0)
check("Ch3 (log n)^3 = o(n)", sp.limit(sp.log(n)**3 / n, n, sp.oo) == 0)

# ===== 第1章: TSP の数値主張 =====
sec_per_year = sp.Rational(31557600)       # ユリウス年
rate = sp.Integer(10)**9                    # 10^9 ルート/秒
N = sp.Integer(10)**6
log10_fact = (sp.loggamma(N + 1) / sp.log(10)).evalf(15)
check("Ch1 log10((10^6)!) ~ 5,565,709", round(float(log10_fact)) == 5565709)
log10_years = (sp.loggamma(N + 1) / sp.log(10)
               - sp.log(rate, 10) - sp.log(sp.Float(sec_per_year), 10)).evalf(15)
check("Ch1 log10(所要年数) ~ 5,565,692", round(float(log10_years)) == 5565692)

# n=30: 所要時間 ~ 8400兆年, 宇宙年齢(1.38e10年)の ~60万倍
yrs30 = sp.factorial(30) / rate / sec_per_year
check("Ch1 n=30 所要 ~8.4e15年 (8400兆年)", 8.0e15 < float(yrs30) < 9.0e15)
check("Ch1 n=30 宇宙年齢の ~60万倍", 5.5e5 < float(yrs30 / sp.Float("1.38e10")) < 6.5e5)

# ===== 出力 =====
print("=" * 64)
ok = True
for label, passed in results:
    print("PASS" if passed else "FAIL", "-", label)
    ok = ok and passed
print("=" * 64)
print(f"{sum(p for _, p in results)}/{len(results)} checks passed")
raise SystemExit(0 if ok else 1)
