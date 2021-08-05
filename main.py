import time
from sys import argv
import instaloader
from instaloader import Profile, Post

instance = instaloader.Instaloader()

if __name__ == '__main__':
    instance.login(user=argv[1], passwd=argv[2])
    profile = Profile.from_username(instance.context, username="jannatkhah.ir")

    for highlight in instance.get_highlights(user=profile):
        # highlight is a Highlight object
        for item in highlight.get_items():
            # item is a StoryItem object
            flag = 0
            while flag == 0:
                try:
                    instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
                    flag = 1
                except:
                    time.sleep(5)
                    continue
