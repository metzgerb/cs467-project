all: crawl

crawl: crawl.py ./crawlutil/crawlutil.py
	dos2unix $^
	chmod +x $^

test: ./Testing/test_%.py
	dos2unix $^
	chmod +x $^

clean: 
	chmod -x ./crawl.py
	chmod -x ./crawlutil/crawlutil.py
	chmod -xr ./Testing/test_*.py