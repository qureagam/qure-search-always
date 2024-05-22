from googlesearch import search


def link(l_value):
   try:
      a = list(search(l_value))
      if a:
        return a
      else:
         pass
   except Exception as r:
       pass