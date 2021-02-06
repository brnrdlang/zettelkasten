from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

import markdown as md

from .models import Zettel, ZettelThread
# Create your views here.

def index(request):
  return HttpResponse("Hello, world. There should be zettels here.")
  
def zettel(request, fid, zid):
  zettel = get_object_or_404(Zettel, full_id=fid + '#{0:03d}'.format(zid))

  content = md.markdown(zettel.content)
  context = {'content': content, 'zettel': zettel}
  return render(request, 'zetteldb/zettel.html', context)

def zettel_thread(request, fid):
  thread = get_object_or_404(ZettelThread, fid=fid)
  
  zettels = thread.zettels.all()
  zettels_md = []
  
  for z in zettels:
    zettels_md.append(md.markdown(z.content))
  
  context = {'thread': thread, 'zettels': zettels_md}
  return render(request, 'zetteldb/thread.html', context)
