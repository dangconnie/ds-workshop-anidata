import luigi
import requests

class FetchAndReverse(luigi.Task):
	output_filename = luigi.Parameter(default='outfile')
	url = luigi.Parameter(default='http://google.com')
 
	def ouptput(self):
		# FetchAndReverse.output_filename = 'other' ===> doing this changes all inputs. We want it all the same.
		return luigi.LocalTarget(self.output_filename)

	def run(self):
		response = requests.get(self.url)
		source = response.text # view source on a webpage
		doctype = source[:16] # grab the first 16 characters in the source
		doc_flip = doctype [::-1] # flip/reverse what we just grabbed
		output_target = self.output() # open up output file
		with output_target.open ('w') as ot: # open the output_target in write mode (hence the 'w'). Name the file as 'ot'.
			ot.write(doc_flip) # write to 'ot':

# = is assign, == is evaluate
if __name__ == '__main__':
	# (taskname, )
	luigi.run(['FetchAndReverse','--local-scheduler'])
