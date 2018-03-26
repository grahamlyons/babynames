from lxml import html

class Parser(object):

    MALE_NAME_INDEX = 2
    MALE_COUNT_INDEX = 3

    def __init__(self, data):
        self.document = html.fromstring(data)

    def get_male_counts(self):
        names = self._xpath(self.MALE_NAME_INDEX)
        counts = self._xpath(self.MALE_COUNT_INDEX)
        counts = [int(i.replace(",", "")) for i in counts]
        return dict(zip(names, counts))

    def _xpath(self, index):
        elements = self.document.xpath(
            "/html/body/table//table/tr/td[{}]".format(index)
        )
        return [e.text for e in elements]
