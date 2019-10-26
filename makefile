all: crawl

crawl: crawl.py ./crawlutil/crawlutil.py ./Testing/test_get_links.py ./Testing/test_keywords.py
	dos2unix $^
	chmod +x $^

clean: 
	chmod -x ./crawl.py
	chmod -x ./crawlutil/crawlutil.py
	chmod -x ./Testing/test_get_links.py
	chmod -x ./Testing/test_keywords.py