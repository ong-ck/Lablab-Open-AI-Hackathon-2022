def updateScore():
  with open("/home/runner/Streamlit-Test/score.txt") as fin:
    lines = fin.read()
  newLine = int(lines) + 1
  with open("/home/runner/Streamlit-Test/score.txt", 'r+') as fin:
      fin.write(str(newLine))

def printScore():
  with open("/home/runner/Streamlit-Test/score.txt") as fin:
      lines = fin.read()
  print("Score: ", lines)
  return lines

def resetScore():
  with open("/home/runner/Streamlit-Test/score.txt", 'r+') as fin:
      fin.truncate(0)
      fin.write("0")
  with open("/home/runner/Streamlit-Test/score.txt") as fin:
    lines = fin.read()
  print("Score reset to ", lines)