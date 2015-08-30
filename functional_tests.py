from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # she is invited to enter a to-do list straight away

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item'
        )

        # she type "buy Something" into a text box when she hits enter
        input.send_keys('Buy peacock feathers')

        # the page updates, and now the page lists
        # "1. buy something"
        inputbox.send_keys(Keys.ENTER)

        table = self.broswer.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        # there is still a text box inviting her to add another. She
        # enters " use purchased item"
        self.fail('Finish the test')

# the page updates again, and now both items are on her list
# The site generated a unique URL for her -- there is text explaining tthe URL
# She visits the URL - her To-Do lost is still there.
#
if __name__ == '__main__':
    unittest.main()
