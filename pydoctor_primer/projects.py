from __future__ import annotations

from pydoctor_primer.model import Project

def get_projects() -> list[Project]:
    projects = [
        # PROJECTS USING PYDOCTOR
        Project(
            location="https://github.com/twisted/pydoctor",
            pydoctor_cmd="{pydoctor} ./pydoctor --privacy='HIDDEN:pydoctor.test'", 
            expected_success=True
        ),
        Project(
            location="https://github.com/twisted/twisted",
            pydoctor_cmd="{pydoctor} ./src/twisted", 
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
            pydoctor_cmd=("{pydoctor} --project-base-dir=. temporalio"), 
        ),
        Project(
            location="https://github.com/agx/git-buildpackage",
            pydoctor_cmd="{pydoctor} gbp",
            revision='debian/0.9.32',
        ),
        Project(
            location="https://github.com/CMA-ES/pycma",
            pydoctor_cmd="{pydoctor} cma --docformat=restructuredtext",
        ),
        Project(
            location="https://github.com/bw2/ConfigArgParse",
            pydoctor_cmd=("{pydoctor} ./configargparse.py "
                          "--docformat=google  "
                          "--intersphinx=https://docs.python.org/3/objects.inv")
        ),
        Project(
            location="https://github.com/numbbo/coco",
            pydoctor_cmd=("{pydoctor} ./code-postprocessing/cocopp "
                          "--docformat=restructuredtext ")
        ),

        # PROJECTS NOT USING PYDOCTOR
        Project(
            location="https://github.com/google/pytype",
            pydoctor_cmd="{pydoctor} ./pytype/pytype --docformat=plaintext",
        ),
        Project(
            location="https://github.com/docutils/docutils",
            pydoctor_cmd="{pydoctor} ./docutils/docutils --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/numpy/numpy",
            pydoctor_cmd="{pydoctor} ./numpy --docformat=numpy"
        ),
        Project(
            location="https://github.com/scrapy/scrapy",
            pydoctor_cmd="{pydoctor} ./scrapy --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/lxml/lxml",
            pydoctor_cmd="{pydoctor} ./src/lxml --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/bottlepy/bottle",
            pydoctor_cmd="{pydoctor} ./bottle.py --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/sphinx-doc/sphinx",
            pydoctor_cmd="{pydoctor} ./sphinx --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/pylint-dev/pylint",
            pydoctor_cmd="{pydoctor} ./pylint --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/pylint-dev/astroid",
            pydoctor_cmd="{pydoctor} ./astroid --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/python-attrs/attrs",
            pydoctor_cmd="{pydoctor} ./src/attr --docformat=restructuredtext"
        ),
        Project(
            location="https://github.com/pypa/twine",
            pydoctor_cmd="{pydoctor} ./twine --docformat=restructuredtext",
        ),
        Project(
            location="https://github.com/urllib3/urllib3",
            pydoctor_cmd="{pydoctor} ./src/urllib3 --docformat=restructuredtext",
        ),

    ]
    assert len(projects) == len({p.name for p in projects})
    return projects
