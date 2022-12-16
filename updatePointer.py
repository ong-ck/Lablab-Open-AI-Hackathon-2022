def updatePointer():
  with open("/home/runner/Lablab-Open-AI-Hackathon-2022/pointer.txt") as fin:
    lines = fin.read()
  newLine = (int(lines) + 1) % 9
  with open("/home/runner/Lablab-Open-AI-Hackathon-2022/pointer.txt", 'r+') as fin:
      fin.write(str(newLine))

def getPointer():
  with open("/home/runner/Lablab-Open-AI-Hackathon-2022/pointer.txt") as fin:
    lines = fin.read()
  return int(lines)