from requestium import Session, Keys
import tqdm
import os
import argparse


class IslandoraReviewer:
    def __init__(self, pids_to_review):
        self.s = Session(
            webdriver_path='/usr/local/bin/chromedriver',
            browser='chrome',
            default_timeout=15,
            webdriver_options={'arguments': ['headless']}
        )
        self.for_review = pids_to_review
        self.already_created = self.__find_already_created()
        self.__process__()

    def __take_screenshot__(self, output, id='region-content'):
        original_size = self.s.driver.get_window_size()
        required_width = self.s.driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.s.driver.execute_script('return document.body.parentNode.scrollHeight')
        self.s.driver.set_window_size(required_width, required_height)
        self.s.driver.find_element_by_xpath(f'//div[@id="{id}"]').screenshot(f'{output}.png')
        self.s.driver.set_window_size(original_size['width'], original_size['height'])
        return

    def __process__(self):
        for pid in tqdm.tqdm(self.for_review):
            if pid in self.already_created:
                pass
            else:
                self.s.driver.get(f'https://digital.lib.utk.edu/collections/islandora/object/{pid}')
                self.__click_details(pid)
                self.__take_screenshot__(f'screenshots/{pid.replace(":", "_")}', 'zone-content')
        return

    def __find_already_created(self):
        already_created = []
        for p, d, files in os.walk('screenshots'):
            for file in files:
                already_created.append(file.replace('_', ':').replace('.png', ''))
        return already_created

    def __click_details(self, pid):
        try:
            l = self.s.driver.find_element_by_xpath('//a[@class="fieldset-title"]')
            self.s.driver.execute_script('arguments[0].click();', l)
        except:
            print(pid)
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build a batch of screenshots.')
    parser.add_argument("-b", "--batch", dest="batch", help="Specify batch.")
    args = parser.parse_args()
    for_review = []
    with open(args.batch, 'r') as current_batch:
        for line in current_batch:
            for_review.append(line.strip())
    x = IslandoraReviewer(for_review)
