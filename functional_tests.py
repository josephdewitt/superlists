from selenium import webdriver
import unittest

class NewVisitorTest( unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # online to-do list
        self.browser.get('http://josephdewitt8.pythonanywhere.com')
        # the pape title and header mention to-to list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# she is invited to enter a to-do list straight away
# she type "buy Something" into a text box when she hits enter
# the page updates, and now the page lists
# "1. buy something"
# there is still a text box inviting her to add another. She
# enters " use purchased item"
# the page updates again, and now both items are on her list
# The site generated a unique URL for her -- there is text explaining tthe URL
# She visits the URL - her To-Do lost is still there.
#
if __name__ == '__main__':
    unittest.main()
