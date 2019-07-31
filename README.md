# doubanimage
爬取http://www.douban.com/photos/album/1638835355
<br/>
scrapy下載圖片:
在pipelines.py新增一個中間件DoubanImgDownloadPipeline
<ul>
  <li>
    <h2>get_media_requests--下載圖片到本地</h2>
  </li>
  <li>
    <h2>下載完成後會執行item_completed,這裡可以利用參數results做額外的處理後回傳item到Doubanimage2Pipeline</h2>
    <h2>當然在settings.py的權值要自己設定</h2>
  </li>
  <li>
    <h2>回傳到Doubanimage2Pipeline後可在close_spider將資料同步傳至momgodb及json</h2>
  </li>
</ul>
  
 
