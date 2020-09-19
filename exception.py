class ElementNotFoundException(Exception):
    def __init__(self, item, cause = None):
        super(ElementNotFoundException, self).__init__()
        self.item = item

    def __str__(self):
        return f"The element with By.{self.item[0]} and locator - '{self.item[1]}' was not found"
