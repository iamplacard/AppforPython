#Rasie exception 활용
import glob, os.path

def traverse(dir, depth) :
  for obj in glob.glob(dir+'/*'):
    if depth == 0:
      prefix = '|--'
    else :
      prefix = '|'+ ' '*depth + '+--'
    if os.path.isdir(obj):
      print(prefix + os.path.basename(obj) )
      traverse (obj, depth+1)
    elif os.path.isfile(obj) :
      print(prefix + os.path.basename(obj) )
    else:
      raise UnknonObjectError(obj)

if __name__=='__main__' :
  try:
    traverse('.', 0)
  except UnknownObjectError as e:
    print('UnknownObjectError occurs:',e.obj)
  except:
    exc, value, tb = sys.exc_info()
    print(exc, value, tb)
    traceback.print_exc()
