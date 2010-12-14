from unittest import TestCase
from django.test.client import Client

class TestTemplateStub(TestCase):
    
    def setUp(self):
        self.browser = Client()
    
    def test_should_response_ok(self):
        response = self.browser.get('/templatestub/?t=teste.html')
        self.assertEquals( 200, response.status_code )
        
    def test_should_response_ok_when_template_loads_invalid_tag(self):
        response = self.browser.get('/templatestub/?t=load.html')
        self.assertEquals( 200, response.status_code )

    def test_should_response_ok_when_replace_tag(self):
        response = self.browser.get('/templatestub/?t=tag.html&tt=my_tag')
        self.assertEquals( 200, response.status_code )    
        
    def test_should_response_value_when_replace_tag_with_this_value(self):
        response = self.browser.get('/templatestub/?t=tag.html&tt=my_tag:my_value')
        self.assertEquals( 'my_value', response.content )
        
    def test_should_response_values_when_replace_more_than_one_tag_with_values(self):
        response = self.browser.get('/templatestub/?t=tags.html&tt=my_tag1:my_value1&tt=my_tag2:my_value2')
        self.assertEquals( 'my_value1\nmy_value2', response.content )
                
    def test_should_response_ok_when_replace_filter(self):
        response = self.browser.get('/templatestub/?t=filter.html&f=my_filter')
        self.assertEquals( 200, response.status_code )          

    def test_should_response_ok_when_replace_filter_that_uses_param(self):
        response = self.browser.get('/templatestub/?t=filter_with_param.html&f=my_filter')
        self.assertEquals( 200, response.status_code )                   

    def test_should_response_value_when_replace_filter_with_this_value(self):
        response = self.browser.get('/templatestub/?t=filter.html&f=my_filter:filters_value')
        self.assertEquals( 'filters_value', response.content )            
        
    def test_should_response_value_when_replace_filter_that_uses_param_with_this_value(self):
        response = self.browser.get('/templatestub/?t=filter_with_param.html&f=my_filter:filters_value')
        self.assertEquals( 'filters_value', response.content )            
                
    def test_should_response_values_when_replace_more_than_one_filter_with_values(self):
        response = self.browser.get('/templatestub/?t=filters.html&f=my_filter1:filters_value1&f=my_filter2:filters_value2')
        self.assertEquals( 'filters_value1\nfilters_value2', response.content )            

    def test_should_put_the_json_context_in_template(self):
        response = self.browser.get('/templatestub/?t=context.html&c={"person":{"name":"my_name"}}')
        self.assertEquals( 'my_name', response.content )

    def test_should_put_the_json_context_in_template_with_array(self):
        response = self.browser.get('/templatestub/?t=context_with_array.html&c={"people":[{"name":"my_name"},{"name":"other_name"}]}')
        self.assertEquals( 'my_nameother_name', response.content )

                