import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://xn--80adi8aaufcj8j.xn--j1amh/testelex/base/4074/1',
    ]

    def parse(self, response):

        for quote in response.xpath("//*/ul[@class='list-group']//li[@class='list-group-item']/span[@class='label label-info']/text()"):
            print("QQQQQQ", quote.get())
            # li = "//*/ul[@class='list-group']//li[@class='list-group-item']"
            # for text in quote.xpath("//li[@class='list-group-item']"):
            #     print("TTTTTTTTTTTTTTTTTTTT", text)


            yield {
                    'text': quote.get(),
                }

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)




        worked_h4_xpath = "//*/div[@class='container']/h4/text()"
        worked_questions_xpath_without_percent = "//*/ul[@class='list-group']//li[@class='list-group-item']/text()"
        worked_percent = "//*/ul[@class='list-group']//li[@class='list-group-item']/span[@class='label label-info']/text()"