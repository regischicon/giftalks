from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    def gifmaker(self):
        # Create your tests here.
        ############API GIPHY
        api_instance = giphy_client.DefaultApi()
        api_key = 'U4A5T0UYFd2mIYANkPWOxBZjjuWvATAQ' # str | Giphy API Key.
        tag = self.title # str | Filters results by specified tag. (optional)
        rating = 'g' # str | Filters results by specified rating. (optional)
        fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

        #try:
            # Random Endpoint
        api_response = api_instance.gifs_random_get(api_key, tag=tag, rating=rating, fmt=fmt)
            #pprint(api_response)
        self.title = api_response.data.fixed_height_downsampled_url
        #except ApiException as e:
            #print("Exception when calling DefaultApi->gifs_random_get: %s\n" % e)

        return self.title
        ############API GIPHY
