book={}#dictionary object
book['tom']={
  'name':'tom',
  'address':'ll',
  'phone':999

}
book['bob']={
  'name':'bob',
  'address':'bb',
  'phone':4444
}
import json
s=json.dumps(book)#taking dictionary object and dumping it as string then it is in json format
with open("c://data//book.txt,'w'")as f:
  f.write(s)