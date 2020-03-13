# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser
import codecs

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print("Encountered comment: ", data)
    pos = self.getpos()
    print("\tAt line: ", pos[0]," position ", pos[1])

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = codecs.open("samplehtml.html", 'r', 'utf-8')
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)

if __name__ == "__main__":
  main();
  