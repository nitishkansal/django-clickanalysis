from clickanalysis.models import Campaign, ClickTracking
from django.http import HttpResponseRedirect


class ClickAnalysisMiddleware(object):
    """This middleware is the core logic for tracking all the clicks across the site
       We have already added campaign ids to the links which we want to track
       and this class will isolate that campaign id, if campaign id is valid, click will be
       recorded to the related campaign.
    """

    def process_request(self, request):
        if request.GET.get('cid', ''):  # Will process the logic only if campaign id is present
            try:
                campaign = Campaign.objects.get(campaign_id=request.GET['cid'])
            except:
                campaign = None

            # Clearing the cid parameter from the link or providing a clean url for user to redirect
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

            if campaign:  # If campaign was found then here the click will be recorded
                click, created = ClickTracking.objects.get_or_create(campaign=campaign, link=url)
                if created:
                    click.count = 1
                else:
                    click.count += 1
                click.save()

            return HttpResponseRedirect(url)
