from clickanalysis.models import Campaign, ClickTracking
from django.http import HttpResponseRedirect

class ClickAnalysisMiddleware(object):
    def process_request(self, request):
        if request.GET.get('cid', ''):
            try:
                campaign = Campaign.objects.get(campaign_id=request.GET['cid'])
            except:
                campaign = None

            get_params = request.get_full_path().split('?')[1].split('&')
            params_to_send = []
            for g_p in get_params:
                name = g_p.split('=')[0]
                if name != 'cid':
                    params_to_send.append(g_p)

            params = '&'.join(params_to_send)
            if params_to_send:
                url = request.get_full_path().split('?')[0] + '?' + params
            else:
                url = request.get_full_path().split('?')[0]

            if campaign:
                click, created = ClickTracking.objects.get_or_create(campaign=campaign, link=url)
                if created:
                    click.count = 1
                else:
                    click.count += 1
                click.save()

            return HttpResponseRedirect(url)
