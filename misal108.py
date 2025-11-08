#108ci sual
#İnformasiyanın həcmi bitlə verilmişdir. Onu bayta, kilobayta və meqabayta çevirin.
while True:
	def həcm(x):
		byte = 8*x
		kilobyte = 1024*x
		megabyte = (1024**2)*x
		print(f" bayt: {byte}, kilobayt: {kilobyte},megabayt: {megabyte}")
	
	
	n = int(input(" İnformasiyanın həcmini bitlə yazın: "))
	həcm(n)