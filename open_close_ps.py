import win32com.client
import pythoncom
import subprocess
import time
def main():
	print ('Opening ps')
	psApp = win32com.client.Dispatch("Photoshop.Application")
	print ('rest for 5 second')
	time.sleep(5.0)
	pythoncom.CoInitialize()
	WMI = win32com.client.GetObject('winmgmts:')
	all_process = WMI.ExecQuery('SELECT * FROM Win32_Process where Name="Photoshop.exe"')
	for process in all_process:
		#logging.error( 'Run taskkill %s' % process.name)
		print ('Run taskkill %s' % process.name)
		subprocess.Popen('taskkill /F /pid %s' % process.processid,
						 stderr=subprocess.PIPE,
						 stdout=subprocess.PIPE,
						 )
		time.sleep(1.0)
	pythoncom.CoUninitialize ()
if __name__ == "__main__":
	main()	