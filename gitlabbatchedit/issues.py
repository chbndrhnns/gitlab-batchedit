import os
import re
from gitlab import Gitlab

from gitlabbatchedit import settings


class IssueManager:
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, project='ao-mvp-backlog', gitlab=None):
        if gitlab is None:
            self.gitlab = Gitlab.from_config('pannet', ['.gitlabconfig', os.path.join(IssueManager.dir_path, '..', '.gitlabconfig')])
        self.gitlab.auth()
        self.project = self.gitlab.projects.list(search=project)[0]
        self.issues = self.project.issues.list()

    def log(self, issues=None):
        settings.logging.info('Logging issues...')
        if issues is None:
            issues = self.issues
        for i in issues:
            settings.logging.info('{}'.format(i.title))

    def filter(self, log=False, **kwargs):
        settings.logging.info('Applying filter: {}'.format(kwargs))
        filtered = self.project.issues.list(**kwargs)
        if log:
            self.log(filtered)
        settings.logging.info('Found {} matching issues'.format(len(filtered)))
        return filtered

    def rename(self, issues=None, search_pattern='', replace_with='', dry_run=True):
        if issues is None:
            issues = self.issues
        if len(issues) is 0:
            settings.logging.info('No issues to process')
            return

        settings.logging.info('=== {} Searching for "{}", Replacing with "{}" ==='.format("DRY RUN:" if dry_run is True else "", search_pattern, replace_with))
        for i in issues:
            new_title = re.sub(search_pattern, replace_with, i.title)
            settings.logging.info('FROM "{}" TO "{}"'.format(i.title, new_title))
            if not dry_run:
                i.title = new_title


def main():
    i = IssueManager(project='ao-mvp-backlog')
    filtered = i.filter(milestones='sprint1-1')

    i.log(filtered)

    # examples
    # i.rename(filtered, search_pattern=r'AO-US-(\d+).+', replace_with=r'\1')
    # i.rename(filtered, search_pattern=r'VNF', replace_with=r'BLA')
    # i.rename(filtered, search_pattern=r'\[', replace_with=r'')


if __name__ == '__main__':
    main()
