import subprocess
import sys
import platform

# OSの種類を調べて、Windows 10じゃなければ、実行できないようにする
if platform.system() != "Windows" and platform.release != "10":
  print("The OS you are using is not Windows 10.")
  sys.exit()

# コマンドライン引数からプロジェクト名を入力してもらう。なければ、もしくは、予約語なら、終了
if sys.argv[1] == "":
  print("The project name must be entered.")
  sys.exit()
elif sys.argv[1] == "{{ project_name }}":
  print("The project name cannot be used.")
  sys.exit()

# 区切り文字がプロジェクト名に入る場合も除去する
if "\\" in sys.argv[1] == True:
  print("The project name cannot be used.")
  sys.exit()

project_name = sys.argv[1]

# コマンドを1行ずつ入れる
tasklist = []

# 結果を一行の文字列にする
result = ""

# ファイル名
filename = "tasklist.txt"

# ファイルを読み込む
with open(filename, "r") as f:
  tasklist = f.readlines()

# 改行コードを削除する
for i, task in enumerate(tasklist):
  task = task.rstrip()
  tasklist[i] = task.replace("{{ project_name }}", project_name)


# 各行のタスクを連結して1行にする
result = " && ".join(tasklist)

# コマンドプロンプト上で実行する
subprocess.call(result, shell=True)
