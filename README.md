# gitlab-batchedit

These tools were created to make editing Gitlab objects easier when dealing with lots of objects.

## `issues.py`

### Filtering

You can filter based on the properties provided by the [Gitlab API](https://docs.gitlab.com/ce/api/issues.html).

The filtered issues can printed to the console.

Example:

```python
from gitlabbatchedit import issues

i = IssueManager(project='ao-mvp-backlog')
filtered = i.filter(milestones='sprint1-1', log=True)
```

### Renaming

Example:

All opening square brackets in the issue titles are removed.

```python
from gitlabbatchedit import issues

i = IssueManager(project='ao-mvp-backlog')
i.rename(i.issues, search_pattern=r'\[', replace_with=r'')
```

