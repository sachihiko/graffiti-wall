import json, os
import unittest

class TestTags(unittest.TestCase):

    def setUp(self):
        self.directory = os.path.join(os.path.dirname(__file__), './tags')
        self.tag_file_names = os.listdir(self.directory)

    def tag_name_test(self, tag):
        name = tag.get('name')

        self.assertIsNotNone(name)
        self.assertIs(type(name), str)
        self.assertTrue(len(name) > 0)

    def tag_color_test(self, tag):
        color = tag.get('color')

        self.assertIsNotNone(color)
        self.assertIs(type(color), str)
        self.assertTrue(len(color) > 0)

    def tag_grid_test(self, tag):
        grid = tag.get('grid')

        self.assertIsNotNone(grid)
        self.assertIs(type(grid), list)
        self.assertEqual(len(grid), 7)

        for row in grid:
            self.assertEqual(len(row), 7)

    def tag_test(self, tag):
        file_name = (os.path.join(self.directory, tag))
        self.assertTrue(file_name.endswith('.json'))

        with open(file_name, 'r') as f:
            try:
                tag_obj = json.load(f)
            except ValueError:
                self.fail(
                    (('The tag "{tag}" at "{file_name}" can\'t be decoded as JSON!'
                    ' Double check your JSON file structure.')).format(tag=tag,file_name=file_name)
                )

            self.assertIsNotNone(tag_obj)
            self.assertIs(type(tag_obj), dict)

            self.tag_name_test(tag_obj)
            self.tag_color_test(tag_obj)
            self.tag_grid_test(tag_obj)

    def test_tags(self):
        for tag in self.tag_file_names:
            self.tag_test(tag)

if __name__ == '__main__':
    unittest.main()
