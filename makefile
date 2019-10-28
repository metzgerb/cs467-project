all: crawl

crawl: crawl.py ./crawlutil/crawlutil.py
	dos2unix $^
	chmod +x $^

tests:
	dos2unix ./Testing/test_keywords.py
	dos2unix ./Testing/test_get_links.py
	dos2unix ./Testing/test_get_random.py
	chmod +x ./Testing/test_keywords.py
	chmod +x ./Testing/test_get_links.py
	chmod +x ./Testing/test_get_random.py

run_tests:
	python3 ./Testing/test_keywords.py
	python3 ./Testing/test_get_links.py
	python3 ./Testing/test_get_random.py
	
run_tests_d:
	python3 ./Testing/test_keywords.py debug
	python3 ./Testing/test_get_links.py debug
	python3 ./Testing/test_get_random.py debug
	
clean: 
	chmod -x ./crawl.py
	chmod -x ./crawlutil/crawlutil.py
	chmod -x ./Testing/test_keywords.py
	chmod -x ./Testing/test_get_links.py
	chmod -x ./Testing/test_get_random.py