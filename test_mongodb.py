import pymongo
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
print(dblist)
if "mongotest" in dblist:
    print("数据库已存在！")
mydb = myclient["mongotest"]

collist = mydb.list_collection_names()
if "items" in collist:
    print("集合已存在！")
mycol = mydb["items"]
item_data = {"category_id": 1, "supplier_category_id": 0,
             "skc": "st2204049749099993"}
# item_data = {"localSizeList":{"category_id":0,"supplier_category_id":0,"skc":"st2204049749099993","size_rule_list":null,"country_code":"","category_name":"","skc_filter_time":null,"config_id":null,"goods_id":10283098},"wishGood":0,"model":{},"tsp":[{"c7d_top_checkout_uv":"","goods_id":"10283098","premium_series_id":"","current_top_browsing_uv":"","brand":"","c7d_top_wishlist_uv":""}],"multiLocalSize":{"category_id":0,"supplier_category_id":0,"skc":"st2204049749099993","size_rule_list":{},"category_name":"","skc_filter_time":null,"config_id":null,"goods_id":10283098},"sizeInfoDes":{"multiPartFlag":0,"multiPartInfo":[],"sizeInfo":[{"attr_id":87,"attr_name":"Size","attr_value_id":568,"attr_value_name":"S","attr_value_name_en":"S","Length ":" 21 cm","Waist Size ":" 100-62 cm"},{"attr_id":87,"attr_name":"Size","attr_value_id":417,"attr_value_name":"M","attr_value_name_en":"M","Length ":" 22 cm","Waist Size ":" 104-66 cm"},{"attr_id":87,"attr_name":"Size","attr_value_id":387,"attr_value_name":"L","attr_value_name_en":"L","Length ":" 23 cm","Waist Size ":" 108-70 cm"}],"sizeInfoInch":[{"attr_id":87,"attr_name":"Size","attr_value_id":568,"attr_value_name":"S","attr_value_name_en":"S","Length ":" 8.3 inch","Waist Size ":" 39.4-24.4 inch"},{"attr_id":87,"attr_name":"Size","attr_value_id":417,"attr_value_name":"M","attr_value_name_en":"M","Length ":" 8.7 inch","Waist Size ":" 40.9-26 inch"},{"attr_id":87,"attr_name":"Size","attr_value_id":387,"attr_value_name":"L","attr_value_name_en":"L","Length ":" 9.1 inch","Waist Size ":" 42.5-27.6 inch"}],"sizeUnit":0,"allcmFlag":1,"sizeInfoAttribute":[],"basicAttribute":{"image_url":"http://img.ltwebstatic.com/images3_pi/2022/01/28/164334610316712508956e54db47e16bdc4da4e983.jpg","attribute_info":[{"name":"Your bust","sort":1,"desc":"Measure the circumference over the fullest part of your bust."},{"name":"Your waist","sort":2,"desc":"Measure your waist at the thinnest place.\n"},{"name":"Your hips","sort":3,"desc":"Measure the fullest part of your hips.\n"}],"base_code_info":[{"size":"S","Height":"165-170 cm","Bust":"86-90 cm","Waist Size":"66-70 cm","Hip Size":"91-95 cm"},{"size":"M","Height":"165-170 cm","Bust":"90-94 cm","Waist Size":"70-74 cm","Hip Size":"95-99 cm"},{"size":"L","Height":"170-175 cm","Bust":"95-101 cm","Waist Size":"75-81 cm","Hip Size":"100-106 cm"}],"base_code_info_inch":[{"size":"S","Height":"65-66.9 inch","Bust":"33.9-35.4 inch","Waist Size":"26-27.6 inch","Hip Size":"35.8-37.4 inch"},{"size":"M","Height":"65-66.9 inch","Bust":"35.4-37 inch","Waist Size":"27.6-29.1 inch","Hip Size":"37.4-39 inch"},{"size":"L","Height":"66.9-68.9 inch","Bust":"37.4-39.8 inch","Waist Size":"29.5-31.9 inch","Hip Size":"39.4-41.7 inch"}],"base_code_info_other":[],"base_code_show_mode":0},"braRecommendSize":[]},"getSeriesAndBrand":{"skc":"st2204049749099993","brand":null,"series":{"id":1953,"name":"SHEIN WOMEN","image_url":"","corner_img_left":null,"corner_img_right":null,"main_site":"shein","goods_id":null},"goods_id":10283098},"country":"JP","getSellingPoints":[],"gradeState":[{"skc":"st2204049749099993","goods_id":10283098,"new_product_unsale":0}],"detail":{"goods_id":"10283098","cat_id":"3056","goods_sn":"st2204049749099993","goods_url_name":"Rhinestone Rib knit Sports Brief","supplier_id":"2113015","goods_name":"Rhinestone Rib-knit Sports Brief","original_img":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4.jpg","is_stock_enough":"1","goods_thumb":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4_thumbnail_220x293.jpg","goods_img":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4_thumbnail_405x552.jpg","brand":"","sizeTemplate":{"image_url":"http://img.ltwebstatic.com/images3_pi/2021/12/01/1638324070a64eb2a4f39a00f9a278c978052d00ff.jpg","description_multi":[{"sort":1,"name":"Bottom Waist","description":"Measure straight across the top of the waistband from edge to edge."},{"sort":2,"name":"Bottom Length","description":"Measure from the waistband to the leg opening or hem."}]},"goods_desc":"","supplier_top_category_id":"231","parent_id":"3055","is_on_sale":"1","is_virtual_stock":"0","stock":"999","is_init":"1","is_pre_sale":"0","is_pre_sale_end":"0","isMultiPartProduct":0,"multiPartInfo":[],"mainSaleAttrShowMode":2,"productDetails":[{"attr_id":73,"attr_value_id":"515","attr_name":"Pattern Type","attr_name_en":"Pattern Type","value_sort":1,"attr_select":1,"attr_sort":7,"left_show":1,"attr_value":"Plain","attr_value_en":"Plain","attr_desc":"","attr_image":""},{"attr_id":31,"attr_value_id":"550","attr_name":"Details","attr_name_en":"Details","value_sort":1,"attr_select":1,"attr_sort":9,"left_show":1,"attr_value":"Rhinestone","attr_value_en":"Rhinestone","attr_desc":"","attr_image":""},{"attr_id":27,"attr_value_id":"112","attr_name":"Color","attr_name_en":"Color","value_sort":1,"attr_select":1,"attr_sort":20,"left_show":1,"attr_value":"Black","attr_value_en":"Black","attr_desc":"","attr_image":""},{"attr_id":133,"attr_value_id":"135","attr_name":"Panty Type","attr_name_en":"Panty Type","value_sort":1,"attr_select":1,"attr_sort":23,"left_show":1,"attr_value":"Thongs & V-Strings","attr_value_en":"Thongs & V-Strings","attr_desc":"","attr_image":""},{"attr_id":39,"attr_value_id":"281","attr_name":"Fabric","attr_name_en":"Fabric","value_sort":1,"attr_select":1,"attr_sort":53,"left_show":1,"attr_value":"High Stretch","attr_value_en":"High Stretch","attr_desc":"","attr_image":""},{"attr_id":160,"attr_value_id":"466","attr_name":"Material","attr_name_en":"Material","value_sort":1,"attr_select":1,"attr_sort":63,"left_show":1,"attr_value":"Nylon","attr_value_en":"Nylon","attr_desc":"","attr_image":""},{"attr_id":62,"attr_value_id":"466","attr_name":"Composition","attr_name_en":"Composition","value_sort":1,"attr_select":1,"attr_sort":65,"left_show":1,"attr_value":"90% Nylon","attr_value_en":"90% Nylon","attr_desc":"","attr_image":""},{"attr_id":62,"attr_value_id":"621","attr_name":"Composition","attr_name_en":"Composition","value_sort":1,"attr_select":1,"attr_sort":65,"left_show":1,"attr_value":"10% Spandex","attr_value_en":"10% Spandex","attr_desc":"","attr_image":""},{"attr_id":1000069,"attr_value_id":"1002238","attr_name":"Care Instructions","attr_name_en":"Care Instructions","value_sort":1,"attr_select":1,"attr_sort":67,"left_show":1,"attr_value":"Machine wash or professional dry clean","attr_value_en":"Machine wash or professional dry clean","attr_desc":"","attr_image":""},{"attr_id":207,"attr_value_id":"763","attr_name":"Sheer","attr_name_en":"Sheer","value_sort":1,"attr_select":1,"attr_sort":79,"left_show":1,"attr_value":"Yes","attr_value_en":"Yes","attr_desc":"","attr_image":""},{"attr_id":1000095,"attr_value_id":"1004886","attr_name":"Activity","attr_name_en":"Activity","value_sort":1,"attr_select":1,"attr_sort":83,"left_show":1,"attr_value":"Daily & Casual","attr_value_en":"Daily & Casual","attr_desc":"","attr_image":""}],"mainSaleAttribute":[{"attr_id":27,"attr_value_id":"112","attr_name":"Color","attr_name_en":"Color","value_sort":1,"attr_select":1,"attr_sort":20,"left_show":1,"attr_value":"Black","attr_value_en":"Black","attr_desc":"","attr_image":""}],"comment":{"comment_num":"0","comment_rank":"0"},"is_subscription":"0","promotionInfo":[],"promotion":null,"color_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201242eef23cdf5ae9be3b34733af57dc0f7c.jpg","productRelationID":"t22040497490","retailPrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"store_code":1,"business_model":0,"goods_img_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4_thumbnail_405x552.webp","original_img_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4.webp","salePrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"unit_discount":"0","special_price_old":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"is_clearance":0,"limit_count":"7","flash_goods":{"is_flash_goods":0},"isPriceConfigured":1,"appPromotion":[],"rewardPoints":3,"doublePoints":0,"color_type":"0","beautyCategory":false,"needAttrRelation":false,"brandInfo":null,"series":{"id":1953,"name":"SHEIN WOMEN","image_url":"","corner_img_left":null,"corner_img_right":null,"main_site":"shein","goods_id":null}},"commentInfoLocal":{},"exclusivePromotionPrice":null,"more_goods_imgs":[],"getBeautyGoodsDesc":{"goodsDesc":"","goodsComponent":"","beautyCategory":0},"rule_id":0,"getItemPlusSize":{},"cccTemplateData":{"appTemplate":1,"content":[{"detailImg":"0","sizeChart":"1","description":"1","countCell":"0","imgSrc":"","colorType":"0"}],"id":992322,"sourceId":1252677,"tempCode":null,"tempType":1,"templateId":26},"getOtherOptions":[],"soldoutColor":[],"commentInfo":{},"currentCat":{"cat_id":"3056","site_id":"7","url_cat_id":"3056","cat_url_name":"Women Sports Briefs","goods_type_id":"0","show_in_nav":"1","image":"","image_app":"","parent_id":"3055","sort_order":"0","is_leaf":"1","is_return":"1","cat_name":"Women Sports Briefs","meta_title":"","meta_keywords":"","meta_description":"","cat_desc":"","category_description_seo":"","left_description":"","language_flag":"en"},"relation_color":[],"skcSort":{},"parentCats":{"cat_id":"3195","url_cat_id":"3195","goods_type_id":"0","cat_url_name":"Sports","cat_name":"Sports","parent_id":"0","sort_order":"0","is_leaf":"0","goods_num":"0","multi":{"cat_id":"3195","cat_name":"Sports","meta_title":"","meta_keywords":"","meta_description":"","cat_desc":"","language_flag":"en"},"children":[{"cat_id":"1894","url_cat_id":"1894","goods_type_id":"0","cat_url_name":"Women Activewear","cat_name":"Women Activewear","parent_id":"3195","sort_order":"0","is_leaf":"0","goods_num":"0","multi":{"cat_id":"1894","cat_name":"Women Activewear","meta_title":"","meta_keywords":"","meta_description":"","cat_desc":"","language_flag":"en"},"children":[{"cat_id":"3055","url_cat_id":"3055","goods_type_id":"0","cat_url_name":"Women Sports Intimates","cat_name":"Women Sports Intimates","parent_id":"1894","sort_order":"0","is_leaf":"0","goods_num":"0","multi":{"cat_id":"3055","cat_name":"Women Sports Intimates","meta_title":"","meta_keywords":"","meta_description":"","cat_desc":"","language_flag":"en"},"children":[{"cat_id":"3056","url_cat_id":"3056","goods_type_id":"0","cat_url_name":"Women Sports Briefs","cat_name":"Women Sports Briefs","parent_id":"3055","sort_order":"0","is_leaf":"1","goods_num":"0","multi":{"cat_id":"3056","cat_name":"Women Sports Briefs","meta_title":"","meta_keywords":"","meta_description":"","cat_desc":"","language_flag":"en"},"children":[]}]}]}]},"metaInfo":{"meta_title":"Rhinestone Rib-knit Sports Brief -SHEIN","meta_keywords":"Rhinestone Rib-knit Sports Brief -SHEIN","meta_description":"Shop Rhinestone Rib-knit Sports Brief online. SHEIN offers Rhinestone Rib-knit Sports Brief & more to fit your fashionable needs."},"hotColorList":[{"hot_color":"","goods_id":"10283098","tag":"","new_arrival_28":"1"}],"attrSizeList":{"sale_attr_list":{"10283098":{"goods_id":"10283098","goods_sn":"st2204049749099993","skc_name":"st2204049749099993","sku_list":[{"sku_code":"I4gxhaeq22j5","stock":999,"sku_sale_attr":[{"attr_id":87,"attr_name":"Size","attr_name_en":"Size","attr_value_id":568,"attr_value_name":"S","attr_value_name_en":"S"}],"price":{"retailPrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"salePrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"unit_discount":0},"rewardPoints":3,"doublePoints":0},{"sku_code":"I4gxhaervmh0","stock":999,"sku_sale_attr":[{"attr_id":87,"attr_name":"Size","attr_name_en":"Size","attr_value_id":417,"attr_value_name":"M","attr_value_name_en":"M"}],"price":{"retailPrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"salePrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"unit_discount":0},"rewardPoints":3,"doublePoints":0},{"sku_code":"I4gxhaetzaqo","stock":999,"sku_sale_attr":[{"attr_id":87,"attr_name":"Size","attr_name_en":"Size","attr_value_id":387,"attr_value_name":"L","attr_value_name_en":"L"}],"price":{"retailPrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"salePrice":{"amount":"450","amountWithSymbol":"¥450","usdAmount":"3.42","usdAmountWithSymbol":"US$3.42"},"unit_discount":0},"rewardPoints":3,"doublePoints":0}],"skc_sale_attr":[{"attr_id":87,"attr_name":"Size","attr_value_list":[{"attr_value_id":568,"attr_value_name":"S","attr_value_name_en":"S","attr_std_value":""},{"attr_value_id":417,"attr_value_name":"M","attr_value_name_en":"M","attr_std_value":""},{"attr_value_id":387,"attr_value_name":"L","attr_value_name_en":"L","attr_std_value":""}]}]}},"attrSize":[]},"afterPayInfo":{},"goods_imgs":{"main_image":{"origin_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4.jpg","thumbnail":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4_thumbnail_220x293.jpg","medium_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4_thumbnail_405x552.jpg","thumbnail_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4_thumbnail_220x293.webp","origin_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4.webp","medium_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/16506201173c3e275bdef151a6db1631346f8887f4_thumbnail_405x552.webp"},"detail_image":[{"origin_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011855003a246975ee637da0719b6923eb39.jpg","medium_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011855003a246975ee637da0719b6923eb39_thumbnail_405x552.jpg","thumbnail":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011855003a246975ee637da0719b6923eb39_thumbnail_220x293.jpg","thumbnail_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011855003a246975ee637da0719b6923eb39_thumbnail_220x293.webp","origin_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011855003a246975ee637da0719b6923eb39.webp","medium_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011855003a246975ee637da0719b6923eb39_thumbnail_405x552.webp"},{"origin_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011905b1ab6a9823086d1e14b7a0f9592773.jpg","medium_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011905b1ab6a9823086d1e14b7a0f9592773_thumbnail_405x552.jpg","thumbnail":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011905b1ab6a9823086d1e14b7a0f9592773_thumbnail_220x293.jpg","thumbnail_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011905b1ab6a9823086d1e14b7a0f9592773_thumbnail_220x293.webp","origin_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011905b1ab6a9823086d1e14b7a0f9592773.webp","medium_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062011905b1ab6a9823086d1e14b7a0f9592773_thumbnail_405x552.webp"},{"origin_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/1650620120eb1fffb4eaa5b2389ffc0290128ec159.jpg","medium_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/1650620120eb1fffb4eaa5b2389ffc0290128ec159_thumbnail_405x552.jpg","thumbnail":"//img.ltwebstatic.com/images3_pi/2022/04/22/1650620120eb1fffb4eaa5b2389ffc0290128ec159_thumbnail_220x293.jpg","thumbnail_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/1650620120eb1fffb4eaa5b2389ffc0290128ec159_thumbnail_220x293.webp","origin_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/1650620120eb1fffb4eaa5b2389ffc0290128ec159.webp","medium_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/1650620120eb1fffb4eaa5b2389ffc0290128ec159_thumbnail_405x552.webp"},{"origin_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062012105009a07db8e0be5ec950c31d84a6007.jpg","medium_image":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062012105009a07db8e0be5ec950c31d84a6007_thumbnail_405x552.jpg","thumbnail":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062012105009a07db8e0be5ec950c31d84a6007_thumbnail_220x293.jpg","thumbnail_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062012105009a07db8e0be5ec950c31d84a6007_thumbnail_220x293.webp","origin_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062012105009a07db8e0be5ec950c31d84a6007.webp","medium_image_webp":"//img.ltwebstatic.com/images3_pi/2022/04/22/165062012105009a07db8e0be5ec950c31d84a6007_thumbnail_405x552.webp"}],"video_url":""}}
# item_data = json.load(mydict)
# print(item_data)
x = mycol.insert_one(item_data)
print(x.inserted_id)
