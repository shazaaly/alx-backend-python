from unittest.mock import patch, PropertyMock
import unittest

class MyTestCase(unittest.TestCase):
    def test_my_property(self):
        with patch.object(MyClass, 'my_property', new_callable=PropertyMock) as mock_property:
            mock_property.return_value = 'mocked value'
            
            instance = MyClass()
            self.assertEqual(instance.my_property, 'mocked value')

if __name__ == '__main__':
    unittest.main()
