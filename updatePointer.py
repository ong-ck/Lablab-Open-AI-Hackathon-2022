def updatePointer():
  with open("/home/runner/Streamlit-Test/pointer.txt") as fin:
    lines = fin.read()
  newLine = (int(lines) + 1) % 9
  with open("/home/runner/Streamlit-Test/pointer.txt", 'r+') as fin:
      fin.write(str(newLine))

def getPointer():
  with open("/home/runner/Streamlit-Test/pointer.txt") as fin:
    lines = fin.read()
  return int(lines)