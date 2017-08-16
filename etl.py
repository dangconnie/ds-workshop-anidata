import luigi
import requests

class FetchAndReverse(luigi.Task):
    output_filename = luigi.Parameter(default='outfile')
    url = luigi.Parameter(default='https://google.com')

    def output(self):
        return luigi.LocalTarget(self.output_filename)

    def run(self):
        response = requests.get(self.url)
        source = response.text
        doctype = source[:16]
        doc_flip = doctype[::-1]
        output_target = self.output()

        with output_target.open('w') as ot:
            ot.write(doc_flip)

if __name__ == '__main__':
    luigi.run(['FetchAndReverse','--local-scheduler'])

