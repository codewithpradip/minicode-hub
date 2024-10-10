import scrapy

base_url = 'https://bg.annapurnapost.com/api/news/list?page={}&per_page=21&category_alias=tech&isCategoryPage=1'
page_num = 1

class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['www.annapurnapost.com']
    start_urls = [base_url.format(page_num)]

    def parse(self, response):
        global page_num
        json_data = response.json()
        print(json_data["status"])
        print(page_num)

        for data in json_data["data"]:
            yield{
                'post': data["title"],
                'slug': data["slug"],
                'publishOn': data["publishOn"],  
                'featuredImageURL': f"https://bg.annapurnapost.com/{data['featuredImage']}"
            }
        
        # pagination method 1

        # p = [4,3,2]
        # for n in p:
        #     print("page number")
        #     print(n)
        #     next_page_url = base_url.format(n)
        #     yield scrapy.Request(next_page_url, callback=self.parse)


        # pagination method 2

        page_num +=1
        if page_num <= 4:
            next_page_url = base_url.format(page_num)
            yield scrapy.Request(next_page_url, callback=self.parse)
          

