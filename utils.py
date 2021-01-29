import os, json, sys
from datetime import datetime


def inference(name="", tag = True):
	'''
	if the current year is 2021, then inference function will run successfully, otherwise fails.
	Here the attribute variable holds the string version of the date in MM-DD-YYYY format
	'''

	print("Hello {}, the inference function has been successfully started".format(name))

	attribute = str(datetime.now().strftime('%m-%d-%Y'))
	response = "You license has been expired, please contact us."
	year_to_expire = int(2022)

	try:
		assert int(attribute.split('-')[-1]) == year_to_expire, response
	except AssertionError as e:
		print(response)
		sys.exit()

	# Replace your main code to operate here.
	# if the above assertion is True, it will reach until this point, otherwise it will stop in the previous line.

	if tag:
		print("inference function has been completed successfully")
		return True
	else:
		return False

if __name__ == "__main__":
	_ = inference(name="Bala")

	'''
	Function outputs,
	Case 1: if year_to_expire = int(2021)
		Hello Bala, the inference function has been successfully started
		inference function has been completed successfully
		[Finished in 0.2s]
	Case 2: if year_to_expire = int(2022)
		Hello Bala, the inference function has been successfully started
		You license has been expired, please contact us.
		[Finished in 0.2s]
	'''
