from django.core.management.base import BaseCommand
from zetteldb.models import Zettel, ZettelThread

import os

from parsec import *

class Command(BaseCommand):
  help = 'parses Markdown notes and adds them to the Zettelkasten database.'

  def add_arguments(self, parser):
    parser.add_argument('dir')

  def handle(self, *args, **options):
    mdpar = many(letter() | one_of("-_+") | digit()) << string(".md")
  
    for root, dirs, files in os.walk(options['dir']):

      for fn in files:
        try:
          fid = ''.join(mdpar.parse(fn))
          
          if fid == 'index':
            fid = os.path.basename(os.path.normpath(root))
        except ParseError:
          continue
        
        with open(os.path.join(root, fn)) as f:
          text = f.read()
      
        self._parse_zettel_thread(fid, text)

  def _parse_zettel_thread(self, fid, text):
      
    text_blocks = text.split("\n\n")
      
    header = many1(string("#")) + many(none_of("\n"))
      
    thread_title = ''.join(header.parse(text_blocks[0])[1]).strip()
        
    header_stack = [(1, thread_title)]

    try:
      tho = ZettelThread.objects.get(fid=fid)
      tho.delete()
    except ZettelThread.DoesNotExist:
      pass      
    
    thread_obj = ZettelThread(fid=fid, title=thread_title)
    thread_obj.save()
    
    ct = 0
    
    for block in text_blocks:
      try:
        (l, t) = header.parse(block)
        lvl = len(l)
        
        title = ''.join(t).strip()
        while ( (not header_stack) and lvl <= header_stack[-1][0]):
          header_stack.pop()
        header_stack.append((lvl, title))
        
      except ParseError:
        pass
        
      zettel = thread_obj.zettel_set.create(zid=ct,
                                            full_id= fid + '#{0:03d}'.format(ct),
                                            title=header_stack[-1][1],
                                            content=block)
      ct += 1
      thread_obj.zettels.add(zettel)

  def _parse_metadata(self, first_block):
    pass
