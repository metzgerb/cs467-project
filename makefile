all: crawl

crawl: crawl.py ./crawlutil/crawlutil.py
	dos2unix $^
	chmod +x $^

test:
	dos2unix ./Testing/test_*.py
	chmod +x ./Testing/test_*.py

clean: 
	chmod -x ./crawl.py
	chmod -x ./crawlutil/crawlutil.py
	chmod -x ./Testing/test_*.py