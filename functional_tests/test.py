#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

#import unittest

class NewVisitorTest(StaticLiveServerTestCase):
	
	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url	
	
	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()	

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
        # online to-do list
		self.browser.get(self.server_url)

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

		self.check_for_row_in_list_table('1: Buy peacock feathers')

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url



# the page updates again, and now both items are on her list
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: use peacock feathers to make a fly')

## Now a new user, Francis, come along to the site.
## of Edith's is coming through from cookies etc.

		self.browser.quit()
		self.browser = webdriver.Firefox()

# Francis visits the home page. There is no sign of Edith's
# list.
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly',page_text)

# Francis starts a new list by entering a new item, He
# is less interesting than Edith...

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy Milk')
		inputbox.send_keys(Keys.ENTER)

# Francis get his own unique URL

		francis_list_url = self.browser.current_url

		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

# Again, there is no trace of Edith's list

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy Milk', page_text)

#satified, they both go back to sleep

# Edith goes to the home page
	def test_layout_and_styling(self):
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024, 768)

# She notices the input box is nicely centered
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] /2,
			512, delta=5)

# She sterts a new list and sees the input is nicely centered there too
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] /2,
			512, delta=5
			)
        #self.fail('Finish the test')
# She visits the URL - her To-Do list is still there.
#
#if __name__ == '__main__':
#    unittest.main()
