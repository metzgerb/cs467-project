all: crawl

crawl: crawl.py ./crawlutil/crawlutil.py ./Testing/test_%.py
	dos2unix $<
	chmod +x $<

test: 
	echo "test"

clean: 
	chmod -x ./crawl.py
	chmod -x ./crawlutil/crawlutil.py
	chmod -xr ./Testing/test_*.py