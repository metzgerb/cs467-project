all: crawl

crawl: crawl.py crawlutil.py test_get_links.py
	dos2unix $^
	chmod +x $^

clean: 
	chmod -x ./crawl.py
	chmod -x ./crawlutil.py
	chmod -x ./test_get_links.py