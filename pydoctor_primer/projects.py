from __future__ import annotations

from pydoctor_primer.model import Project

def get_projects() -> list[Project]:
    projects = [
        Project(
            location="https://github.com/twisted/pydoctor",
            pydoctor_cmd="{pydoctor} ./pydoctor --privacy='HIDDEN:pydoctor.test'", 
            expected_success=True
        ),
        Project(
            location="https://github.com/twisted/twisted",
            pydoctor_cmd="{pydoctor} ./src/twisted", 
            expected_success=False
        ),
        Project(
            location="https://github.com/twisted/tubes",
            pydoctor_cmd=("{pydoctor} ./tubes --privacy='HIDDEN:tubes.test' "
                          "--intersphinx=https://docs.python.org/3/objects.inv "
                          "--intersphinx=https://docs.twisted.org/en/stable/api/objects.inv "
                          "--intersphinx=https://zopeinterface.readthedocs.io/en/latest/objects.inv "), 
            revision='v0.2.1',
            expected_success=True
        ),
        Project(
            location="https://github.com/temporalio/sdk-python",
            pydoctor_cmd=("{pydoctor} --project-base-dir=."), 
            expected_success=False
        ),
    ]
    assert len(projects) == len({p.name for p in projects})
    return projects
