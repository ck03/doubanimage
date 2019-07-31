# doubanimage
scrapy下載圖片:
在pipelines.py新增一個中間件DoubanImgDownloadPipeline
<ul>
  <li>
    <h2>get_media_requests</h2>--下載圖片到本地
  </li>
  <li>
    下載完成後會執行item_completed,這裡可以利用參數results做額外的處理
  </li>
</ul>
  
 
