# Jev Prompt Reversi: レポート

## 準備

### Move: 1

```
   A B C D E F G H
------------------
1|□□□□□□□□
2|□□□□□□□□
3|□□□□□□□□
4|□□□○●□□□
5|□□□●○□□□
6|□□□□□□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['D3', 'C4', 'F5', 'E6']
```

- 初手はどこも変わらないため、F5を選択

### Move: 2

```
   A B C D E F G H
------------------
1|□□□□□□□□
2|□□□□□□□□
3|□□□□□□□□
4|□□□○●□□□
5|□□□○●●□□
6|□□□○□□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['C3', 'C4', 'C5', 'C6', 'C7']
```

- 内側の石を裏返したい(D5狙い) -> 対象はC5、C6
- C5は周りに3つ、C6は周りに2つ石があり、多いのはC5 -> 開放度理論により、C5
- 開放度理論は置く石と裏返す石を対象に評価している

### Move: 3

```
   A B C D E F G H
------------------
1|□□□□□□□□
2|□□□□□□□□
3|□□□□□□□□
4|□□□○○○□□
5|□□●●○●□□
6|□□□○□□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['D3', 'E3', 'F3', 'D7', 'E7']
```

- 裏返す石の数はD3、F3が2つ、それ以外は1つ -> 裏返す石が少ない方を選ぶ
- 開放度理論により、E3一択

### Move: 4

```
   A B C D E F G H
------------------
1|□□□□□□□□
2|□□□□□□□□
3|□□□□●□□□
4|□□□●○○□□
5|□○○○○●□□
6|□□□○□□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['D3', 'F3', 'G4', 'A5', 'G5', 'B6', 'E6', 'F6', 'D7']
```

- 開放度理論により、D3、F6の順に良い
- 裏返す石の数も同じであるため、D3を選択
- 開放度理論は減点方式の方が良い(置く石と裏返す石の周りの空白の数)

### Move: 5

```
   A B C D E F G H
------------------
1|□□□□□□□□
2|□□□□□○□□
3|□□□●○□□□
4|□□□○●○□□
5|□○○○○●□□
6|□□□○□□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['E2', 'F3', 'C4', 'G4', 'A5', 'C6', 'E6', 'D7']
```

- 開放度理論により、C4

### Move: 6

```
   A B C D E F G H
------------------
1|□□□□□□□□
2|□□□□○○□□
3|□□□○○□□□
4|□□○●●○□□
5|□○○○○●□□
6|□□□○□□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['E1', 'G1', 'C2', 'D2', 'F3', 'B4', 'G4', 'A5', 'B6', 'C6', 'E6', 'F6', 'D7']
```

- 開放度理論により、C6とE6に絞れる
- 先読みをすると、C6の方が相手のF3を消していてよい手に見えるが、C3に打たれるため、結局大差はない
- C6は相手にE6を与えているため、E6の方が良い
- 相手の合法手の数が少ない手はE6
- 開放度が同じ時は「相手」の合法手の数が少ない方を選ぶ

### Move: 7

```
   A B C D E F G H
------------------
1|□□□□□□□□
2|□□□□○○□□
3|□□□○○○□□
4|□□○●○○□□
5|□○○○●●□□
6|□□□○●□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['E1', 'F1', 'G1', 'C2', 'D2', 'B3', 'G3', 'B4', 'G4', 'A5', 'B6', 'C6', 'C7', 'D7']
```

- 開放度理論により、E1、D2に絞れる
- 相手の合法手の数は、8、9とE1の方が良い
- よってE1に決まる

### Move: 8

```
   A B C D E F G H
------------------
1|□□□○●□□□
2|□□□□○○□□
3|□□□○●○□□
4|□□○●●○□□
5|□○○○●●□□
6|□□□○●□□□
7|□□□□□□□□
8|□□□□□□□□
Next Moves: ['C1', 'F1', 'G1', 'C2', 'D2', 'G2', 'B3', 'C3', 'G3', 'B4', 'G4', 'A5', 'G5', 'B6', 'C6', 'C7', 'D7']
```
- 開放度理論により、D2一択

### Move: 9

```
   A B C D E F G H
------------------
1|□□□○●□□□
2|□□□●○○□□
3|□□□●●○□□
4|□□○●●○□□
5|□○○○●●□□
6|□□□○○□□□
7|□□□□□○□□
8|□□□□□□□□
Next Moves: ['C1', 'F1', 'G1', 'G2', 'G3', 'B4', 'G4', 'A5', 'G5', 'A6', 'B6', 'C6', 'C7', 'D7', 'E7']
```

- 開放度理論により、C1、C6に絞られる
- 相手の合法手の数は、基本7、C1は4、C6は10であり、C1の方が良い

### Move: 10

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□●●○□□
4|□□○●●○□□
5|□○○○●●□□
6|□□□○○□□□
7|□□□□□○□□
8|□□□□□□□□
Next Moves: ['B1', 'F1', 'G1', 'G2', 'B3', 'C3', 'G3', 'B4', 'G4', 'A5', 'G5', 'A6', 'B6', 'C6', 'C7', 'D7', 'E7']
```

- 開放度理論により、C6一択

### Move: 11

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□□○●○○□□
5|□○○●●○□□
6|□□●○○□○□
7|□□□□□○□□
8|□□□□□□□□
Next Moves: ['G1', 'G2', 'B3', 'C3', 'G3', 'A4', 'B4', 'G4', 'A5', 'G5', 'B6', 'F6', 'C7', 'D7', 'E7', 'G8']
```

- 開放度理論により、B6一択

### Move: 12

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|□○○●●○□□
6|□●●○○□○□
7|□□□□□○□□
8|□□□□□□□□
Next Moves: ['G1', 'G2', 'B3', 'C3', 'G3', 'A4', 'G4', 'A5', 'G5', 'F6', 'C7', 'D7', 'E7', 'G8']
```

- 開放度理論により、A5一択

### Move: 13

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○●●●○□□
6|○○○○○□○□
7|□□□□□○□□
8|□□□□□□□□
Next Moves: ['G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'A7', 'B7', 'C7', 'D7', 'E7', 'G8']
```

- 開放度理論により、A7一択

### Move: 14

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○●●●○□□
6|●○○○○□○□
7|●○□□□○□□
8|□□□□□□□□
Next Moves: ['F1', 'G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'F6', 'C7', 'D7', 'E7', 'A8', 'C8', 'G8']
```

- 開放度理論により、F1、A8に絞れる
- 相手の合法手の数は、基本0、F1は3、A8は3
- ここで、自分の確定石の数はF1が0、A8が4
- 確定石と合法手、開放度理論の優先順位はここでは決められないが、今回は確定石を考慮してA8とする

### Move: 15

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○●●●○□□
6|●○○○○□○□
7|●●□○□○□□
8|●□□□□□□□
Next Moves: ['F1', 'G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'F6', 'C7', 'E7', 'D8', 'G8']
```

- 開放度理論により、C7一択

### Move: 16

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○○●●○□□
6|●●●○○□○□
7|●●●○○○□□
8|●□□□□□□□
Next Moves: ['F1', 'G1', 'G2', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'F6', 'G7', 'D8', 'E8', 'G8']
```

- 開放度理論により、F6一択

### Move: 17

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○○●●○○□
6|●●●●●○○□
7|●●●○○○□□
8|●□□□□□□□
Next Moves: ['F1', 'G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'H5', 'H6', 'G7', 'C8', 'D8', 'E8', 'F8', 'G8']
```

- 開放度理論により、C8、D8に絞れる
- 相手の合法手の数、確定石の数は同じ
- 強いて言うならC8はハイパー偶数の種ができるので、D8の方が優れている

### Move: 18

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○○●○○○□
6|●○●○●○○□
7|●○○●○○□□
8|●○□●□□□□
Next Moves: ['F1', 'G1', 'G2', 'B3', 'C3', 'G3', 'A4', 'G4', 'H4', 'H5', 'H6', 'G7', 'C8', 'E8', 'G8']
```

- 開放度理論により、C8一択

### Move: 19

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○○●○○○□
6|●○○○●○○□
7|●●●○○○□□
8|●●●●○□□□
Next Moves: ['F1', 'G1', 'G2', 'B3', 'C3', 'G3', 'A4', 'G4', 'H4', 'H5', 'H6', 'G7', 'F8', 'G8']
```

- 開放度理論により、F8一択

### Move: 20

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□○○●○□□
4|□○○○○○□□
5|●○○●○○○□
6|●○○○●○○□
7|●●●○○○□□
8|●●●●●●□□
Next Moves: ['F1', 'G1', 'G2', 'A3', 'B3', 'G3', 'A4', 'G4', 'H4', 'H5', 'H6', 'G7', 'G8']
```

- 開放度理論により、A4一択

### Move: 21

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□○○●○□□
4|●○○○○○□□
5|●●○●○○○□
6|●○●○●○○□
7|●●●●○○□□
8|●●●●●●□□
Next Moves: ['F1', 'G1', 'G2', 'A3', 'B3', 'G3', 'G4', 'H4', 'H5', 'H6', 'G7', 'G8']
```

- 開放度理論により、G8、A3に絞れる
- 相手の合法手の数、確定石の数は同じ
- どちらでも良いが、裏返す石が少ないことと偶数に打ちたくないのでG8の方が良いか

### Move: 22

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□○○●○□□
4|●○○○○○□□
5|●●○●○○○□
6|●○●○●○○□
7|●●●●○○○□
8|●●●●●●●□
Next Moves: ['F1', 'G1', 'G2', 'A3', 'B3', 'G3', 'G4', 'H4', 'H5', 'H6', 'H7']
```

- 開放度理論により、H7、A3に絞れる
- 相手の合法手の数は同じ
- 確定石はA3の方が多い

### Move: 23

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|●○○○●○□□
4|●○○○○○□□
5|●○●●○○○□
6|●○●●●○○□
7|●●●●●○○□
8|●●●●●●●□
Next Moves: ['F1', 'G1', 'A2', 'B2', 'G2', 'G3', 'G4', 'H4', 'H5', 'H6', 'H7']
```

- 開放度理論により、A2、B2、H7に絞れる
- 相手の合法手の数はA2、H7が1、B2が2
- 確定石はA2が多い

### Move: 24

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|●○○○○○□□
3|●○○○●○□□
4|●○●○○○□□
5|●○●●○○○□
6|●○●●●○○□
7|●●●●●○○□
8|●●●●●●●□
Next Moves: ['B1', 'F1', 'G1', 'G2', 'G3', 'G4', 'H4', 'H5', 'H6', 'H7']
```

- 開放度理論により、B1に絞れる
- しかし、Xを裏返して相手にA1を与えているため、良くない
- ここでようやくXにペナルティを与えることを考える
- Xを自分の石にする手B1、G2、G4、H6、H7を候補から外す
- 再度、開放度理論により、H4、G1に絞れる
- しかし、G1は相手にF1を与えてH1を許してしまうため、良くない
- ここでCに対してもペナルティを与える
- Cを自分の石にするB1、G1、H7は候補から外す
- よってH4となる
- なお、自分の石が隅にある時の隣接するXとCはペナルティの対象外とする(辺から伸びたCは後に検討)

### Move: 25

```
   A B C D E F G H
------------------
1|□□●●●□□□
2|●○○○○○□□
3|●○○○●○□□
4|●○●○○○□●
5|●○●●○○○○
6|●○●●●●○□
7|●●●●●○○□
8|●●●●●●●□
Next Moves: ['A1', 'B1', 'F1', 'G1', 'G2', 'G3', 'G4', 'H6', 'H7', 'H8']
```

- X or C:B1、G1、G2、G4、H6、H7
- 開放度理論により、A1一択(しかし、偶数理論的にはH8の方が良い)

### Move: 26

```
   A B C D E F G H
------------------
1|●○●●●□□□
2|●○○○○○□□
3|●○●○●○□□
4|●○●●○○□●
5|●○●●●○○○
6|●○●●●●○□
7|●●●●●○○□
8|●●●●●●●□
Next Moves: ['F1', 'G1', 'G2', 'G3', 'G4', 'H6', 'H7', 'H8']
```

- X or C: G1、G2、G4、H6、H7
- 開放度理論により、H8一択(結局H8に打ち、偶数理論を生かせている)

### Move: 27

```
   A B C D E F G H
------------------
1|●○○○○○□□
2|●○○○○○□□
3|●○●○●○□□
4|●○●●○○□●
5|●○●●●○○○
6|●○●●●●○□
7|●●●●●○●□
8|●●●●●●●●
Next Moves: ['G1', 'G2', 'G3', 'G4', 'H6']
```

- X or C: G2(G1は確定石)
- 開放度理論により、G4、H6に絞れる
- 相手の合法手の数はG4が4、H6が3
- よって、H6

### Move: 28

```
   A B C D E F G H
------------------
1|●○○○○○□□
2|●○○○○○□□
3|●○●○●○□□
4|●○●●○●□●
5|●○●●●○●●
6|●○●●●●○●
7|●●●●●○○○
8|●●●●●●●●
Next Moves: ['G1', 'G2', 'G3', 'G4']
```

- X or C: G2
- 開放度理論により、G4一択

### Move: 29

```
   A B C D E F G H
------------------
1|●○○○○○□□
2|●○○○○○□□
3|●○●○●○○□
4|●○●●○●○●
5|●○●●●●○●
6|●○●●●●○●
7|●●●●●○○○
8|●●●●●●●●
Next Moves: ['G1', 'G2', 'H2', 'H3']
```

- X or C: G2、H2
- 開放度理論により、G1、H3に絞れる
- 相手の合法手の数はG1の方が少ない(確定石の数は圧倒)

### Move: 30

```
   A B C D E F G H
------------------
1|●●●●●●●□
2|●○○○○●□□
3|●○●○●○○○
4|●○●●○●○○
5|●○●●●●○○
6|●○●●●●○○
7|●●●●●○○○
8|●●●●●●●●
Next Moves: ['G2', 'H2']
```

- X or C: G2(H2は確定石)
- 実質H2一択

### Move: 31

```
   A B C D E F G H
------------------
1|●●●●●●●□
2|●○○○○○○●
3|●○●○●○○●
4|●○●●○●○●
5|●○●●●●○●
6|●○●●●●○●
7|●●●●●○○●
8|●●●●●●●●
Next Moves: ['H1']
```

- H1一択

### 結果

```
   A B C D E F G H
------------------
1|●●●●●●●●
2|●○○○○○●●
3|●○●○●●○●
4|●○●●●●○●
5|●○●●●●○●
6|●○●●●●○●
7|●●●●●○○●
8|●●●●●●●●
```

- Black: 48, White: 16で黒の勝ち

### 考察

- プロンプトは「開放度理論」を最優先
- 開放度理論は「置いた石」と「裏返した石」の周りの空きマスを重複有りで減点
- 開放度理論が同じ値の時は「相手の合法手の数」を優先
- 相手の合法手の数も同じ時は「(自分の)確定石の数」を比較
- ただし、XやCにはペナルティを与える
- Xは隣接する隅が自分の石でない時にペナルティ
- Cは隣接する隅が自分の石でない時、かつそのCが確定石でない時にペナルティ
- 理論的には単独Cでない時はペナルティを与える必要はないが、安全のため

## Jev Prompt: 1

### プロンプト

- INFO内の各選択肢について、
- 最初に、LIBERTYの値が小さい候補を優先して選択。
- 次に、LIBERTYの値の最も小さい候補が複数ある場合は、その中でよりMOVABLEの値が小さい候補を優先して選択。
- 次に、MOVABLEの値の最も小さい候補が複数ある場合は、その中でよりSTABLEの値が大きい候補を優先して選択。
- ただし、XやCの値が0でない選択肢は選択を避ける。

### 対局結果

- MonteCarloPlayer : Wins = 36
- JevPlayer : Wins = 14

### 棋譜解析(手動)の結果

- LIBERTYの値による選択はできているという印象
- しかし、XやCに打ち、相手に隅を取られる展開が多く、勝率が低い

### 修正

- プログラムを確認したところXやCを見る際の石が相手の石だったため、自分の石を見るように修正

### 対局結果(v2)

- MonteCarloPlayer : Wins = 34
- JevPlayer : Wins = 16,

## Jev Prompt: 2

- 次の処理を順に行い、候補を選択する。
- なお、数値を比較せずに候補を選択しないこと。
- (1)INFO内の全候補を対象とする。
- (2)XやCの値が0以外の候補を除外する。
- (3)残りの候補の内、LIBERTYの値が最小の候補だけを残す。
- (4)その候補の内、MOVABLEの値が最小の候補だけを残す。
- (5)その候補の内、STABLEの値が最大の候補を残す。
- (6)この時点で候補が複数残っている場合はランダムに候補を選ぶ。

### プログラムの動作確認

- Move: 1

F5

---

- Move: 2

```python
{
    'MOVABLE_POS': ['C3', 'C4', 'C5', 'C6', 'C7'],
    'INFO': {
        'C3': {'LIBERTY': 11, 'MOVABLE': 4, 'STABLE': 0, 'X': 0, 'C': 0},
        'C4': {'LIBERTY': 10, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
        'C5': {'LIBERTY': 8, 'MOVABLE': 4, 'STABLE': 0, 'X': 0, 'C': 0},
        'C6': {'LIBERTY': 9, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 0},
        'C7': {'LIBERTY': 12, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0}
    }
}
```

Best Move: C5

Jev Move: C5

---

- Move: 3

```python
{
    'MOVABLE_POS': ['D3', 'E3', 'F3', 'D7', 'E7'],
    'INFO': {
        'D3': {'LIBERTY': 11, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
        'E3': {'LIBERTY': 8, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
        'F3': {'LIBERTY': 12, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'D7': {'LIBERTY': 11, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
        'E7': {'LIBERTY': 11, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0}
    }
}
```

Best Move: E3

Jev Move: E3

---

- Move: 4

```python
{
    'MOVABLE_POS': ['D3', 'F3', 'G4', 'A5', 'G5', 'B6', 'E6', 'F6', 'D7'],
    'INFO': {
        'D3': {'LIBERTY': 6, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
        'F3': {'LIBERTY': 8, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
        'G4': {'LIBERTY': 11, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'A5': {'LIBERTY': 19, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
        'G5': {'LIBERTY': 9, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
        'B6': {'LIBERTY': 9, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
        'E6': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
        'F6': {'LIBERTY': 7, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
        'D7': {'LIBERTY': 14, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0}
    }
}
```

Best Move: D3

Jev Move: D3

---

- Move: 5

```python
{
    'MOVABLE_POS': ['E2', 'F3', 'C4', 'G4', 'A5', 'C6', 'E6', 'D7'],
    'INFO': {
        'E2': {'LIBERTY': 7, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
        'F3': {'LIBERTY': 9, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'C4': {'LIBERTY': 4, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
        'G4': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
        'A5': {'LIBERTY': 19, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
        'C6': {'LIBERTY': 6, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'E6': {'LIBERTY': 5, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'D7': {'LIBERTY': 16, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0}
    }
}
```

Best Move: C4

Jev Move: C4

---

- Move: 6

```python
{
    'MOVABLE_POS': ['E1', 'G1', 'C2', 'D2', 'F3', 'B4', 'G4', 'A5', 'B6', 'C6', 'E6', 'F6', 'D7'],
    'INFO': {
        'E1': {'LIBERTY': 9, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'G1': {'LIBERTY': 11, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 1},
        'C2': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
        'D2': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'F3': {'LIBERTY': 6, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'B4': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
        'G4': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
        'A5': {'LIBERTY': 16, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
        'B6': {'LIBERTY': 8, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
        'C6': {'LIBERTY': 5, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
        'E6': {'LIBERTY': 5, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
        'F6': {'LIBERTY': 7, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
        'D7': {'LIBERTY': 13, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0}
    }
}
```

Best Move: E6

Jev Move: E6

---

- Move: 7

```python
{
   'MOVABLE_POS': ['E1', 'F1', 'G1', 'C2', 'D2', 'B3', 'G3', 'B4', 'G4', 'A5', 'B6', 'C6', 'C7', 'D7'], 
   'INFO': {
      'E1': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'F1': {'LIBERTY': 13, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'G1': {'LIBERTY': 9, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 1},
      'C2': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'D2': {'LIBERTY': 7, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'B3': {'LIBERTY': 10, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 7, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'B4': {'LIBERTY': 7, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'A5': {'LIBERTY': 13, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'B6': {'LIBERTY': 8, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'C6': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'C7': {'LIBERTY': 10, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 10, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0}
   }
}
```

Best Move: E1

上記の解説は誤りだが、結果的に同じ手

Jev Move: E1

---

- Move: 8

```python
{
   'MOVABLE_POS': ['C1', 'F1', 'G1', 'C2', 'D2', 'G2', 'B3', 'C3', 'G3', 'B4', 'G4', 'A5', 'G5', 'B6', 'C6', 'C7', 'D7'],
   'INFO': {
      'C1': {'LIBERTY': 6, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'F1': {'LIBERTY': 11, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'G1': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 1},
      'C2': {'LIBERTY': 8, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'D2': {'LIBERTY': 5, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'G2': {'LIBERTY': 8, 'MOVABLE': 11, 'STABLE': 0, 'X': 1, 'C': 0},
      'B3': {'LIBERTY': 10, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'C3': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'B4': {'LIBERTY': 7, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 7, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'A5': {'LIBERTY': 13, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 8, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'B6': {'LIBERTY': 8, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'C6': {'LIBERTY': 7, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'C7': {'LIBERTY': 10, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 10, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0}
   }
}
```

Best Move: D2

Jev Move: D2

---

- Move: 9

```python
{
   'MOVABLE_POS': ['C1', 'F1', 'G1', 'G2', 'G3', 'B4', 'G4', 'A5', 'G5', 'A6', 'B6', 'C6', 'C7', 'D7', 'E7'],
   'INFO': {
      'C1': {'LIBERTY': 4, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'F1': {'LIBERTY': 11, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'G1': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 1},
      'G2': {'LIBERTY': 12, 'MOVABLE': 7, 'STABLE': 0, 'X': 1, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'B4': {'LIBERTY': 7, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 7, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'A5': {'LIBERTY': 13, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 8, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'A6': {'LIBERTY': 12, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'B6': {'LIBERTY': 8, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'C6': {'LIBERTY': 4, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'C7': {'LIBERTY': 10, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 12, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'E7': {'LIBERTY': 7, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0}
   }
}
```

Best Move: C1

Jev Move: C1

---

- Move: 10

```python
{
   'MOVABLE_POS': ['B1', 'F1', 'G1', 'G2', 'B3', 'C3', 'G3', 'B4', 'G4', 'A5', 'G5', 'A6', 'B6', 'C6', 'C7', 'D7', 'E7'],
   'INFO': {
      'B1': {'LIBERTY': 6, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 1},
      'F1': {'LIBERTY': 11, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'G1': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 1},
      'G2': {'LIBERTY': 8, 'MOVABLE': 6, 'STABLE': 0, 'X': 1, 'C': 0},
      'B3': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'C3': {'LIBERTY': 6, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'B4': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 10, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'A5': {'LIBERTY': 13, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 8, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'A6': {'LIBERTY': 12, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'B6': {'LIBERTY': 8, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'C6': {'LIBERTY': 4, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'C7': {'LIBERTY': 10, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 12, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'E7': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0}
   }
}
```

Best Move: C6

Jev Move: C6

---

- Move: 11

```python
{
   'MOVABLE_POS': ['G1', 'G2', 'B3', 'C3', 'G3', 'A4', 'B4', 'G4', 'A5', 'G5', 'B6', 'F6', 'C7', 'D7', 'E7', 'G8'],
   'INFO': {
      'G1': {'LIBERTY': 7, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 1},
      'G2': {'LIBERTY': 8, 'MOVABLE': 6, 'STABLE': 0, 'X': 1, 'C': 0},
      'B3': {'LIBERTY': 11, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'C3': {'LIBERTY': 10, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'A4': {'LIBERTY': 8, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'B4': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 10, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'A5': {'LIBERTY': 10, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 9, 'MOVABLE': 9, 'STABLE': 0, 'X': 0, 'C': 0},
      'B6': {'LIBERTY': 6, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'F6': {'LIBERTY': 8, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'C7': {'LIBERTY': 8, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'E7': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'G8': {'LIBERTY': 12, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 1}
   }
}
```

Best Move: B6

Jev Move: B6

---

- Move: 12

```python
{
   'MOVABLE_POS': ['G1', 'G2', 'B3', 'C3', 'G3', 'A4', 'G4', 'A5', 'G5', 'F6', 'C7', 'D7', 'E7', 'G8'], 
   'INFO': {
      'G1': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 1},
      'G2': {'LIBERTY': 8, 'MOVABLE': 8, 'STABLE': 0, 'X': 1, 'C': 0},
      'B3': {'LIBERTY': 16, 'MOVABLE': 11, 'STABLE': 0, 'X': 0, 'C': 0},
      'C3': {'LIBERTY': 6, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 12, 'STABLE': 0, 'X': 0, 'C': 0},
      'A4': {'LIBERTY': 11, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 10, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'A5': {'LIBERTY': 4, 'MOVABLE': 4, 'STABLE': 0, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 9, 'MOVABLE': 10, 'STABLE': 0, 'X': 0, 'C': 0},
      'F6': {'LIBERTY': 8, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'C7': {'LIBERTY': 7, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'E7': {'LIBERTY': 7, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'G8': {'LIBERTY': 12, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 1}
   }
}
```

Best Move: A5

Jev Move: A5

---

- Move: 13

```python
{
   'MOVABLE_POS': ['G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'A7', 'B7', 'C7', 'D7', 'E7', 'G8'],
   'INFO': {
      'G1': {'LIBERTY': 7, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 1},
      'G2': {'LIBERTY': 8, 'MOVABLE': 5, 'STABLE': 0, 'X': 1, 'C': 0},
      'A3': {'LIBERTY': 7, 'MOVABLE': 2, 'STABLE': 0, 'X': 0, 'C': 0},
      'B3': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'C3': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'A4': {'LIBERTY': 7, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 10, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'A7': {'LIBERTY': 6, 'MOVABLE': 1, 'STABLE': 0, 'X': 0, 'C': 1},
      'B7': {'LIBERTY': 7, 'MOVABLE': 6, 'STABLE': 0, 'X': 1, 'C': 0},
      'C7': {'LIBERTY': 11, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 7, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'E7': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'G8': {'LIBERTY': 12, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 1}
   }
}
```

Best Move: A7 -> A3(Cにペナルティを与えたため。しかしA7は単独Cではなくこの局面の最善でもある)

Jev Move: A3(一旦、正解とする)

---

- Move: 14

```python
{
   'MOVABLE_POS': ['F1', 'G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'F6', 'C7', 'D7', 'E7', 'A8', 'C8', 'G8'],
   'INFO': {
      'F1': {'LIBERTY': 6, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 1},
      'G1': {'LIBERTY': 7, 'MOVABLE': 2, 'STABLE': 0, 'X': 0, 'C': 2},
      'G2': {'LIBERTY': 8, 'MOVABLE': 4, 'STABLE': 0, 'X': 1, 'C': 1},
      'A3': {'LIBERTY': 7, 'MOVABLE': 2, 'STABLE': 0, 'X': 0, 'C': 1},
      'B3': {'LIBERTY': 9, 'MOVABLE': 4, 'STABLE': 0, 'X': 0, 'C': 1},
      'C3': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 1},
      'G3': {'LIBERTY': 12, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 1},
      'A4': {'LIBERTY': 7, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 1},
      'G4': {'LIBERTY': 10, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 1},
      'G5': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 1},
      'F6': {'LIBERTY': 11, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 1},
      'C7': {'LIBERTY': 10, 'MOVABLE': 5, 'STABLE': 0, 'X': 1, 'C': 1},
      'D7': {'LIBERTY': 7, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 1},
      'E7': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 1},
      'A8': {'LIBERTY': 6, 'MOVABLE': 3, 'STABLE': 4, 'X': 0, 'C': 0},
      'C8': {'LIBERTY': 7, 'MOVABLE': 2, 'STABLE': 0, 'X': 1, 'C': 1},
      'G8': {'LIBERTY': 12, 'MOVABLE': 4, 'STABLE': 0, 'X': 0, 'C': 2}
   }
}
```

Best Move: A8(実はCを解消しているため、現在のプロンプトではこれしか候補に残らない)

Jev Move: A8

---

- Move: 15

```python
{
   'MOVABLE_POS': ['F1', 'G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'F6', 'C7', 'E7', 'D8', 'G8'],
   'INFO': {
      'F1': {'LIBERTY': 6, 'MOVABLE': 4, 'STABLE': 4, 'X': 0, 'C': 0},
      'G1': {'LIBERTY': 7, 'MOVABLE': 3, 'STABLE': 4, 'X': 0, 'C': 1},
      'G2': {'LIBERTY': 8, 'MOVABLE': 5, 'STABLE': 4, 'X': 1, 'C': 0},
      'A3': {'LIBERTY': 7, 'MOVABLE': 3, 'STABLE': 4, 'X': 0, 'C': 0},
      'B3': {'LIBERTY': 14, 'MOVABLE': 6, 'STABLE': 4, 'X': 0, 'C': 0},
      'C3': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 4, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 8, 'STABLE': 4, 'X': 0, 'C': 0},
      'A4': {'LIBERTY': 7, 'MOVABLE': 4, 'STABLE': 5, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 10, 'MOVABLE': 7, 'STABLE': 4, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 4, 'X': 0, 'C': 0},
      'F6': {'LIBERTY': 8, 'MOVABLE': 3, 'STABLE': 4, 'X': 0, 'C': 0},
      'C7': {'LIBERTY': 4, 'MOVABLE': 3, 'STABLE': 4, 'X': 0, 'C': 0},
      'E7': {'LIBERTY': 6, 'MOVABLE': 5, 'STABLE': 4, 'X': 0, 'C': 0},
      'D8': {'LIBERTY': 10, 'MOVABLE': 5, 'STABLE': 4, 'X': 0, 'C': 0},
      'G8': {'LIBERTY': 11, 'MOVABLE': 4, 'STABLE': 4, 'X': 0, 'C': 1}
   }
}
```

Best Move: C7

Jev Move: C7

---

## Jev Prompt: 3

- 次の処理を順に行い、候補を選択する。
- なお、数値を比較せずに候補を選択しないこと。
- (1)INFO内の全候補を対象とする。
- (2)その候補の内、Xの値が最小の候補だけを残す。
- (3)その候補の内、Cの値が最小の候補だけを残す。
- (4)その候補の内、LIBERTYの値が最小の候補だけを残す。
- (5)その候補の内、MOVABLEの値が最小の候補だけを残す。
- (6)その候補の内、STABLEの値が最大の候補を残す。
- (7)この時点で候補が複数残っている場合はランダムに候補を選ぶ。

### 対局結果

```
JevPlayer : Wins = 44, MonteCarloPlayer : Wins = 4,
MonteCarloPlayer : Wins = 7, JevPlayer : Wins = 42,
```

### GUIで対戦した感想

- 単独C以外のC(確定石を除く)にペナルティを与えている影響が強く、悪手側に着手している
   - 一瞬だけ変更してみたが、双方Cに対して自分から当てるため、逆に致命的な悪手が増えた
- 挙動がおかしいことがある
   - X打ち以外がある局面でのX打ち
   - D3C5の後、C6と打とうとする。開放度理論から明らかにD6が最善

```python
{
   'MOVABLE_POS': ['B6', 'C6', 'D6', 'E6', 'F6'],
   'INFO': {
      'B6': {'LIBERTY': 12, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'C6': {'LIBERTY': 9, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 0},
      'D6': {'LIBERTY': 8, 'MOVABLE': 4, 'STABLE': 0, 'X': 0, 'C': 0},
      'E6': {'LIBERTY': 10, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'F6': {'LIBERTY': 11, 'MOVABLE': 4, 'STABLE': 0, 'X': 0, 'C': 0}
   }
}
```

## Jev Prompt: 4

- 次の処理を順に行い、候補を選択する。
- なお、数値を比較せずに候補を選択しないこと。
- (1)INFO内の全候補を対象とする。
- (2)その候補の内、Xの値が最小の候補だけを残す。
- (3)その候補の内、Cの値が最小の候補だけを残す。
- (4)その候補の内、LIBERTYの値が最小の候補だけを残す。
- (5)その候補の内、MOVABLEの値が最小の候補だけを残す。
- (6)その候補の内、STABLEの値が最大の候補を残す。
- (7)最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。

※(7)だけランダムに選ぶ候補から曖昧さを軽減(できているかを評価することが難しい)

## Jev Prompt: 5

- 次の処理を順に行い、候補を選択する。
- なお、数値を比較せずに候補を選択しないこと。
- (1)INFO内の全候補を対象とする。
- (2)その候補の内、Xの値がMIN_Xの候補だけを残す。
- (3)その候補の内、Cの値がMIN_Cの候補だけを残す。
- (4)その候補の内、LIBERTYの値がMIN_LIBERTYの候補だけを残す。
- (5)その候補の内、MOVABLEの値がMIN_MOVABLEの候補だけを残す。
- (6)その候補の内、STABLEの値がMAX_STABLEの候補だけを残す。
- (7)最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。

### テスト

- D3C5

```python
{
   'MOVABLE_POS': ['B6', 'C6', 'D6', 'E6', 'F6'],
   'INFO': {
      'B6': {'X': 0, 'C': 0, 'LIBERTY': 12, 'MOVABLE': 5, 'STABLE': 0},
      'C6': {'X': 0, 'C': 0, 'LIBERTY': 9, 'MOVABLE': 3, 'STABLE': 0},
      'D6': {'X': 0, 'C': 0, 'LIBERTY': 8, 'MOVABLE': 4, 'STABLE': 0},
      'E6': {'X': 0, 'C': 0, 'LIBERTY': 10, 'MOVABLE': 5, 'STABLE': 0},
      'F6': {'X': 0, 'C': 0, 'LIBERTY': 11, 'MOVABLE': 4, 'STABLE': 0}
   },
   'MIN_X': 0, 'MIN_C': 0, 'MIN_LIBERTY': 8, 'MIN_MOVABLE': 3, 'MAX_STABLE': 0
}
```

Best Move: D6

Jev Move: D6

### 欠陥

- このプロンプトは候補が除外されるたびに再計算が必要
- その再計算はLLM(Jev)側で行うため、干渉できない

## Jev Prompt: 6

- 次の処理を順に行い、候補を選択する。
- なお、数値を比較せずに候補を選択しないこと。
- (1)INFO内の全候補を対象とする。
- (2)その候補の内、Xの値が最小の候補だけを残す。
- (3)その候補の内、Cの値が最小の候補だけを残す。
- (4)その候補の内、STABLEの値が最大の候補を残す。
- (5)その候補の内、LIBERTYの値が最小の候補だけを残す。
- (6)その候補の内、MOVABLEの値が最小の候補だけを残す。
- (7)最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。

### 変更点

1. 確定石優先
2. ブロックとウィングから伸びるC(いわゆる余裕手)はペナルティの対象外

### テスト

- 所感: 意外と良いのでは？
   - 伸びるCを打てるようにしたことで戦略が広がった印象

### 対局結果

```
RandomPlayer : Wins = 1, JevPlayer : Wins = 49
JevPlayer : Wins = 47, RandomPlayer : Wins = 3
MonteCarloPlayer : Wins = 8, JevPlayer : Wins = 42
JevPlayer : Wins = 40, MonteCarloPlayer : Wins = 9
```

- 勝率下がってる ?

## Jev Prompt: 7

- 次の処理を順に行い、候補を選択する。
- なお、数値を比較せずに候補を選択しないこと。
- (1)INFO内の全候補を対象とする。
- (2)その候補の内、Xの値が最小の候補だけを残す。
- (3)その候補の内、Cの値が最小の候補だけを残す。
- (4)その候補の内、LIBERTYの値が最小の候補だけを残す。
- (5)その候補の内、MOVABLEの値が最小の候補だけを残す。
- (6)その候補の内、STABLEの値が最大の候補を残す。
- (7)最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。

### 変更点

- 確定石の優先順位を元に戻す
- この後、JevCloneを作成する

### 対局結果

```
RandomPlayer : Wins = 3, JevPlayer : Wins = 47
JevPlayer : Wins = 47, RandomPlayer : Wins = 3
MonteCarloPlayer : Wins = 6, JevPlayer : Wins = 42
JevPlayer : Wins = 41, MonteCarloPlayer : Wins = 9
```

## JevClone

- Prompt 7を直接実装
- プロンプトの意図通りに動かした時の強さを評価

### テスト

- Move: 13
   - A7 -> A3(A7はCのペナルティが考慮されていないため、仕方ない)

- Move: 17
   - D8 -> D8(乱数の結果。ハイパー偶数は考慮していない)

- Move: 21
   - G8 -> A3(乱数の結果。偶数理論は考慮していない)

- 棋譜(テストの副産物)

```
F5D6C5F4E3B5D3F2C4E2E6F3E1D1D2F7C1C2C6G6B6B4A5A6A7B7A8D7C7E7F6G5D8B8C8E8F8C3A4G8G7A3B3A2B2H4H5A1B1H8F1H6H7G4G3G1H3H2G2H1
```

- 考察
   - プロンプトの指示通りに打てれば、こちらが想定する手に一致することが確認できた
      - 後はLLM(今回はJev)がプロンプトを正しく理解できれば、こちらが想定する手を打つことができる
   
   - 乱数に委ねているのは、今のところ偶数理論の部分だけである
      - 偶数理論はプログラムで高速にカウントすることが難しい
      - 準偶数理論を実装して妥協したとしてプロンプト(の優先順位)も難しい
      - 今は無理に実装せず、乱数に委ねる
   
   - 辺理論が弱いことは明確に弱点
      - Cについて単独C以外をどのように扱うかが重要

### 対局結果

※実験ではPrompt 6のCloneも実装して比較する

- JevClone(Prompt 6)

```
RandomPlayer : Wins = 0, JevClonePlayer : Wins = 50
JevClonePlayer : Wins = 50, RandomPlayer : Wins = 0
MonteCarloPlayer : Wins = 1, JevClonePlayer : Wins = 48
JevClonePlayer : Wins = 47, MonteCarloPlayer : Wins = 3
```

- JevClone(Prompt 7)

```
RandomPlayer : Wins = 1, JevClonePlayer : Wins = 49
JevClonePlayer : Wins = 49, RandomPlayer : Wins = 1
MonteCarloPlayer : Wins = 1, JevClonePlayer : Wins = 49
JevClonePlayer : Wins = 44, MonteCarloPlayer : Wins = 6
```

### 比較結果

|プロンプトの種類|Random|MonteCarlo|棋譜ファイル|
|:---:|:---:|:---:|:---:|
|Prompt 6|96勝4敗0引(96%)|82勝17敗1引(82%)|reversi_history_P6.txt|
|Prompt 7|94勝6敗0引(94%)|83勝15敗2引(83%)|reversi_history_P7.txt|
|JevClone(Prompt 6)|100勝0敗0引(100%)|95勝4敗1引(95%)|reversi_history_CP6.txt|
|JevClone(Prompt 7)|98勝2敗0引(98%)|93勝7敗0引(93%)|reversi_history_CP7.txt|

### 考察

- JevCloneもRandomに負けることがあるため、評価関数の改善は必要
- どちらのプロンプトも黒番が苦手傾向
- Prompt 7はMCに対して全滅負けが多い
- Prompt 6のように確定石(隅)を優先する方が勝率が良い
- この結果を元に、Prompt 6を対人戦による評価の対象にする

### 対人戦による評価

|対局相手|対局結果|棋譜ファイル|
|:---:|:---:|:---:|
|学生|7勝2敗1引(70%)|evaluate_students.txt|
|自分|0勝10敗0引(0%)|evaluate_me.txt|

- 謝辞
   - 本実験にご協力いただいた学生に、深く感謝する

### Jevの指し手をLLM(Gemini)が解説

- Input

```
リバーシの次の局面を考えます。

   A B C D E F G H
------------------
1|□□●●●□□□
2|□□○○○○□□
3|□□□○●○□□
4|□○○●○○□□
5|●○●●●○□□
6|○○○○○□○□
7|□□□□□○□□
8|□□□□□□□□
Next Moves: ['G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'A7', 'B7', 'C7', 'D7', 'E7', 'G8']

この局面に対し、Jev(LLMのように自然言語のプロンプトを入力できる)に次のプロンプトを入力しました。

# Prompt Start
{
   'MOVABLE_POS': ['G1', 'G2', 'A3', 'B3', 'C3', 'G3', 'A4', 'G4', 'G5', 'A7', 'B7', 'C7', 'D7', 'E7', 'G8'],
   'INFO': {
      'G1': {'LIBERTY': 7, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 1},
      'G2': {'LIBERTY': 8, 'MOVABLE': 5, 'STABLE': 0, 'X': 1, 'C': 0},
      'A3': {'LIBERTY': 7, 'MOVABLE': 2, 'STABLE': 0, 'X': 0, 'C': 0},
      'B3': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'C3': {'LIBERTY': 9, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 0},
      'G3': {'LIBERTY': 12, 'MOVABLE': 8, 'STABLE': 0, 'X': 0, 'C': 0},
      'A4': {'LIBERTY': 7, 'MOVABLE': 3, 'STABLE': 0, 'X': 0, 'C': 0},
      'G4': {'LIBERTY': 10, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'G5': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'A7': {'LIBERTY': 6, 'MOVABLE': 1, 'STABLE': 0, 'X': 0, 'C': 1},
      'B7': {'LIBERTY': 7, 'MOVABLE': 6, 'STABLE': 0, 'X': 1, 'C': 0},
      'C7': {'LIBERTY': 11, 'MOVABLE': 7, 'STABLE': 0, 'X': 0, 'C': 0},
      'D7': {'LIBERTY': 7, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'E7': {'LIBERTY': 9, 'MOVABLE': 6, 'STABLE': 0, 'X': 0, 'C': 0},
      'G8': {'LIBERTY': 12, 'MOVABLE': 5, 'STABLE': 0, 'X': 0, 'C': 1}
   }
}
- 次の処理を順に行い、候補を選択する。
- なお、数値を比較せずに候補を選択しないこと。
- (1)INFO内の全候補を対象とする。
- (2)その候補の内、Xの値が最小の候補だけを残す。
- (3)その候補の内、Cの値が最小の候補だけを残す。
- (4)その候補の内、STABLEの値が最大の候補を残す。
- (5)その候補の内、LIBERTYの値が最小の候補だけを残す。
- (6)その候補の内、MOVABLEの値が最小の候補だけを残す。
- (7)最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。
# Prompt End

その結果、A3が選択されました。このAIの思考を解説してください。
```

- Output

```
提示されたプロンプトの条件（1）〜（6）を順番に適応して候補を絞り込んでいく過程をたどることで、なぜ最終的に **A3** が選ばれたのかを解説します。

---

### 絞り込みのステップ解説

#### **(1) INFO内の全候補を対象とする**

初期状態での候補（全15箇所）：
`G1`, `G2`, `A3`, `B3`, `C3`, `G3`, `A4`, `G4`, `G5`, `A7`, `B7`, `C7`, `D7`, `E7`, `G8`

---

#### **(2) Xの値が最小の候補だけを残す**

各候補の `X` の値を確認します。

* `X = 1` : `G2`, `B7`
* `X = 0` : それ以外のすべて (`G1`, `A3`, `B3`, `C3`, `G3`, `A4`, `G4`, `G5`, `A7`, `C7`, `D7`, `E7`, `G8`)

**残る候補（13箇所）：**
`G1`, `A3`, `B3`, `C3`, `G3`, `A4`, `G4`, `G5`, `A7`, `C7`, `D7`, `E7`, `G8`

---

#### **(3) Cの値が最小の候補だけを残す**

残った候補の中で `C` の値を確認します（最小値は `0`）。

* `C = 1` : `G1`, `A7`, `G8`（脱落）
* `C = 0` : `A3`, `B3`, `C3`, `G3`, `A4`, `G4`, `G5`, `C7`, `D7`, `E7`

**残る候補（10箇所）：**
`A3`, `B3`, `C3`, `G3`, `A4`, `G4`, `G5`, `C7`, `D7`, `E7`

---

#### **(4) STABLEの値が最大の候補を残す**

残ったすべての候補において `STABLE` はすべて `0` です。
最大値は `0` となるため、**全員がそのまま残ります**。

**残る候補（10箇所）：**
`A3`, `B3`, `C3`, `G3`, `A4`, `G4`, `G5`, `C7`, `D7`, `E7`

---

#### **(5) LIBERTYの値が最小の候補だけを残す**

残った10箇所の `LIBERTY` の値を比較します。

* `A3`: **6**
* `A4`: 7
* `D7`: 7
* `B3`: 9
* `C3`: 9
* `G5`: 9
* `E7`: 9
* `G4`: 10
* `C7`: 11
* `G3`: 12

最小値は **`6`**（`A3`）となります。そのため、`LIBERTY` が 7 以上の候補がすべて脱落します。

**残る候補（1箇所）：**
`A3`

---

#### **(6)・(7) 絞り込みの完了**

ステップ(5)の時点で候補が **`A3` の1つのみ**に絞り込まれたため、ステップ(6)および(7)を実行するまでもなく、最終的な選択として **`A3`** が決定しました。

---

### まとめ

AI（Jev）はプロンプトの評価基準（Xの回避 → Cの回避 → STABLE最大化 → LIBERTY最小化）に厳密に従い、**「危険なマス（XやC）を避けつつ、開放度（LIBERTY＝相手に与える選択肢や影響範囲の少なさ）が最小となる『A3』」** を最も価値の高い手として算出し、選択しました。
```

- 考察
   - まとめで「危険なマス」や「開放度」等のオセロの専門用語を使用して説明できている点が高く評価できる。

### 棋譜解析

To be continued

## 最終更新

2026年10月29日
