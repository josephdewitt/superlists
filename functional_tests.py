from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest( unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(rwo_text, [row.text for row in rows)

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
        inputbox.send_keys('Buy peacock feathers')

        # the page updates, and now the page lists
        # "1. buy something"
        inputbox.send_keys(Keys.ENTER)

        check_for_row_in_list_table(1: Buy peacock feathers)

#        table = self.browser.find_element_by_id('id_list_table')
#        rows = table.find_elements_by_tag_name('tr')
#
#        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
#
#        self.assertTrue(
#            any(row.text == '1: Buy peacock feathers' for row in rows),
#            "New to-do item did not appear in table -- its text was:\n%s" % (table.text,
#            )
#        )
        # there is still a text box inviting her to add another. She
        # enters " use peacock feathers to make a fly"

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)



# the page updates again, and now both items are on her list

        check_for_row_in_list_table('1: Buy peacock feathers')
        check_for_row_in_list_table('2: use peacock feathers to make a fly')

#        self.assertIn('1. Buy peacock feathers', [row.text for row in rows])
#        self.assertIn('2: use peacock feathers to make a fly' , [row.text for row in rows])

# The site generated a unique URL for her -- there is text explaining tthe URL

        self.fail('Finish the test')
# She visits the URL - her To-Do lost is still there.
#
if __name__ == '__main__':
    unittest.main()
