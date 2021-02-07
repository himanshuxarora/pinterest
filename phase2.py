def createpin(title,description,linkvenue,address,temp):
	print("phase2.createpin() started")
	global driver,uname
	cat =onthiscategory()
	extractionforpin()
	driver.get('https://www.pinterest.com/'+str(cat.replace(' ','-'))
	btnlst = driver.find_elements_by_tag_name('button')
	
	upldPic=driver.find_element_by_id('media-upload-input')
	
	
	upldPic.send_keys('../image/'temp)
	title = driver.find_element_by_tag_name('textarea')
	descript = driver.find_element_by_id('pin-draft-description')
	destin = driver.find_element_by_id('pin-draft-link')
	descript.send_keys(description +'\n' + address)
	destin.send_keys(linkvenue)
	title.send_keys(title)
	saver = driver.find_elements_by_tag_name('div')
	for save in saver:
		if(save.get_attribute('data-test-id')=='SaveButton'):
			sav= save
	sav.click()
	print("phase2.createpin() finished")
