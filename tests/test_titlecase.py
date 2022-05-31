from titlecase import title_case #importing logic will put under test, hence unit test!

class TitleCaseTests:

    def test_some_text_is_uppercased(self):
        initial_text = 'this should all be capitalized'
        expected_text = 'This Should All Be Capitalized'

        returned_text = title_case(initial_text)
        assert returned_text == expected_text