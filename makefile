all: crawl

crawl: crawl.py ./crawlutil/crawlutil.py
	dos2unix $^
	chmod +x $^

test:
	dos2unix ./Testing/test_*.py
	chmod +xr ./Testing/test_*.py

clean: 
	chmod -x ./crawl.py
	chmod -x ./crawlutil/crawlutil.py
	chmod -xr ./Testing/test_*.py