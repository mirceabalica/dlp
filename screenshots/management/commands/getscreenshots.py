from django.core.management.base import BaseCommand
from selenium import webdriver
from StringIO import StringIO
from django.core.files import File
from screenshots.models import Screenshot
from screenshots.models import Domain


class Command(BaseCommand):
    help = 'Gets all the bento sites screenshots'


    # def add_arguments(self, parser):
    #     parser.add_argument('site_url', nargs='+', type=str)

    @staticmethod
    def _get_screenshot(driver, domain, suffix=''):
        driver.get('http://{0}{1}'.format(domain, suffix))
        return StringIO(driver.get_screenshot_as_png())

    def handle(self, *args, **options):
        site_list = Domain.objects.all()
        driver = webdriver.Firefox()

        ids = []
        for s in Screenshot.objects.all():
            ids.append(s.run_id)
        new_id = max(ids) + 1

        for domain in site_list:
            s = Screenshot(domain=domain)
            s.run_id = new_id
            png_file = self._get_screenshot(driver, domain,
                                            suffix='.lunchbox-qa.pbs.org')
            s.qa_image.save('{}.png'.format(domain), File(png_file))
            png_file.close()

            png_file = self._get_screenshot(driver, domain)
            s.production_image.save('{}.png'.format(domain), File(png_file))
            png_file.close()
        driver.quit()