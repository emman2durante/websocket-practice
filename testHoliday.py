from test import Holiday
import datetime

class TestHoliday:
    def test_get_theme_returns_christmas(self):
        n = Holiday()
        date_now = datetime.datetime(2019, 12 ,25)
        
        result = n.get_theme()

        print(result)
        assert result == "Christmas"
    
    def test_get_theme_returns_not_christmas(self):
        n = Holiday()
        n.date_now = datetime.datetime(2019, 11, 18)

        result = n.get_theme()

        print(result)
        assert result == "Not Christmas"


t = TestHoliday()
print('Test 1:')
print(t.test_get_theme_returns_christmas())
print('Test 2:')
print(t.test_get_theme_returns_not_christmas())

