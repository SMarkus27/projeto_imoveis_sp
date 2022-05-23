from gc import callbacks
import scrapy


class CourseraSpider(scrapy.Spider):
    name = 'olx'
    start_urls = ['https://sp.olx.com.br/sao-paulo-e-regiao/imoveis/']

    def parse(self, response):
        items = response.xpath('//ul[@id="ad-list"]/li')
        for item in items:
            url = item.xpath('.//a/@href').extract_first()
            if url is not None:
                yield scrapy.Request(
                    url = url,
                    callback = self.parse_details
                )
        for _ in range(200):
            next_page = response.xpath('//div[contains(@class, "sc-hmzhuo fFyjgz sc-jTzLTM iwtnNi")]//a[@data-lurker-detail="next_page"]/@href').extract_first()

            if next_page:
                yield scrapy.Request(
                    url = next_page,
                    callback = self.parse
                )

    def parse_details(self,response):
        category = response.xpath('//dt[contains(text(),"Categoria")]/following-sibling::a/text()').extract_first()
        iptu = response.xpath('//dt[contains(text(), "IPTU")]/following-sibling::dd/text()').extract_first()
        bathrooms = response.xpath('//dt[contains(text(), "Banheiros")]/following-sibling::dd/text()').extract_first()
        type_house = response.xpath('//dt[contains(text(), "Tipo")]/following-sibling::a/text()').extract_first()
        size = response.xpath('//dt[contains(text(), "Área útil")]/following-sibling::dd/text()').extract_first()
        bedrooms = response.xpath('//dt[contains(text(), "Quartos")]/following-sibling::a/text()').extract_first()
        garage = response.xpath('//dt[contains(text(), "Vagas na garagem")]/following-sibling::dd/text()').extract_first()
        condominium = response.xpath('//dt[contains(text(), "Condomínio")]/following-sibling::dd/text()').extract_first()
        
        yield{
            'category': category,
            'iptu': iptu,
            'bathrooms': bathrooms,
            'type_house': type_house,
            'size': size,
            'bedrooms': bedrooms,
            'garage': garage,
            'condominium': condominium

        }