from lxml import etree
from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/foo')
def ajax_ddl():
    xml = 'foo'
    return Response(xml, mimetype='text/xml')

@app.route('/rss')
def rss():
    root = etree.XML('''<?xml version="1.0"?><rss></rss>''')

    channel = etree.SubElement(root, "channel")
    title = etree.SubElement(channel, "title")
    title.text = "Azure service updates"

    link = etree.SubElement(channel, "link")
    link.text = "https://azure.microsoft.com/en-us/updates/"

    description = etree.SubElement(channel, "description")
    description.text = "Azure service updates"

    lastBuildDate = etree.SubElement(channel, "lastBuildDate")
    lastBuildDate.text = "Mon, 07 Aug 2017 12:59:04 Z"

    item = etree.SubElement(channel, "item")

    item_guid = etree.SubElement(item, "guid")
    item_guid.text = "azure-site-recovery-available-in-dod-and-new-azure-government-regions"

    item_link = etree.SubElement(item, "link")
    item_link = "https://azure.microsoft.com/en-us/updates/azure-site-recovery-available-in-dod-and-new-azure-government-regions/"

    item_title = etree.SubElement(item, "title")
    item_title.text = "Azure Site Recovery available in US DoD and new Azure Government regions"

    item_description = etree.SubElement(item, "description")
    item_description.text = "Azure Site Recovery is now available in all Azure Government regions (US DOD Central, US DOD East, US Gov Arizona, US Gov Texas, US Gov Iowa, US Gov Virginia)."

    item_pubdate = etree.SubElement(item, "pubDate")
    item_pubdate.text = "Wed, 02 Aug 2017 17:00:10 Z"


    # return etree.tostring(root,pretty_print=False)
    return Response(etree.tostring(root,pretty_print=False,xml_declaration = True, encoding='UTF-8'), mimetype='text/xml')


    # print(etree.tostring(root, pretty_print=True))
