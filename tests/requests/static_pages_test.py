from redrover import *


class StaticPagesTest(RedRoverLiveTest):

    subject = page

    @describe
    def the_home_page(self):
        visit('home')
        it.should(have_selector, 'h1', text="Welcome to Django")
