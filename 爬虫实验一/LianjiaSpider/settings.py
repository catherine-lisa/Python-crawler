BOT_NAME = 'Spider'

SPIDER_MODULES = ['Spider.spiders']
NEWSPIDER_MODULE = 'Spider.spiders'

ITEM_PIPELINES = {
 'Spider.pipelines.LianjiaPipeline': 300,
}

