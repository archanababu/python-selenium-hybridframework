# python-selenium-hybridframework

Designing selenium hybrid framework using page object model

# To run test on desired browser

pytest -s -v TestCases\Test_Login.py --browser chrome

pytest -s -v TestCases\Test_Login.py --browser firefox

# To run test parallel

pytest -s -v -n=2 TestCases\Test_Login.py

-n = 2 (-n means number of workers. At max 3, otherwise the performance will be slow)

# To generated pytest-html report

pytest -s -v -n=2 --html=Reports\report.html TestCases\Test_Login.py

# To group testcases using pytest.mark

pytest -s -v -m "regression" --html=Reports\report.html TestCases\
pytest -s -v -m "sanity" --html=Reports\report.html TestCases\
pytest -s -v -m "sanity or regression" --html=Reports\report.html TestCases\
pytest -s -v -m "sanity and regression" --html=Reports\report.html TestCases\
