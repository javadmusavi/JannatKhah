import time
from sys import argv
import instaloader
from instaloader import Profile

instance = instaloader.Instaloader()

if __name__ == '__main__':
    instance.login(user=argv[1], passwd=argv[2])
    profile = Profile.from_username(instance.context, username="jannatkhah.ir")

    for highlight in instance.get_highlights(user=profile):
        for item in highlight.get_items():
            flag = 0
            while flag == 0:
                    instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
                    flag = 1

